from common.config import (
    get_api_key,
    get_model,
    get_system_prompt,
    ConfigError,
)

from common.client import GroqClient


def run():
    """Run the stateless chatbot."""

    print("=" * 60)
    print("STATELESS CHATBOT")
    print("=" * 60)
    print("This bot has NO conversation memory.")
    print("Type 'quit' to exit.")
    print()

    # ---------------------------------------------------------
    # Load configuration
    # ---------------------------------------------------------

    api_key = get_api_key()
    model = get_model()
    system_prompt = get_system_prompt()

    # ---------------------------------------------------------
    # Create Groq client
    # ---------------------------------------------------------

    client = GroqClient(
        api_key=api_key,
        model=model
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

        if not user_input:
            print("Please enter a message.\n")
            continue

        if user_input.lower() == "quit":
            print("\nGoodbye!")
            break

        # -----------------------------------------------------
        # IMPORTANT:
        #
        # We create a NEW messages list for every request.
        #
        # Therefore, previous conversations are NOT remembered.
        # -----------------------------------------------------

        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]

        try:
            assistant_reply = client.get_response(
                messages
            )

            print(f"Bot: {assistant_reply}\n")

        except Exception as exc:
            print(f"Error: {exc}\n")


def main():
    try:
        run()

    except ConfigError as exc:
        print(f"Configuration Error: {exc}")

    except Exception as exc:
        print(f"Fatal Error: {exc}")


if __name__ == "__main__":
    main()
