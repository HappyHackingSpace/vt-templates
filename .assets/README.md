# .assets

Auto-generated data files and the scripts that produce them. Everything here is driven by the `generate-data.yml` GitHub Actions workflow.

## Scripts

### `generate_templates.py`

Walks every `index.yaml` across all category directories (`cves/`, `benchmarks/`, `labs/`, `http/`) and aggregates them into a single `templates.json`. Preserves each template's `added_date` from the previous run to avoid unnecessary git churn, falling back to `git log` for newly added templates.

### `update_readme.py`

Reads `templates.json` and regenerates the **Targets** table in the root `README.md` so it always reflects the current template inventory.

### `generate_stats.py`

Reads `templates.json` and produces `stats.json` — a lightweight summary consumed by [vt-site](https://github.com/HappyHackingSpace/vt-site) for dashboard widgets, badge counts, and the tag cloud. Keeping stats in a separate file avoids parsing the full templates list on every page load.

## Generated Files

### `templates.json`

Complete array of all templates with full metadata (info, tags, PoCs, providers, etc.). Source of truth for the site and any downstream tooling.

### `stats.json`

Compact summary with total count, per-category counts, the full sorted tag list, and a last-updated timestamp. Exists so consumers can fetch aggregate numbers without downloading the full templates payload.
