#!/usr/bin/env python3
"""Generate stats.json from templates.json."""
import json
from collections import Counter
from datetime import datetime, timezone


def main():
    with open(".assets/templates.json", "r") as f:
        templates = json.load(f)

    categories = dict(Counter(t.get("category", "unknown") for t in templates))

    tags = sorted(
        {tag for t in templates for tag in t.get("info", {}).get("tags", [])}
    )

    stats = {
        "total": len(templates),
        "categories": categories,
        "tags": tags,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    with open(".assets/stats.json", "w") as f:
        json.dump(stats, f, indent=2)
        f.write("\n")

    print(f"Generated stats: {stats['total']} templates, {len(categories)} categories, {len(tags)} tags")


if __name__ == "__main__":
    main()
