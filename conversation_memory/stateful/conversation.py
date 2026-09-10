from typing import List, Dict


Message = Dict[str, str]


class Conversation:
    """
    Manages the conversation history.
    """

    def __init__(self, system_prompt: str):
        if not system_prompt.strip():
            raise ValueError(
                "System prompt cannot be empty."
            )

        self.messages: List[Message] = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def add_user_message(self, content: str) -> None:
        """Add a user message."""

        if not content.strip():
            raise ValueError(
                "User message cannot be empty."
            )

        self.messages.append(
            {
                "role": "user",
                "content": content
            }
        )

    def add_assistant_message(self, content: str) -> None:
        """Add an assistant message."""

        if not content.strip():
            raise ValueError(
                "Assistant message cannot be empty."
            )

        self.messages.append(
            {
                "role": "assistant",
                "content": content
            }
        )

    def get_messages(self) -> List[Message]:
        """Return the complete conversation."""

        return list(self.messages)

    def remove_last_message(self) -> None:
        """Remove the most recent message."""

        if len(self.messages) > 1:
            self.messages.pop()

    def message_count(self) -> int:
        """Return the number of stored messages."""

        return len(self.messages)
