# Task 9 — SQL Injection Testing (DVWA)

A controlled SQL Injection learning project using **Damn Vulnerable Web Application (DVWA)** hosted locally with Docker on Kali Linux.

> **Authorization and safety:** This project is intended only for a DVWA instance that you own and run locally. Do not test these techniques against public websites or systems without explicit written authorization. Do not expose DVWA to the public internet.

## Objectives

- Deploy DVWA locally with Docker.
- Compare DVWA SQL Injection behavior at Low and Medium security levels.
- Understand how request methods and input controls affect testing.
- Practice observing application responses in a controlled lab.
- Document findings and recommend secure coding controls.

## Lab environment

| Component | Details |
|---|---|
| Host OS | Kali Linux |
| Container runtime | Docker 28.5.2 (shown in supplied terminal evidence) |
| Target | DVWA (`vulnerables/web-dvwa`) |
| Deployment | Docker container |
| Local URL | `http://127.0.0.1/dvwa/` or the URL configured in the lab |
| Testing tool | Web browser; Burp Suite may be used for request inspection |

## Repository structure

```text
Task-9-SQL-Injection/
├── README.md
├── LICENSE
├── sql_injection_exploit.sh
├── screenshots/
│   ├── docker-version.jpg
│   ├── dvwa-image-pull.jpg
│   ├── dvwa-container-running.jpg
│   ├── dvwa-security-low.jpg
│   ├── sql-injection-low-result.jpg
│   └── sql-injection-baseline.jpg
├── payloads/
│   └── manual-payloads.md
├── reports/
│   └── vulnerability-report.md
├── remediation/
│   ├── python-fix.py
│   └── php-fix.php
└── docs/
    └── installation-guide.md
```

## Lab workflow

1. Start the DVWA container using the local installation guide.
2. Complete DVWA database setup if prompted.
3. Set the DVWA security level to Low and record the baseline behavior.
4. Set the security level to Medium and repeat the authorized lab observation.
5. Save genuine screenshots and record actual results in the vulnerability report.
6. Review the secure Python and PHP examples in `remediation/`.

## Evidence included

The supplied screenshots document:
- Docker version output.
- Successful DVWA image pull.
- DVWA container startup and web server logs.
- DVWA Security page showing Low selected.
- SQL Injection module output for a logical-condition test string.
- Baseline lookup for user ID `1`.

**Evidence limitation:** The screenshots supplied with this project show the Low-level page and test results. No Medium-level screenshot was included in the uploaded files. Add your genuine Medium-level evidence if you want the repository to demonstrate that stage visually; do not label Low screenshots as Medium evidence.

## Remediation summary

- Use parameterized queries / prepared statements.
- Validate identifiers on the server side.
- Avoid concatenating untrusted input into SQL.
- Apply least-privilege database permissions.
- Avoid exposing detailed database errors to users.

See `remediation/python-fix.py` and `remediation/php-fix.php`.

## Disclaimer

DVWA is intentionally vulnerable and is designed for security training. This repository documents a local educational lab; it is not an authorization to test any other system.
