import docx
import re

# Section headers we expect to find in the resume
SECTION_HEADERS = [
    "Profile Summary",
    "Education",
    "Technical Skills",
    "Soft Skills",
    "Experience",
    "Projects",
    "Certifications"
]

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def split_into_sections(text):
    sections = {}
    pattern = "|".join([re.escape(h) for h in SECTION_HEADERS])
    matches = list(re.finditer(pattern, text))

    for i, match in enumerate(matches):
        header = match.group()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[header] = text[start:end].strip()

    return sections

if __name__ == "__main__":
    file_path = "data/resume.docx"
    raw_text = extract_text_from_docx(file_path)
    sections = split_into_sections(raw_text)

    for header, content in sections.items():
        print(f"--- {header} ---")
        print(content)
        print()