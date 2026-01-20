#!/usr/bin/env python3
"""Update README.md with targets table."""
import json
import re




def format_tags(tags, limit=2):
    """Format tags as backtick-wrapped strings"""
    filtered = [t for t in tags if t not in ['cve', 'xbow', 'ctf', 'training']]
    return ' '.join(f'`{t}`' for t in filtered[:limit])


def main():
    with open('.assets/templates.json', 'r') as f:
        templates = json.load(f)

    cves = [t for t in templates if t.get('category') == 'cves']
    labs = [t for t in templates if t.get('category') == 'labs']
    benchmarks = [t for t in templates if t.get('category') == 'benchmarks']
    total = len(templates)

    # Sort all templates by added_date (newest first). 
    # Use category priority as a tie-breaker for same-day additions.
    priority = {"cves": 3, "labs": 2, "benchmarks": 1}
    templates.sort(key=lambda x: (
        x.get('added_date', '1970-01-01'),
        priority.get(x.get('category', ''), 0),
        x.get('id', '')
    ), reverse=True)

    # Build table
    lines = []
    benchmarks_shown = 0
    total_benchmarks = len(benchmarks)
    
    for t in templates:
        category = t.get('category', '')
        # Only show the first 3 benchmarks encountered (the newest ones)
        if category == 'benchmarks':
            if benchmarks_shown >= 3:
                continue
            benchmarks_shown += 1
        
        tid = t.get('id', '')
        info = t.get('info', {})
        name = info.get('name', '')
        # Clean up benchmark names
        if category == 'benchmarks' and 'XBEN-' in name:
            name = name.split(' ', 1)[-1] if ' ' in name else name
            
        tech = ', '.join(info.get('targets', []))
        tags = format_tags(info.get('tags', []))
        
        icon = "🔴" if category == 'cves' else "🧪" if category == 'labs' else "📊"
        
        # Link path based on category
        link_prefix = "benchmarks/xbow" if category == 'benchmarks' else category
        lines.append(f"| {icon} | [{tid}]({link_prefix}/{tid}) | {name} | {tech} | {tags} |")

    if total_benchmarks > 3:
        lines.append(f"| 📊 | ... | *{total_benchmarks - 3} more benchmarks* | | |")

    table = "| Type | ID | Name | Tech | Tags |\n|:----:|-----|------|------|------|\n" + "\n".join(lines)

    stats_sentence = f"> Currently tracking **{total}** security targets, including **{len(cves)}** CVEs, **{len(labs)}** labs, and **{len(benchmarks)}** benchmarks."
    targets_section = f"""## 🎯 Targets

{table}

{stats_sentence}"""

    with open('README.md', 'r') as f:
        readme = f.read()

    if '## 🎯 Targets' in readme:
        # Replace the entire Targets section until the end or the next major header
        readme = re.sub(
            r'## 🎯 Targets.*',
            targets_section,
            readme,
            flags=re.DOTALL
        )

    with open('README.md', 'w') as f:
        f.write(readme)

    print(f"Updated README: {total} total, {len(cves)} CVEs, {len(labs)} labs, {len(benchmarks)} benchmarks")


if __name__ == '__main__':
    main()
