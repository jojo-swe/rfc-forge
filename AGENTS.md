# AGENTS.md

## Purpose

RFC Forge renders a consistent Markdown RFC from required metadata.
The public API is `rfc_forge.render_rfc(title, owner, problem, decision) -> str`.
An empty `title`, `owner`, `problem`, or `decision` raises `ValueError("all fields are required")`.

## Layout

- `src/rfc_forge/core.py` — `render_rfc`
- `src/rfc_forge/__init__.py` — exports `render_rfc` (`__all__`)
- `tests/test_core.py` — pytest checks for the Decision section and missing fields
- `pyproject.toml` — package metadata (`rfc-forge`), hatchling build, dev extras
- `.github/workflows/ci.yml` — `ruff check .` and `pytest` on Python 3.11 and 3.12

## Build and test

Requires Python 3.11 or newer.

```bash
pip install -e ".[dev]"
ruff check .
pytest
```

Dev extras are `pytest>=8` and `ruff>=0.5`. Hatchling builds the wheel from `src/rfc_forge`.

## Conventions

- Keep the public surface to `render_rfc`.
- Arguments are positional strings: `title`, `owner`, `problem`, `decision`.
- Output is Markdown: an H1 title, `**Owner:**`, `## Problem`, and `## Decision`.
- There is no extra Ruff or pytest config. CI uses each tool's defaults.
- License is Apache-2.0, declared in `pyproject.toml`.

## Privacy / Integritet

Inga privata uppgifter får committas, och de får inte stå i PR-text (titel, beskrivning eller kommentar). Det gäller:

- personlig e-post — använd GitHubs noreply-adress i stället
- telefonnummer
- postadresser och hemadresser
- namn på privatpersoner
- interna IP-adresser
- Tailscale-värdnamn
- användarnamn i sökvägar
- nycklar och tokens
- innehåll i `.env`

Kör `pre-commit install` lokalt så att gitleaks granskar staged ändringar mot `.gitleaks.toml` före varje commit.

Agenter som hittar privata uppgifter maskerar dem med platshållare och skriver aldrig ut själva värdet i en commit, en pull request eller en logg. Använd till exempel `<email>`, `<user>`, `192.168.x.y`, `10.x.y.z`, `100.64.0.x` och `<host>.ts.net`.
