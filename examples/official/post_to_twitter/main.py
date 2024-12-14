# main.py
import handgpt
from agent_twitter import agent

if __name__ == "__main__":
    handgpt.init(agent, user="your_user", password="your_password")
