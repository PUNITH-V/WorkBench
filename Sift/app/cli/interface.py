from app.pipeline import research_topic
from app.memory.manager import MemoryManager


def run():
    memory = MemoryManager()

    print("Sift — Research Assistant")

    name = input("What's your name? ").strip()

    while True:
        topic = input("\nResearch topic (or 'exit'): ").strip()

        if topic.lower() == "exit":
            break

        if not topic:
            continue

        memory.remember(name, topic)

        report = research_topic(topic)

        print("\n" + report.model_dump_json(indent=2))