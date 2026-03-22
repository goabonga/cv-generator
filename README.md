# md-cv-gen

Generate a clean, professional PDF CV from a Markdown file. Optionally password-protect the output.

## Prerequisites

- Python 3.10+
- [WeasyPrint system dependencies](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

## Installation

```bash
pip install md-cv-gen
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

The output format is determined by the `-o` file extension (`.pdf` or `.html`). Without `-o`, HTML is printed to stdout.

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

The CSS is defined in the `STYLE` variable in `cv_generator.py`. You can modify colors, fonts and spacing directly.

| Element | Property | Default |
|---|---|---|
| Primary color | `color` (h2, links) | `#2980b9` (blue) |
| Text color | `color` (body) | `#2c3e50` (dark grey) |
| Font | `font-family` | Helvetica Neue, Arial |
| Page size | `size` (@page) | A4 |
| Margins | `margin` (@page) | 1.5cm 2cm |

## License

MIT
