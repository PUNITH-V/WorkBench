from pathlib import Path
import json

from loader import load_pdf
from chunks import chunk_pages
from summarizer import summarize_chunks, reduce_summaries


def Map_reduce_pipeline(pdf_path):

    pages = load_pdf(pdf_path)
    chunks = chunk_pages(pages)
    map_results = summarize_chunks(chunks)
    final_summary = reduce_summaries(map_results)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    chunk_summary_path = output_dir / "chunk_summaries.json"

    with open(chunk_summary_path, 'w', encoding = 'utf-8') as f:
        json.dump(map_results, f, ensure_ascii=False, indent =2)

    final_summary_path = output_dir/"final_summary.md"

    with open(final_summary_path, 'w', encoding = 'utf-8') as f:
        f.write("#Final Summary\n\n")
        f.write(final_summary)
    

if __name__ == "__main__":
    pdf_path = Path("data/source.pdf")
    Map_reduce_pipeline(pdf_path)
    print("Pipeline completed. Check the output directory for results.")