This tool was developed as part of my internship in the Cybersecurity & Ethical Hacking domain.
The task was to create a basic file integrity monitor using Python and hashing techniques.
It gave me practical exposure to real-world applications of cryptographic hash functions and file forensics.

# FILE-INTEGRITY-CHECKER

COMPANY: CODETECH IT SOLUTIONS
NAME:Ahammed Falah F M
Intern ID:CT04DZ2299
DOMAIN: Cyber Security And Ethical Hacking 
DURATION: 4 WEEKS 
MENTOR: NEELA SANTOSH

# 🛡️ File Integrity Checker

A simple and reliable Python tool to **monitor changes in files** by calculating and verifying hash values using various cryptographic algorithms.

This tool helps ensure **file integrity** by detecting tampering, corruption, or unintended modifications in any file. It uses Python’s built-in `hashlib` and supports automatic detection of the hashing algorithm during verification.

---

## 🚀 Features

- 🔐 Supports multiple hash algorithms: `sha256` (default), `sha512`, `sha1`, `md5`
- 💾 Saves hash values with the algorithm type (e.g., `sha256 abcd123...`)
- ✅ Verifies file integrity by comparing current hash with saved hash
- 🔄 Automatically detects the correct algorithm during verification
- ⚡ No external dependencies (pure Python)

---


```bash
python file_integrity_checker.py sample.txt --algorithm sha256
