import json 
from pathlib import Path

chunk_summary_path = Path("output/chunk_summaries.json")
final_summary_path = Path("output/final_summary.md")

with open(chunk_summary_path, 'r', encoding='utf-8') as f:
    chunk_summaries = json.load(f)
with open(final_summary_path, 'r', encoding='utf-8') as f:
    final_summary = f.read()

total_chunk_count = len(chunk_summaries)

pages = set()
for chunk in chunk_summaries:
    pages.add(chunk['page_number'])

total_pages_count = len(pages)

empty_chunk_summaries  = 0
for chunk in chunk_summaries:
    if not chunk['summary'].strip():
        empty_chunk_summaries +=1

longest_map_summary_words = 0
for chunk in chunk_summaries:
    word_count = len(chunk['summary'].split())

    if word_count > longest_map_summary_words:
        longest_map_summary_words = word_count

final_summary = final_summary.replace("# Final Summary", "").strip()

final_summary_word_count = len(final_summary.split())

final_summary_under_500 = final_summary_word_count < 500

print("Evaluation Report")
print("-----------------")
print("Total page count:", total_pages_count)
print("Total chunk count:", total_chunk_count)
print("Empty chunk summaries:", empty_chunk_summaries)
print("Longest map-summary word count:", longest_map_summary_words)
print("Final-summary word count:", final_summary_word_count)
print("Final summary under 500 words:", final_summary_under_500)
