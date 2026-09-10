from common.config import (
    get_api_key,
    get_model,
    get_system_prompt,
    get_memory_limit,
    ConfigError,
)

from common.client import GroqClient
from stateful.conversation import Conversation
from stateful.memory import trim_messages


def run():
    """Run the stateful chatbot."""

    print("=" * 60)
    print("STATEFUL CHATBOT")
    print("=" * 60)
    print("This bot remembers your conversation.")
    print("Type 'quit' to exit.")
    print()

    # ---------------------------------------------------------
    # Load configuration
    # ---------------------------------------------------------

    api_key = get_api_key()
    model = get_model()
    system_prompt = get_system_prompt()
    memory_limit = get_memory_limit()

    # ---------------------------------------------------------
    # Initialize Groq client
    # ---------------------------------------------------------

    client = GroqClient(
        api_key=api_key,
        model=model
    )

    # ---------------------------------------------------------
    # Initialize conversation
    # ---------------------------------------------------------

    conversation = Conversation(
        system_prompt=system_prompt
    )

    # ---------------------------------------------------------
    # Chat loop
    # ---------------------------------------------------------

    while True:

        try:
            user_input = input("You: ").strip()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        except EOFError:
            print("\n\nInput closed.")
            break

        # -----------------------------------------------------
        # Validate input
        # -----------------------------------------------------

        if not user_input:
            print("Please enter a message.\n")
            continue

        # -----------------------------------------------------
        # Exit
        # -----------------------------------------------------

        if user_input.lower() == "quit":
            print("\nGoodbye!")
            break

        # -----------------------------------------------------
        # Add user message
        # -----------------------------------------------------

        conversation.add_user_message(
            user_input
        )

        # -----------------------------------------------------
        # Get conversation history
        # -----------------------------------------------------

        messages = conversation.get_messages()

        # -----------------------------------------------------
        # Apply memory limit
        # -----------------------------------------------------

        messages = trim_messages(
            messages,
            memory_limit
        )

        try:

            # -------------------------------------------------
            # Send ENTIRE conversation to Groq
            # -------------------------------------------------

            assistant_reply = client.get_response(
                messages
            )

        except Exception as exc:

            print(f"Error: {exc}\n")

            # Remove unanswered user message
            conversation.remove_last_message()

            continue

        # -----------------------------------------------------
        # Store assistant response
        # -----------------------------------------------------

        conversation.add_assistant_message(
            assistant_reply
        )

        # -----------------------------------------------------
        # Display response
        # -----------------------------------------------------

        print(f"Bot: {assistant_reply}\n")


def main():
    try:
        run()

    except ConfigError as exc:
        print(f"Configuration Error: {exc}")

    except Exception as exc:
        print(f"Fatal Error: {exc}")


if __name__ == "__main__":
    main()
