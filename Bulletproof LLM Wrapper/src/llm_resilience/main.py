from .llm import generate_response
from .exceptions import LLMServiceUnavailableError


def main():

    print("\n🤖 AI Assistant")
    print("=" * 40)

    user_prompt = input(
        "Ask the AI something: "
    )

    try:

        print("\n⏳ Generating response...\n")

        result = generate_response(
            user_prompt
        )

        print("🤖 AI:")
        print(result)

    except LLMServiceUnavailableError:

        print(
            "\n⚠️ Sorry, our AI service is "
            "temporarily unavailable."
        )

        print(
            "Please try again in a few moments."
        )

    except ValueError as error:

        print(
            f"\n❌ Invalid input: {error}"
        )


if __name__ == "__main__":
    main()
