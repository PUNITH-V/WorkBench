from pathlib import Path
from extractor import extract_support_ticket

def main():
    input_path = Path("data")/"sample_ticket.txt"
    output_dir = Path("output")
    output_path = output_dir / 'ticket.json'

    transcript = input_path.read_text(encoding='utf-8')
    ticket = extract_support_ticket(transcript)
    output_dir.mkdir(exist_ok = True)
    json_text = ticket.model_dump_json(indent=2)
    output_path.write_text(json_text, encoding='utf-8')
    print(f"Saved Ticket to {output_path}")

if __name__ == "__main__":
    main()
