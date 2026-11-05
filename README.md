
# Secure a Cloud Data Pipeline with Access Control and Masking

## Project Overview

This project demonstrates a secure sales data pipeline using Python and SQLite.

It focuses on protecting sensitive customer information (PII) through secure SQL queries, data masking, and role-based access control.

## Technologies Used

- Python
- SQLite
- SQL
- VS Code

## Project Features

1. Synthetic Customer Dataset
2. SQLite Database Creation
3. Parameterized SQL Queries
4. SQL Injection Prevention
5. Customer Data Masking
6. Role-Based Access Control (RBAC)
7. Security Documentation

## Data Masking

Original customer information is transformed before being displayed to analysts.

Example:

| Data | Original | Masked |
|---|---|---|
| Name | Arun | A*** |
| Email | arun@gmail.com | a***@gmail.com |
| Phone | 9876543210 | ******3210 |

## Access Control

- Admin: Can view original customer information.
- Analyst: Can view masked customer information.
- Guest: Access denied.

Note: This is a local demonstration of role-based access. Production systems require authenticated identities and database/cloud-enforced permissions.

## Security Measures

### Data at Rest
- AES-256 encryption
- Secure database access
- IAM policies
- Secure backups

### Data in Transit
- HTTPS
- TLS encryption
- Secure API communication

These are recommended real-cloud security measures and are documented as production practices, not implemented in this local demo.

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

## Project Structure

- main.py
- sales.db
- security_documentation.txt
- README.md
- screenshots/

## Conclusion

This project demonstrates how to protect sensitive customer data using parameterized SQL queries, data masking, and access control concepts.
