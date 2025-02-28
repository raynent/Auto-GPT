"""Commands to control the internal state of the program"""

from __future__ import annotations

COMMAND_CATEGORY = "system"
COMMAND_CATEGORY_TITLE = "System"

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from autogpt.agents.agent import Agent

from autogpt.agents.features.context import get_agent_context
from autogpt.agents.utils.exceptions import InvalidArgumentError
from autogpt.command_decorator import command

logger = logging.getLogger(__name__)


@command(
    "goals_accomplished",
    "Goals are accomplished and there is nothing left to do",
    {
        "reason": {
            "type": "string",
            "description": "A summary to the user of how the goals were accomplished",
            "required": True,
        }
    },
)
def task_complete(reason: str, agent: Agent) -> None:
    """
    A function that takes in a string and exits the program

    Parameters:
        reason (str): A summary to the user of how the goals were accomplished.
    Returns:
        A result string from create chat completion. A list of suggestions to
            improve the code.
    """
    logger.info(reason, extra={"title": "Shutting down...\n"})
    quit()


@command(
    "close_context_item",
    "Close an open file, folder or other context item",
    {
        "index": {
            "type": "integer",
            "description": "The 1-based index of the context item to close",
            "required": True,
        }
    },
    available=lambda a: get_agent_context(a) is not None,
)
def close_context_item(index: int, agent: Agent) -> str:
    assert (context := get_agent_context(agent)) is not None

    if index > len(context.items) or index == 0:
        raise InvalidArgumentError(f"Index {index} out of range")

    context.close(index)
    return f"Context item {index} closed ✅"
