"""
CODTECH IT SOLUTIONS - INTERNSHIP PROJECT
Project Name: Reverse Engineering Basics (Static Bytecode & String Analyzer)
Task: Cybersecurity / Python Domain
Intern Name: Morcha Shanmukha Kishor
Intern ID: CIS30
Duration: 4 Weeks
"""

import dis
import inspect
import importlib.util
import re
import os

def extract_strings(filepath: str, min_len: int = 4):
    """Simulates the standard UNIX 'strings' utility on compiled/script files."""
    print(f"\n[*] --- EXTRACTING READABLE STRINGS FROM: {os.path.basename(filepath)} ---")
    try:
        with open(filepath, "rb") as f:
            content = f.read()
        # Find printable ASCII strings of at least min_len characters
        pattern = bytes(f"[A-Za-z0-9_\-+=/.,:;!@#%^&*()<>]{{{min_len},}}", "ascii")
        matches = re.findall(pattern, content)
        
        unique_matches = sorted(list(set(m.decode('ascii', errors='ignore') for m in matches)))
        for s in unique_matches[:25]:  # display top readable strings
            print(f"    [str] {s}")
        if len(unique_matches) > 25:
            print(f"    ... and {len(unique_matches) - 25} more strings found.")
    except Exception as e:
        print(f"[!] Error reading file: {e}")

def disassemble_target(module_path: str):
    """Disassembles Python bytecode into opcodes to understand execution flow."""
    print(f"\n[*] --- BYTECODE DISASSEMBLY ANALYSIS ---")
    try:
        spec = importlib.util.spec_from_file_location("target_mod", module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        # Inspect and disassemble functions inside the module
        functions = [obj for name, obj in inspect.getmembers(mod) if inspect.isfunction(obj)]
        
        for func in functions:
            print(f"\n[+] Disassembly of function '{func.__name__}':")
            print("=" * 60)
            dis.dis(func)
            print("=" * 60)
    except Exception as e:
        print(f"[!] Disassembly error: {e}")

def analyze_constants(module_path: str):
    """Inspects raw code objects, constant pools (co_consts), and variable names."""
    print(f"\n[*] --- CODE OBJECT INSPECTION (CO_CONSTS & CO_NAMES) ---")
    try:
        with open(module_path, "r") as f:
            source = f.read()
        code_obj = compile(source, module_path, "exec")
        
        for const in code_obj.co_consts:
            if inspect.iscode(const):
                print(f"\nFunction: {const.co_name}")
                print(f"  • Constants (co_consts) : {const.co_consts}")
                print(f"  • Variables (co_varnames): {const.co_varnames}")
                print(f"  • Global Names (co_names): {const.co_names}")
    except Exception as e:
        print(f"[!] Inspection error: {e}")

def main():
    print("=" * 65)
    print("   CODTECH IT SOLUTIONS - REVERSE ENGINEERING BASICS TOOL   ")
    print("   Intern: Morcha Shanmukha Kishor | ID: CIS30             ")
    print("=" * 65)

    target_file = "target_program.py"

    while True:
        print(f"Target: {target_file}")
        print("1. Extract Embedded Strings (Static Reconnaissance)")
        print("2. Inspect Constants & Variables Pool (Code Object Analysis)")
        print("3. Disassemble Bytecode to Assembly Instructions (Flow Analysis)")
        print("4. Run Complete Analysis")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            extract_strings(target_file)
        elif choice == '2':
            analyze_constants(target_file)
        elif choice == '3':
            disassemble_target(target_file)
        elif choice == '4':
            extract_strings(target_file)
            analyze_constants(target_file)
            disassemble_target(target_file)
        elif choice == '5':
            print("Exiting tool. Happy analyzing!")
            break
        else:
            print("[!] Invalid option. Select between 1 and 5.\n")
        print("-" * 65 + "\n")

if __name__ == "__main__":
    main()
