
def detect_process_and_type(text):
    """Very simple keyword-based detector. Returns a dict with process and doc_type."""
    lower = text.lower()
    # Detect doc type
    if 'articles of association' in lower or 'article' in lower and 'association' in lower:
        doc_type = 'Articles of Association'
        process = 'Company Incorporation'
    elif 'memorandum of association' in lower or 'memorandum' in lower:
        doc_type = 'Memorandum of Association'
        process = 'Company Incorporation'
    elif 'shareholder' in lower and 'resolution' in lower:
        doc_type = 'Shareholder Resolution'
        process = 'Company Governance'
    elif 'employment' in lower and 'contract' in lower:
        doc_type = 'Employment Contract'
        process = 'Employment & HR'
    else:
        doc_type = 'Unknown Document Type'
        process = 'Unknown Process'
    return { 'process': process, 'doc_type': doc_type }
