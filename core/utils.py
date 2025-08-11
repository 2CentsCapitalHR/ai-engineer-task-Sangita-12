
import json

def make_report(docs):
    # Aggregate a simple report matching required output format
    # Determine process from majority
    process = 'Unknown'
    if docs:
        process = docs[0]['doc_type'] if docs[0].get('doc_type') else 'Unknown'
    total = len(docs)
    # Example: assume incorporation requires 5 docs; naive
    required = 5 if 'Incorporation' in process else 3
    missing = max(0, required - total)
    report = {
        'process': docs[0]['doc_type'] if docs else 'Unknown',
        'documents_uploaded': total,
        'required_documents': required,
        'missing_documents_count': missing,
        'missing_document': None if missing==0 else 'See checklist',
        'issues_found': []
    }
    for d in docs:
        for it in d['issues']:
            report['issues_found'].append(it)
    return report
