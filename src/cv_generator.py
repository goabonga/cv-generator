#!/usr/bin/env python3
"""Generate a clean PDF CV from a Markdown file."""

import argparse
import sys
from pathlib import Path

import markdown
import pikepdf
from weasyprint import HTML

STYLE = """
@page {
    size: A4;
    margin: 1.5cm 2cm;
}

body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #2c3e50;
    max-width: 100%;
}

h1 {
    font-size: 22pt;
    color: #1a252f;
    margin-bottom: 2px;
    border-bottom: none;
}

h1 + p {
    font-size: 11pt;
    color: #555;
    margin-top: 0;
}

h2 {
    font-size: 13pt;
    color: #2980b9;
    border-bottom: 2px solid #2980b9;
    padding-bottom: 3px;
    margin-top: 18px;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

h3 {
    font-size: 11pt;
    color: #1a252f;
    margin-bottom: 2px;
    margin-top: 10px;
}

p {
    margin: 4px 0;
}

em {
    color: #777;
    font-style: italic;
}

a {
    color: #2980b9;
    text-decoration: none;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 12px 0;
}

ul {
    margin: 4px 0;
    padding-left: 20px;
}

ul ul {
    margin: 2px 0;
    padding-left: 18px;
    list-style-type: circle;
}

li {
    margin-bottom: 3px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 9.5pt;
}

th {
    background-color: #f0f4f8;
    text-align: left;
    padding: 6px 10px;
    border-bottom: 2px solid #2980b9;
    color: #2c3e50;
}

td {
    padding: 5px 10px;
    border-bottom: 1px solid #eee;
}

tr:last-child td {
    border-bottom: none;
}

strong {
    color: #1a252f;
}
"""


def md_to_html(md_path: Path) -> str:
    """Convert a Markdown file to a styled HTML document."""
    md_text = md_path.read_text(encoding="utf-8")

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "smarty"],
    )

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <style>{STYLE}</style>
</head>
<body>
{html_body}
</body>
</html>"""


def convert(md_path: Path, output_path: Path, password: str | None = None) -> None:
    """Convert a Markdown file to a styled PDF."""
    html_doc = md_to_html(md_path)

    if password:
        tmp_path = output_path.with_suffix(".tmp.pdf")
        HTML(string=html_doc).write_pdf(str(tmp_path))
        with pikepdf.open(tmp_path) as pdf:
            pdf.save(
                str(output_path),
                encryption=pikepdf.Encryption(
                    user=password,
                    owner=password,
                    R=6,
                ),
            )
        tmp_path.unlink()
        print(f"PDF generated (password protected): {output_path}", file=sys.stderr)
    else:
        HTML(string=html_doc).write_pdf(str(output_path))
        print(f"PDF generated: {output_path}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a PDF CV from a Markdown file")
    parser.add_argument("input", help="Markdown source file")
    parser.add_argument("-o", "--output", default=None, help="Output file (.pdf or .html) — without -o, outputs HTML to stdout")
    parser.add_argument("-p", "--password", default=None, help="Password to protect the PDF")
    args = parser.parse_args()

    md_path = Path(args.input)
    if not md_path.exists():
        print(f"Error: {md_path} not found.", file=sys.stderr)
        sys.exit(1)

    if not args.output:
        print(md_to_html(md_path))
    elif Path(args.output).suffix == ".html":
        Path(args.output).write_text(md_to_html(md_path), encoding="utf-8")
        print(f"HTML generated: {args.output}", file=sys.stderr)
    elif Path(args.output).suffix == ".pdf":
        convert(md_path, Path(args.output), password=args.password)
    else:
        print(f"Error: unsupported format '{Path(args.output).suffix}'. Use .pdf or .html", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
