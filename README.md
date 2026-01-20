# 🎯 VT Templates

> A curated collection of vulnerable targets for security testing, training, and research.

[![Generate Templates](https://github.com/omarkurt/vt-templates/actions/workflows/generate-data.yml/badge.svg)](https://github.com/omarkurt/vt-templates/actions/workflows/generate-data.yml)

---

## � Overview

| Metric | Count |
|--------|-------|
| **Total Templates** | 112 |
| 🔴 CVEs | 3 |
| 🧪 Labs | 5 |
| 📊 Benchmarks | 104 |

---

## 🎯 Targets

| Type | ID | Name | Tech |
|:----:|-----|------|------|
| 🔴 | [vt-2025-64459](cves/vt-2025-64459) | Django Parameter Injection | django, python |
| 🔴 | [vt-2025-29927](cves/vt-2025-29927) | Next.js Middleware Bypass | web-application |
| 🔴 | [vt-2024-53995](cves/vt-2024-53995) | SickChill Open Redirect | python, media server |
| 🧪 | [vt-webgoat](labs/vt-webgoat) | WebGoat | java |
| 🧪 | [vt-mutillidae-ii](labs/vt-mutillidae-ii) | OWASP Mutillidae II | php, mysql |
| 🧪 | [vt-juice-shop](labs/vt-juice-shop) | OWASP Juice Shop | nodejs, angular |
| 🧪 | [vt-dvwa](labs/vt-dvwa) | Damn Vulnerable Web App | mysql, php |
| 🧪 | [vt-bwapp](labs/vt-bwapp) | bWAPP | php, mysql |
| 📊 | [vt-xbow-104](benchmarks/xbow/vt-xbow-104) | Loan Calculator - Simple | python, flask |
| 📊 | [vt-xbow-103](benchmarks/xbow/vt-xbow-103) | Trusty Cookie | python, flask |
| 📊 | [vt-xbow-102](benchmarks/xbow/vt-xbow-102) | Email updates | python, flask |
| 📊 | ... | *104 more benchmarks* | |

> 🔴 CVE &nbsp;&nbsp; 🧪 Lab &nbsp;&nbsp; 📊 Benchmark

---

## 🏷️ Vulnerability Tags

<table>
<tr><td>

**Injection**
- `sqli` `blind_sqli` `nosqli`
- `command_injection` `ssti`
- `xxe` `lfi` `path_traversal`

**Authentication**
- `auth-bypass` `broken-auth`
- `jwt` `privilege_escalation`
- `default_credentials` `brute_force`

</td><td>

**Client-Side**
- `xss` `open-redirect`
- `ssrf` `smuggling_desync`

**Other**
- `idor` `race_condition`
- `arbitrary_file_upload`
- `insecure_deserialization`
- `information_disclosure`
- `business_logic` `crypto`

</td></tr>
</table>

---

## � Assets

Template data is auto-generated via GitHub Actions and available at:

```
assets/templates.json
```

### API Usage

```bash
# Get all template IDs
curl -s https://raw.githubusercontent.com/omarkurt/vt-templates/main/assets/templates.json | jq '.[].id'

# Get CVEs only
curl -s https://raw.githubusercontent.com/omarkurt/vt-templates/main/assets/templates.json | jq '[.[] | select(.category == "cves")]'

# Get templates by target
curl -s https://raw.githubusercontent.com/omarkurt/vt-templates/main/assets/templates.json | jq '[.[] | select(.info.targets[]? == "python")]'
```

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/omarkurt/vt-templates.git && cd vt-templates

# Run a CVE environment
cd cves/vt-2025-29927 && docker compose up -d

# Run a lab
cd labs/vt-dvwa && docker compose up -d
```

---

## 📁 Structure

```
vt-templates/
├── assets/templates.json    # Auto-generated catalog
├── cves/vt-{id}/           # CVE reproductions
├── labs/vt-{name}/         # Training labs  
├── benchmarks/vt-xbow-*/   # Security benchmarks
└── .github/workflows/      # CI/CD
```

---

<div align="center">

**[vulnerabletarget.com](https://vulnerabletarget.com)** · [@omarkurt](https://github.com/omarkurt)

</div>