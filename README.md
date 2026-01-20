# 🎯 VT Templates

> A curated collection of vulnerable targets for security testing, training, and research.

[![Generate Templates](https://github.com/omarkurt/vt-templates/actions/workflows/generate-data.yml/badge.svg)](https://github.com/omarkurt/vt-templates/actions/workflows/generate-data.yml)

---

## 🎯 Targets

| Type | ID | Name | Tech | Tags |
|:----:|-----|------|------|------|
| 🔴 | [vt-2025-64459](cves/vt-2025-64459) | Django Parameter Injection | django, python | `injection` `sqli-like` |
| 🔴 | [vt-2025-29927](cves/vt-2025-29927) | Next.js Middleware Bypass | web-application | `nextjs` `auth-bypass` |
| 🔴 | [vt-2024-53995](cves/vt-2024-53995) | SickChill Open Redirect | python, media server | `open-redirect` `redirect` |
| 🧪 | [vt-webgoat](labs/vt-webgoat) | WebGoat | java | `owasp` `web` |
| 🧪 | [vt-mutillidae-ii](labs/vt-mutillidae-ii) | OWASP Mutillidae II | php, mysql | `owasp` `web` |
| 🧪 | [vt-juice-shop](labs/vt-juice-shop) | OWASP Juice Shop | nodejs, angular | `owasp` `web` |
| 🧪 | [vt-dvwa](labs/vt-dvwa) | Damn Vulnerable Web App | mysql, php | `dvwa` `php` |
| 🧪 | [vt-bwapp](labs/vt-bwapp) | bWAPP | php, mysql | `owasp` `web` |
| 📊 | [vt-xbow-104](benchmarks/xbow/vt-xbow-104) | Loan Calculator - Simple | web | `ssti` `default_credentials` |
| 📊 | [vt-xbow-103](benchmarks/xbow/vt-xbow-103) | Trusty Cookie | web | `information_disclosure` `idor` |
| 📊 | [vt-xbow-102](benchmarks/xbow/vt-xbow-102) | Email updates | web | `default_credentials` `business_logic` |
| 📊 | ... | *101 more benchmarks* | | |

> 🔴 CVE &nbsp;&nbsp; 🧪 Lab &nbsp;&nbsp; 📊 Benchmark

**Stats:** 112 targets · 3 CVEs · 5 Labs · 104 Benchmarks

---

## 📦 Assets

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