# REVERSE ENGINEERING BASICS

A Python-based educational reverse engineering and bytecode analysis tool developed for the **CODTECH IT SOLUTIONS** Internship program.

---

## 📌 Intern & Project Details
* **INTERN ID:** CIS30
* **FULL NAME:** Morcha Shanmukha Kishor
* **NO. OF WEEKS:** 4 Weeks
* **PROJECT NAME:** REVERSE ENGINEERING BASICS
* **PROJECT SCOPE:** 
  The primary objective of this project is to explore the fundamental principles of static and dynamic program analysis. It demonstrates how compiled routines and bytecodes are inspected, how embedded strings and symbol tables are extracted, and how execution flow and disassembly instructions (`LOAD_CONST`, `COMPARE_OP`, `JUMP_IF_FALSE`) are reconstructed to evaluate software behavior and security architectures.

---

## 🚀 Features
- **Static String Extraction:** Scans raw binary/source artifacts to discover hardcoded strings, endpoints, and credentials (analogous to the UNIX `strings` utility).
- **Constant & Variable Pool Inspection:** Audits code objects (`co_consts`, `co_varnames`, `co_names`) to inspect data structures without running unknown routines.
- **Bytecode Disassembly Engine:** Translates Python high-level instructions into low-level virtual machine opcodes using the `dis` engine.
- **Sample Target Program (`target_program.py`):** Includes a practice verification routine to demonstrate real-world analysis workflows.

---

## 📁 Repository Structure
```
Reverse_Engineering_Basics/
│
├── target_program.py         # Sample program for analysis
├── re_analyzer.py            # Static disassembly & reverse engineering tool
├── README.md                 # Complete documentation conforming to CODTECH specifications
└── screenshots/              # Execution logs & sample output
    └── cli_output_sample.txt
```

---

## 💻 How to Run the Project

### Prerequisites:
Python 3.x installed (Uses built-in modules `dis`, `inspect`, `importlib`, `re`, `os`).

### Execution:
1. Run the Reverse Engineering Analyzer:
```bash
python re_analyzer.py
```
2. Select options:
   - **Option 1:** Extract readable strings and hardcoded keys.
   - **Option 2:** Inspect internal constants pool (`co_consts`).
   - **Option 3:** View complete opcode disassembly.
   - **Option 4:** Run a full automated audit.

---

## 📊 Sample Output
```text
Function: verify_serial
  • Constants (co_consts) : (None, 14, 4, -4, 'COD-', '-2026', 530)
  • Variables (co_varnames): ('serial_key', 'prefix', 'suffix', 'body', 'checksum')
```
