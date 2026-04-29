from pypdf import PdfReader
import os

pdf_folder = "data/pdfs"
output_file = "data/raw_combined.txt"

all_text = ""

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        print(f"Processing: {file}")
        reader = PdfReader(os.path.join(pdf_folder, file))
        
        for page in reader.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(all_text)

print("Done! Raw text saved.")
