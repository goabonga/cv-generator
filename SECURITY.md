# Security Policy

## Supported versions

Security fixes are applied only to the latest released version on the
`main` branch (and the matching PyPI release of `md-cv-gen`).

| Version | Supported |
| --- | --- |
| latest release | ✅ |
| older releases | ❌ |

## Reporting a vulnerability

**Please do not open a public issue.** GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
is the preferred channel:

1. Go to the repository's **Security** tab.
2. Click **Report a vulnerability**.
3. Describe the issue with reproduction steps and a suggested mitigation.

If you cannot use GitHub's form, email **goabonga@pm.me** with the same
information. PGP encryption is available on request.

You can expect an acknowledgement within **3 business days**, a triage
assessment within **10 business days**, and a fix or written mitigation
plan before any public disclosure.

## Scope

`md-cv-gen` reads a Markdown file and renders it to HTML/PDF via
[WeasyPrint](https://weasyprint.org/) and [pikepdf](https://pikepdf.readthedocs.io/).
Security-relevant reports typically concern the handling of untrusted
Markdown input or the PDF encryption path. Vulnerabilities in the
underlying rendering libraries should be reported upstream, but please
let us know so the pinned dependency ranges can be bumped.

Thanks for helping keep the project and its users safe.
