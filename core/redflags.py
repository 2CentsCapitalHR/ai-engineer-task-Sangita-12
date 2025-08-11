
import re

def find_red_flags(text, doc_type):
    issues = []
    lower = text.lower()
    # Jurisdiction check
    if 'adgm' not in lower and ('u.a.e' in lower or 'uae' in lower or 'federal court' in lower or 'federal' in lower):
        issues.append({
            'document': doc_type.get('doc_type') if isinstance(doc_type, dict) else doc_type,
            'section': 'Jurisdiction Clause',
            'issue': 'Jurisdiction appears to reference non-ADGM courts or UAE federal courts',
            'severity': 'High',
            'suggestion': 'Update jurisdiction clause to reference ADGM Courts where applicable.'
        })
    # Missing signature check: naive - look for 'Signed' or 'Signature' words
    if 'signature' not in lower and 'signed' not in lower and 'signatory' not in lower:
        issues.append({
            'document': doc_type.get('doc_type') if isinstance(doc_type, dict) else doc_type,
            'section': 'Signatory Section',
            'issue': 'No obvious signatory or signature block found',
            'severity': 'Medium',
            'suggestion': 'Ensure there is a signatory block with names, titles and dates.'
        })
    # Ambiguous language detection (very simple heuristics)
    ambiguous_patterns = [r'\bmay\b', r'\bshould\b', r'\bpossibly\b', r'\bsubject to\b']
    for p in ambiguous_patterns:
        if re.search(p, lower):
            issues.append({
                'document': doc_type.get('doc_type') if isinstance(doc_type, dict) else doc_type,
                'section': 'Ambiguous Language',
                'issue': f'Found potentially non-binding language matching /{p}/',
                'severity': 'Low',
                'suggestion': 'Consider using more binding language where appropriate.'
            })
    return issues
