# 🎯 VT Templates

> A curated collection of vulnerable targets for security testing, training, and research.

[![Generate Templates](https://github.com/omarkurt/vt-templates/actions/workflows/generate-data.yml/badge.svg)](https://github.com/omarkurt/vt-templates/actions/workflows/generate-data.yml)

---

## 🎯 Targets

| Type | ID | Name | Tech | Tags |
|:----:|-----|------|------|------|
| 🔴 | [vt-2026-23829](cves/vt-2026-23829) | mailpit - Mailpit has an SMTP Header Injection via Regex Bypass | mailpit, web, SMTP | `go` `medium` |
| 🔴 | [vt-2025-55182](cves/vt-2025-55182) | React Server Components - Remote Code Execution | react-server-components, nextjs | `rce` `deserialization` |
| 🔴 | [vt-2025-24963](cves/vt-2025-24963) | Vitest Browser Mode API Exposure (LFI & RCE) (CVE-2025-24963) | vitest | `lfi` `rce` |
| 🔴 | [vt-2026-25512](cves/vt-2026-25512) | Group-Office - Remote Code Execution (OS Command Injection) | group-office, php | `groupoffice` `php` |
| 🔴 | [vt-2026-23829](cves/vt-2026-23829) | mailpit - Mailpit has an SMTP Header Injection via Regex Bypass | mailpit, web, SMTP | `go` `medium` |
| 🔴 | [vt-2026-1207](cves/vt-2026-1207) | Django SQL Injection in RasterField lookup (CVE-2026-1207) | django | `sqli` `django` |
| 🔴 | [vt-2025-64459](cves/vt-2025-64459) | Django - CVE-2025-64459 | django, python, mysql | `injection` `sqli-like` |
| 🔴 | [vt-2025-55182](cves/vt-2025-55182) | React Server Components - Remote Code Execution | react-server-components, nextjs | `rce` `deserialization` |
| 🔴 | [vt-2025-29927](cves/vt-2025-29927) | Next.js Middleware Bypass | web-application | `nextjs` `middleware` |
| 🔴 | [vt-2024-53995](cves/vt-2024-53995) | SickChill Login - Open Redirect | python, media server | `open-redirect` `redirect` |
| 🧪 | [vt-webgoat](labs/vt-webgoat) | WebGoat | java | `owasp` `web` |
| 🧪 | [vt-mutillidae-ii](labs/vt-mutillidae-ii) | OWASP Mutillidae II | php, mysql | `owasp` `web` |
| 🧪 | [vt-juice-shop](labs/vt-juice-shop) | OWASP Juice Shop | nodejs, angular, express, sqlite | `xss` `injection` |
| 🧪 | [vt-dvwa](labs/vt-dvwa) | Damn Vulnerable Web App (DVWA) | mysql, php | `dvwa` `php` |
| 🧪 | [vt-bwapp](labs/vt-bwapp) | bWAPP | php, mysql | `owasp` `web` |
| 📊 | [vt-xbow-104](benchmarks/xbow/vt-xbow-104) | Loan Calculator - Simple | web | `ssti` `default_credentials` |
| 📊 | [vt-xbow-103](benchmarks/xbow/vt-xbow-103) | Trusty Cookie | web | `information_disclosure` `idor` |
| 📊 | [vt-xbow-102](benchmarks/xbow/vt-xbow-102) | Email updates | web | `default_credentials` `business_logic` |
| 📊 | ... | *101 more benchmarks* | | |

> Currently tracking **117** security targets, including **8** CVEs, **5** labs, and **104** benchmarks.