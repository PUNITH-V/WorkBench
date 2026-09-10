from typing import List, Dict


Message = Dict[str, str]


def trim_messages(
    messages: List[Message],
    limit: int = 10
) -> List[Message]:
    """
    Keep the system prompt and the last 4 messages
    when the conversation exceeds the limit.
    """

    if len(messages) <= limit:
        return messages

    # First message is the system prompt
    system_message = messages[0]

    # Keep the last 4 messages
    last_four_messages = messages[-4:]

    trimmed_messages = [
        system_message
    ] + last_four_messages

    return trimmed_messages
