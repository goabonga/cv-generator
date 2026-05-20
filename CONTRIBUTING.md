# Contributing to md-cv-gen

Thanks for taking the time to contribute. This document is the short
version of how to propose a change and what the project expects in return.

## Code of Conduct

Participation in this project is governed by the
[Code of Conduct](CODE_OF_CONDUCT.md). By contributing you agree to abide
by its terms.

## Repository layout

```
.
├── src/cv_generator.py    # the CLI module (entry point: cv_generator:main)
├── scripts/               # SPDX header helper
├── pyproject.toml         # uv project + hatchling build
└── multicz.toml           # Conventional Commits releasing
```

`src/cv_generator.py` is a single module shipped at the wheel root as the
importable `cv_generator` package; the `md-cv-gen` console script calls
`cv_generator:main`.

## Development setup

```bash
git clone https://github.com/goabonga/cv-generator.git
cd cv-generator
uv sync
uv run pre-commit install
```

WeasyPrint relies on native libraries (Pango, cairo, …). Install the
[WeasyPrint system dependencies](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)
before generating PDFs.

## Running it locally

```bash
uv run md-cv-gen examples/cv.md -o cv.pdf
```

## Lint and headers

```bash
uv run ruff check .
uv run ruff format --check .
python scripts/add_license_header.py --path . --types py --check
```

## Packaging

```bash
uv build
# inspect dist/*.whl - cv_generator.py must sit at the wheel root
```

## Commit messages

Commit messages MUST follow
[Conventional Commits](https://www.conventionalcommits.org/). They drive
the version bump and CHANGELOG computed by
[multicz](https://github.com/goabonga/multicz).

| Type | Effect on version | Use it for |
| --- | --- | --- |
| `feat` | minor | new capability |
| `fix` | patch | bug fix |
| `perf` | patch | performance improvement |
| `refactor`, `docs`, `test`, `chore`, `ci`, `build`, `style` | none | maintenance |
| `feat!` / `BREAKING CHANGE:` | major | incompatible change |

Only changes under the tracked paths (`src/`, `pyproject.toml`) trigger a
release. Do not append `Co-Authored-By` trailers.

## Releasing

Releases are automated: on every push to `main`, the workflow runs
`multicz bump --commit --tag --push` and publishes `md-cv-gen` to PyPI.
Maintainers do not bump versions or edit the changelog by hand.

## Reporting bugs and asking for features

Please open a GitHub issue. For security-sensitive reports, follow
[SECURITY.md](SECURITY.md) instead of the public tracker.
