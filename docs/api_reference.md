# API Reference for HandGPT

This document provides an overview of the APIs available in HandGPT. The APIs are categorized into two main sections: **Information Retrieval APIs** and **Device Control APIs**. Each API is described with its purpose, parameters, usage details, and corresponding JSON payloads for clarity.

---

## 1. Information Retrieval APIs
These APIs are used to send or retrieve information from the system.

### `reply_message`
**Description**: Sends a reply message for a given task.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `message` (str): The message to send.

**Usage Example**:
```python
api.reply_message(task_id="12345", message="This is a reply.")
```

**Corresponding JSON Payload**:
```json
{
  "type": "reply_message",
  "payload": {
    "message": "This is a reply."
  }
}
```

---

### `get_image_info`
**Description**: Retrieves image information for a given task.

- **Parameters**:
  - `task_id` (str): The ID of the task.

**Usage Example**:
```python
image_info = api.get_image_info(task_id="12345")
```

**Corresponding JSON Payload**:
```json
{
  "type": "get_image_info",
  "taskId": "12345",
  "payload": {}
}
```

---

### `get_device_info`
**Description**: Retrieves device information for a given task.

- **Parameters**:
  - `task_id` (str): The ID of the task.

**Usage Example**:
```python
device_info = api.get_device_info(task_id="12345")
```

**Corresponding JSON Payload**:
```json
{
  "type": "get_device_info",
  "taskId": "12345",
  "payload": {}
}
```

---

### `get_llm`
**Description**: Sends a request to a large language model (LLM) and retrieves the response.

- **Parameters**:
  - `model` (str, optional): The LLM model to use (default: `gpt4o`).
  - `system` (str, optional): System-specific context.
  - `user` (str, optional): User-specific context.
  - `image` (list, optional): List of images (binary or base64-encoded).
  - `history` (list, optional): Historical context.
  - `response_type` (str, optional): The format of the response (default: `json_object`).

**Usage Example**:
```python
response, history = api.get_llm(
    model="gpt4o",
    system="system message",
    user="user message",
    image=[],
    history=None,
    response_type="json_object"
)
```

**Corresponding JSON Payload**:
```json
{
  "type": "get_llm",
  "payload": {
    "model": "gpt4o",
    "system": "system message",
    "user": "user message",
    "image": [],
    "history": null,
    "response_type": "json_object"
  }
}
```

---

## 2. Device Control APIs
These APIs control the device through specific commands.

### `cmd_key`
**Description**: Sends a keyboard command.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `keys` (list): The list of keys to send.

**Usage Example**:
```python
api.cmd_key(task_id="12345", keys=["Ctrl", "C"])
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_key",
  "taskId": "12345",
  "payload": {
    "key": ["Ctrl", "C"]
  }
}
```

---

### `cmd_clipboard`
**Description**: Sets the clipboard content.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `clipboard_content` (str): The content to set in the clipboard.

**Usage Example**:
```python
api.cmd_clipboard(task_id="12345", clipboard_content="Copied text")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_clipboard",
  "taskId": "12345",
  "payload": "Copied text"
}
```

---

### `cmd_input`
**Description**: Sends a text input command.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `input_text` (str): The text to input.

**Usage Example**:
```python
api.cmd_input(task_id="12345", input_text="Hello, world!")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_input",
  "taskId": "12345",
  "payload": {
    "input": "Hello, world!"
  }
}
```

---

### `cmd_moveto`
**Description**: Moves the pointer to a specified element.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `element_id` (list): The target element ID.
  - `offset` (list, optional): Offset values for the movement.

**Usage Example**:
```python
api.cmd_moveto(task_id="12345", element_id=[21], offset=[5, 5])
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_moveto",
  "taskId": "12345",
  "payload": {
    "elementId": [21],
    "offset": [5, 5]
  }
}
```

---

### `cmd_click`
**Description**: Sends a click command on a specified element.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `element_id` (list): The target element ID.
  - `offset` (list, optional): Offset values for the click.
  - `key` (str, optional): The click key (`left`, `right`, `middle`, default: `left`).

**Usage Example**:
```python
api.cmd_click(task_id="12345", element_id=[21], offset=[0, 0], key="left")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_click",
  "taskId": "12345",
  "payload": {
    "elementId": [21],
    "offset": [0, 0],
    "key": "left"
  }
}
```

---

### `cmd_longclick`
**Description**: Sends a long-click command on a specified element.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `element_id` (list): The target element ID.
  - `offset` (list): Offset values for the click.
  - `time_sec` (float): Duration of the long click in seconds.
  - `key` (str, optional): The click key (`left`, `right`, `middle`, default: `left`).

**Usage Example**:
```python
api.cmd_longclick(task_id="12345", element_id=[21], offset=[0, 0], time_sec=2, key="left")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_longclick",
  "taskId": "12345",
  "payload": {
    "elementId": [21],
    "offset": [0, 0],
    "time": 2,
    "key": "left"
  }
}
```

---

### `cmd_slide`
**Description**: Sends a slide command between elements.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `element_id` (list): List of element IDs to slide between.
  - `offsets` (list): List of offsets for each element.
  - `time_sec` (float): Duration of the slide in seconds.
  - `key` (str, optional): The click key (`left`, `right`, `middle`, default: `left`).

**Usage Example**:
```python
api.cmd_slide(task_id="12345", element_id=[21, 25], offsets=[[0, 0], [5, 5]], time_sec=3, key="left")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_slide",
  "taskId": "12345",
  "payload": {
    "elementId": [21, 25],
    "offset": [[0, 0], [5, 5]],
    "time": 3,
    "key": "left"
  }
}
```

---

### `cmd_back`
**Description**: Sends a command to go back.

- **Parameters**:
  - `task_id` (str): The ID of the task.

**Usage Example**:
```python
api.cmd_back(task_id="12345")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_back",
  "taskId": "12345",
  "payload": {}
}
```

---

### `cmd_home`
**Description**: Sends a command to go to the home screen.

- **Parameters**:
  - `task_id` (str): The ID of the task.

**Usage Example**:
```python
api.cmd_home(task_id="12345")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_home",
  "taskId": "12345",
  "payload": {}
}
```

---

### `cmd_app`
**Description**: Sends a command to open an application.

- **Parameters**:
  - `task_id` (str): The ID of the task.
  - `app_package` (str): The package name of the application.

**Usage Example**:
```python
api.cmd_app(task_id="12345", app_package="com.tencent.mm")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_app",
  "taskId": "12345",
  "payload": {
    "app_package": "com.tencent.mm"
  }
}
```

---

### `cmd_close`
**Description**: Closes the current application.

**Usage Example**:
```python
api.cmd_close(task_id="12345")
```

**Corresponding JSON Payload**:
```json
{
  "type": "cmd_close",
  "taskId": "12345",
  "payload": {}
}
```

---

### `finished`
**Description**: Ends all operations once a task is completed.

**Usage Example**:
```python
api.finished(task_id="12345")
```

**Corresponding JSON Payload**:
```json
{
  "type": "finished",
  "taskId": "12345",
  "payload": {}
}
```

---

This document is designed to assist developers in integrating and using the provided APIs effectively.

