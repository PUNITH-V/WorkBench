from pathlib import Path
from pypdf import PdfReader

def load_pdf(pdf_path: Path):
    reader = PdfReader(pdf_path)
    pages = []

    for page_number, page in enumerate(reader.pages,start=1):
        text = page.extract_text() or ""

        pages.append({
            "page_number" : page_number,
            "text": text,
            "source": pdf_path.name
        })
    return pages         
