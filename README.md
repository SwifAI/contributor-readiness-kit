# Contributor Readiness Kit

Small Python utility for formatting contributor readiness notes.

## Local Development

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e . pytest
python -m pytest
python -m contributor_readiness_kit
```

## Usage

```python
from contributor_readiness_kit import format_readiness_summary

print(format_readiness_summary("ready"))
```
