"""Commands to interact with the user"""

from __future__ import annotations

COMMAND_CATEGORY = "user_interaction"
COMMAND_CATEGORY_TITLE = "User Interaction"

from autogpt.agents.agent import Agent
from autogpt.app.utils import clean_input
from autogpt.command_decorator import command


@command(
    "ask_user",
    (
        "If you need more details or information regarding the given goals,"
        " you can ask the user for input"
    ),
    {
        "question": {
            "type": "string",
            "description": "The question or prompt to the user",
            "required": True,
        }
    },
)
def ask_user(question: str, agent: Agent) -> str:
    resp = clean_input(agent.config, f"{agent.ai_config.ai_name} asks: '{question}': ")
    return f"The user's answer: '{resp}'"
