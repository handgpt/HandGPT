import time
import json
import base64
import prompt
import logging

logger = logging.getLogger("HandGPT")

def agent(handgpt, task_id, task_message):
    """
    主任务处理函数，用于处理任务消息并与 handgpt 进行交互。
    """
    logger.info(f"Agent started for task_id: {task_id} with message: {task_message}")
    
    # 获取设备信息
    try:
        device_info = handgpt.get_device_info(task_id)
        logger.debug(f"Device info retrieved: {device_info}")
    except Exception as e:
        logger.error(f"Failed to retrieve device info for task_id: {task_id}. Error: {e}")
        return

    # 生成系统和用户消息以获取任务 JSON
    try:
        system, user = prompt.get_task(task_message)
        task_json, history = handgpt.get_llm(system=system, user=user)
        logger.debug(f"LLM response: {task_json}")
    except Exception as e:
        logger.error(f"Error while processing LLM task for task_id: {task_id}. Error: {e}")
        return

    # 解析任务 JSON
    try:
        task = json.loads(task_json)
        logger.info(f"Task JSON parsed successfully: {task}")
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse task JSON for task_id: {task_id}. Error: {e}")
        return

    task_normal = task.get("message", "")
    handgpt.reply_message(task_id, task_normal)
    logger.info(f"Replied to task_id: {task_id} with message: {task_normal}")

    if not task.get('isTask', False):
        logger.info(f"No further actions required for task_id: {task_id}")
        return
    
    # 处理任务的具体逻辑
    process_task(handgpt, task_id, task_message, task_normal, device_info, is_foreground=True)

def process_task(handgpt, task_id, task_message, task_normal, device_info, is_foreground=False):
    """
    处理具体的任务逻辑，包括生成操作步骤并与 handgpt 交互执行操作。
    """
    logger.info(f"Processing task_id: {task_id} with initial message: {task_message}")
    
    # 提供推荐的步骤描述
    suggest_steps = '''
        Open the Twitter app
        Click the blue 加号_icon in the bottom right corner
        Click "What's happening?"
        Enter the tweet content
        Click the "Post" button
        Task finished

        Reference information:
            URL Scheme (url_scheme): twitter://
    '''
    history = None

    while True:
        try:
            # 获取屏幕信息
            screen = handgpt.get_image_info(task_id)
            logger.debug(f"Screen info retrieved for task_id: {task_id}: {screen}")

            # 解码屏幕图像
            image = base64.b64decode(screen['payload']['image'])
            elements = screen['payload']['element_list']
            print(elements)
            logger.debug(f"Decoded image and retrieved elements for task_id: {task_id}")
        except Exception as e:
            logger.error(f"Failed to retrieve or decode screen info for task_id: {task_id}. Error: {e}")
            break

        # 获取下一步操作的 prompt
        try:
            next_operation_prompt_system, next_operation_prompt_user = prompt.get_operation(
                task_normal, suggest_steps, elements
            )
            logger.info(f"Next operation prompt generated: System={next_operation_prompt_system}, User={next_operation_prompt_user}")
        except Exception as e:
            logger.error(f"Failed to generate operation prompt for task_id: {task_id}. Error: {e}")
            break

        # 与 LLM 交互获取操作步骤
        try:
            llm_response, history = handgpt.get_llm(
                system=next_operation_prompt_system,
                user=next_operation_prompt_user,
                image=[image],
                history=history
            )
            logger.info(f"LLM response for next operation: {llm_response}")
            history.pop(-2)     # history 去掉本次输入
        except Exception as e:
            logger.error(f"Error while interacting with LLM for task_id: {task_id}. Error: {e}")
            break

        # 解析 LLM 的操作响应
        try:
            next_operation = json.loads(llm_response)
            logger.info(f"Next operation parsed: {next_operation}")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse next operation JSON for task_id: {task_id}. Error: {e}")
            break

        # 判断操作是否完成
        if next_operation.get('type') == 'finished':
            logger.info(f"Task {task_id} finished successfully.")
            break

        # 执行下一步操作
        try:
            handgpt.cmd(task_id, next_operation)
            logger.info(f"Executed operation for task_id: {task_id}: {next_operation}")
        except Exception as e:
            logger.error(f"Failed to execute operation for task_id: {task_id}. Error: {e}")
            break

        # 完成后等待 7s
        time.sleep(7)