
import gradio as gr
import json, os
from core.parser import parse_docx
from core.classifier import detect_process_and_type
from core.redflags import find_red_flags
from core.annotator import annotate_docx
from core.utils import make_report

def review_documents(files):
    # files: list of temp file paths
    docs = []
    for f in files:
        text = parse_docx(f.name)
        doc_type = detect_process_and_type(text)
        issues = find_red_flags(text, doc_type)
        annotated_path = annotate_docx(f.name, issues)
        docs.append({
            "filename": os.path.basename(f.name),
            "doc_type": doc_type,
            "issues": issues,
            "annotated_file": annotated_path
        })
    report = make_report(docs)
    # save report
    out_json = 'report.json'
    with open(out_json,'w') as fh:
        json.dump(report, fh, indent=2)
    return report, [d['annotated_file'] for d in docs], out_json

title = "ADGM Corporate Agent - Prototype"
desc = "Upload .docx files to run a review. This prototype uses heuristics and placeholders for RAG/LLM."

iface = gr.Interface(
    fn=review_documents,
    inputs=gr.File(file_count="multiple", label="Upload .docx files"),
outputs=[
    gr.JSON(label="Report"),
    gr.File(label="Annotated .docx files", type='filepath', file_types=['.docx'], file_count='multiple'),
    gr.File(label='Report JSON', type='filepath', file_types=['.json'])
],
    title=title,
    description=desc,
    allow_flagging="never",
    examples=None
)

if __name__ == '__main__':
    iface.launch()
