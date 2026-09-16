from app.pipeline import research_topic


results = research_topic("AI agents", limit=1)

print("\nFINAL RESULT:")
print(results)