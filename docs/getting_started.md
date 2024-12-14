# Getting Started with HandGPT

This guide provides a step-by-step overview for setting up and using HandGPT effectively.

---

## Workflow Overview

1. **User Interaction**:

   - Open the HandGPT app and start screen sharing.
   - Input your desired action (e.g., "Post a tweet on Twitter").

2. **Data Capture**:

   - HandGPT captures a screenshot of your device and identifies screen elements (names and IDs).
   - The app forwards this data along with your command to a customizable `agent`.

3. **Agent Processing**:

   - The `agent` processes the screen information and user command using an LLM.
   - The `agent` generates operation instructions based on the data.

4. **Execution**:

   - HandGPT executes the instructions and performs the required actions on the device.

5. **Completion**:

   - Once all tasks are completed, the `agent` sends a "finished" command to HandGPT.
   - HandGPT notifies the user that the operation is complete.

---

## Recognized Screen Elements

HandGPT identifies and assigns IDs to screen elements for simplified processing. Example:

| ID | Element Name |
| -- | ------------ |
| 1  | button       |
| 2  | ok           |
| 3  | check\_icon  |

---

## Operation Instructions

The `agent` generates operation instructions using basic actions (e.g., mouse actions, keyboard inputs). Operations are simplified by targeting elements via their IDs, improving LLM efficiency and accuracy.

Refer to the [API Reference](api_reference.md) for detailed instruction formats.

---

## Installation

Install HandGPT using pip:

```bash
pip install handgpt
```

### Verify Installation

After installation, run the following test to ensure everything is set up correctly:

```python
>>> import handgpt
>>> handgpt.test()
HandGPT OK.
```

### Environment Requirements

- Python version: `>= 3.9`

---

## Code Example

Below is an example setup for HandGPT with a custom agent.

### `main.py`

```python
import handgpt
from agent_twitter import agent  # Import the agent

if __name__ == "__main__":
    handgpt.init(agent, user="your_user", password="your_password")
```

### `agent_twitter.py`

```python
def agent(handgpt, task_id, task_message):
    # task_id: Temporary task identifier
    # task_message: User command from HandGPT
    pass
```

---

## Testing HandGPT

Run the following command to verify your HandGPT installation:

```python
>>> import handgpt
>>> handgpt.test()
HandGPT OK.
```

---

## Developer Contributions

Developers are encouraged to freely create and upload their own `agents` to extend HandGPT’s functionality. These custom agents can be shared for others to test and use.

### Upload Directory Structure

Agents should be uploaded following this directory structure:

```
HandGPT
|-- examples
|   |-- comunity
|   |   `-- developer_name
|   |       `-- agent_name
```

- **Community Contributions**: Place your custom agents under `examples/comunity/developer_name/agent_name`.
- **Official Examples**: HandGPT provides official agents in the `examples/official/` directory.

### Steps to Upload Your Agent

Follow these steps to create and upload your agent:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/handgpt/HandGPT.git
   cd examples/comunity
   ```

2. **Create Your Agent Folder**:

   Replace `developer_name` and `agent_name` with your own details:

   ```bash
   mkdir -p developer_name/agent_name
   cd developer_name/agent_name
   ````

3. **Implement Your Agent**:

   - Write your `agent_name.py` file with the required logic.
   - Optionally, include additional files such as `main.py` or `prompt.py` if needed.

4. **Test Your Agent**:
   Ensure your agent works as expected by integrating it with HandGPT.

5. **Commit and Push**:

   ```bash
   git add .
   git commit -m "Add new agent: agent_name by developer_name"
   git push origin main
   ```

This structure ensures consistency and discoverability for users.

---

## Next Steps

1. Customize your `agent` to handle specific tasks.
2. Refer to the [API Reference](api_reference.md) for detailed command formats.
3. Start using HandGPT to automate device operations effortlessly!

