"""
CODTECH IT SOLUTIONS - REVERSE ENGINEERING BASICS
Sample Target Program (Challenge for Static & Dynamic Analysis)
Intern Name: Morcha Shanmukha Kishor | ID: CIS30
"""

def verify_serial(serial_key: str) -> bool:
    """Simple algorithm to test reverse engineering skills."""
    # Obfuscated / logic-based validation
    if len(serial_key) != 14:
        return False

    prefix = serial_key[:4]
    suffix = serial_key[-4:]
    body = serial_key[4:-4]

    if prefix != "COD-":
        return False
    if suffix != "-2026":
        return False

    # Check checksum of middle characters
    checksum = sum(ord(c) for c in body)
    return checksum == 530  # e.g., 'TECH' -> 84+69+67+72 = 292, or a specific string

def main():
    print("=== SECURE ACCESS PORTAL ===")
    user_key = input("Enter Activation Key: ").strip()
    if verify_serial(user_key):
        print("[+] Access Granted! License validated successfully.")
    else:
        print("[-] Access Denied! Invalid key.")

if __name__ == "__main__":
    main()
