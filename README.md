
# ADGM Corporate Agent - Prototype

This is a runnable prototype for the "ADGM-Compliant Corporate Agent with Document Intelligence" task.
It provides a Gradio UI to upload `.docx` files, performs simple classification, checklist verification,
red-flag detection, annotates the `.docx` (inline annotations), and produces a JSON report.

## What's included
- `app.py` — Gradio app to upload files and run the review pipeline.
- `core/` — core modules:
  - `parser.py` — extracts text from `.docx`
  - `classifier.py` — guesses document type and process
  - `redflags.py` — heuristic red-flag detectors
  - `annotator.py` — writes annotated `.docx`
  - `rag.py` — RAG indexer placeholder (add embeddings/LLM)
  - `utils.py` — helper functions
- `data_sources/` — place ADGM reference docs here (PDFs, DOCX)
- `sample_before.docx` — example input document
- `example_report.json` — sample output JSON report

## How to run
1. Create virtualenv and install dependencies:
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
2. (Optional) Add ADGM reference docs to `data_sources/` for RAG.
3. Run the app:
```
python app.py
```
4. Open the Gradio link (printed in console) and upload `.docx` files.

## Notes & Next steps
- LLM integration (OpenAI/Gemini/etc.) is left as configurable in `core/rag.py` and `core/classifier.py`.
- The annotator currently inserts visible inline comments next to flagged paragraphs. If you need Word native comment objects,
  that can be implemented with `python-docx` advanced APIs or `docx` comment XML manipulation.
- This is a prototype intended for the take-home assignment. Review code and adapt prompts/citations before claiming legal compliance.
