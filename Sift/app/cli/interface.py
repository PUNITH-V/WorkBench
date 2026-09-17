from app.memory.manager import MemoryManager
from app.pipeline import research_topic


def run():
    memory = MemoryManager()

    print("Sift — Research Assistant")

    name = memory.get_user_name()

    if name:
        print(f"Welcome back, {name}!")
    else:
        name = input("What's your name? ").strip()

        if not name:
            name = "User"

    while True:
        topic = input("\nResearch topic (or 'exit'): ").strip()

        if topic.lower() == "exit":
            print("Goodbye!")
            break

        if not topic:
            print("Please enter a topic.")
            continue

        memory.remember(name, topic)

        print(f"\nResearching: {topic}")

        report = research_topic(topic)

        print("\n--- Research Report ---")
        print(report.model_dump_json(indent=2))