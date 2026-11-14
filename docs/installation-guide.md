DVWA SQL Injection Lab – Installation Guide

1. Overview

This guide explains how to install and configure Damn Vulnerable Web Application (DVWA) using Docker on Kali Linux.

The lab is designed for learning and testing SQL Injection vulnerabilities in a controlled environment.

2. Prerequisites

- Kali Linux
- Docker installed
- Internet connection
- Web browser
- Burp Suite (optional)

3. Verify Docker Installation

Open the Kali Linux terminal and execute:

docker --version

Check whether Docker is running:

sudo systemctl status docker

Start Docker if required:

sudo systemctl start docker

4. Download DVWA Docker Image

Pull the official DVWA lab image:

sudo docker pull vulnerables/web-dvwa

5. Run DVWA Container

Execute:

sudo docker run -d -p 80:80 --name dvwa vulnerables/web-dvwa

Verify the container:

sudo docker ps

6. Access DVWA

Open your browser and visit:

http://127.0.0.1/dvwa/

Default credentials:

- Username: admin
- Password: password

7. Configure DVWA

1. Log in to DVWA.
2. Navigate to DVWA Setup.
3. Select Create / Reset Database.
4. Open Security settings.
5. Select the required security level.
6. Save the configuration.

8. SQL Injection Testing

Navigate to:

Vulnerabilities → SQL Injection

Perform testing at Low and Medium security levels in your local lab.

Use Burp Suite to inspect HTTP requests and responses.

Document the following:

- Input validation behavior
- SQL Injection behavior
- Application responses
- Differences between security levels
- Recommended remediation

9. Stop and Restart DVWA

Stop the container:

sudo docker stop dvwa

Start it again:

sudo docker start dvwa

Remove the container when no longer needed:

sudo docker rm -f dvwa

10. Security Recommendations

- Never expose DVWA to the public internet.
- Run the application only in an isolated lab.
- Do not test unauthorized systems.
- Use parameterized SQL queries in production applications.
- Apply server-side input validation.
- Follow the principle of least privilege.

11. Conclusion

DVWA provides a controlled environment for understanding SQL Injection vulnerabilities, application security testing, and secure coding practices.

This lab is intended strictly for educational and authorized security testing.
