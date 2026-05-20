# md-cv-gen

[![CI](https://github.com/goabonga/cv-generator/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/goabonga/cv-generator/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/md-cv-gen.svg)](https://pypi.org/project/md-cv-gen/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/goabonga/cv-generator/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

Generate a clean, professional PDF CV from a Markdown file. Optionally
password-protect the output.

## Features

- **Markdown in, PDF out** — write your CV in plain Markdown, render it to a
  print-ready A4 PDF (or HTML).
- **Sensible typographic defaults** — an embedded stylesheet handles colors,
  spacing and page layout; tweak it in one place.
- **Password protection** — optionally encrypt the generated PDF.
- **Single dependency-light CLI** — one command, no config files.

## Prerequisites

- Python 3.10+
- [WeasyPrint system dependencies](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)
  (Pango, cairo, …) for PDF output.

## Installation

```bash
pip install md-cv-gen
```

Or run it without installing, using [uv](https://github.com/astral-sh/uv):

```bash
uvx md-cv-gen cv.md -o cv.pdf
```

## Usage

```bash
# Output HTML to stdout
md-cv-gen cv.md

# Generate an HTML file
md-cv-gen cv.md -o cv.html

# Generate a PDF
md-cv-gen cv.md -o cv.pdf

# Generate a password-protected PDF
md-cv-gen cv.md -o cv.pdf -p "secret"
```

The output format is determined by the `-o` file extension (`.pdf` or
`.html`). Without `-o`, HTML is printed to stdout.

## Markdown structure

```markdown
# First Last
**Job title** | City, Country
email | phone | links

---

## Section                         <!-- h2 sections -->

### Role - Company                 <!-- h3 subsections -->
*Dates | Location*                 <!-- dates in italic -->

- Achievements as bullet points
```

## Style customization

The CSS is defined in the `STYLE` variable in `src/cv_generator.py`. You can
modify colors, fonts and spacing directly.

| Element | Property | Default |
|---|---|---|
| Primary color | `color` (h2, links) | `#2980b9` (blue) |
| Text color | `color` (body) | `#2c3e50` (dark grey) |
| Font | `font-family` | Helvetica Neue, Arial |
| Page size | `size` (@page) | A4 |
| Margins | `margin` (@page) | 1.5cm 2cm |

## Development

```bash
git clone https://github.com/goabonga/cv-generator.git
cd cv-generator
uv sync
uv run pre-commit install
uv run ruff check .
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow, commit
conventions and release process.

## License

[MIT](LICENSE) © Chris
