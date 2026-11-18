"""Extrait le texte des PDF d'entretiens vers knowledge/uxr/inputs/txt/ (lisible par une IA).
Usage : python3 tools/extract_corpus.py   (nécessite : pip install pypdf)"""
import pathlib, pypdf
root = pathlib.Path(__file__).resolve().parent.parent / "knowledge/uxr/inputs"
out = root / "txt"; out.mkdir(exist_ok=True)
for pdf in sorted(root.glob("*/*.pdf")):
    text = "\n".join((p.extract_text() or "") for p in pypdf.PdfReader(pdf).pages)
    (out / f"{pdf.parent.name}__{pdf.stem}.txt").write_text(text, encoding="utf-8")
print(len(list(out.glob('*.txt'))), "fichiers texte écrits dans", out)
