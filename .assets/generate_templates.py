#!/usr/bin/env python3
"""Generate templates.json from index.yaml files."""
import json
import yaml
import subprocess
from pathlib import Path


def get_git_date(file_path):
    """Get the first commit date of a file (when it was added)"""
    try:
        result = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--follow', '--format=%aI', '--', str(file_path)],
            capture_output=True, text=True, check=True
        )
        dates = result.stdout.strip().split('\n')
        if dates and dates[-1]:
            return dates[-1]
    except:
        pass
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%aI', '--', str(file_path)],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except:
        return None


def main():
    # Load existing dates to prevent churn
    existing_dates = {}
    try:
        with open('.assets/templates.json', 'r') as f:
            existing_data = json.load(f)
            for t in existing_data:
                if 'id' in t and 'added_date' in t:
                    existing_dates[t['id']] = t['added_date']
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    templates = []

    for index_file in Path('.').rglob('**/index.yaml'):
        if '.git' in str(index_file):
            continue
        try:
            with open(index_file, 'r') as f:
                data = yaml.safe_load(f)
                if data and 'id' in data:
                    parts = str(index_file).split('/')
                    if len(parts) > 1:
                        data['category'] = parts[0]
                    
                    # Use existing date if available, otherwise fetch from git
                    tid = data['id']
                    if tid in existing_dates:
                        data['added_date'] = existing_dates[tid]
                    else:
                        git_date = get_git_date(index_file)
                        if git_date:
                            data['added_date'] = git_date
                            
                    templates.append(data)
        except Exception as e:
            print(f"Error parsing {index_file}: {e}")

    templates.sort(key=lambda x: (x.get('added_date', '1970-01-01'), x.get('id', '')), reverse=True)

    with open('.assets/templates.json', 'w') as f:
        json.dump(templates, f, indent=2)

    print(f"Generated {len(templates)} templates")


if __name__ == '__main__':
    main()
