
from docx import Document

def parse_docx(path):
    """Return concatenated text of the docx paragraphs."""
    doc = Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text and p.text.strip()!='']
    return '\n\n'.join(paragraphs)
