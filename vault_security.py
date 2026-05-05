def ft_vault_security() -> None:
    file_name = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")

    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(content)
    except FileNotFoundError:
        print("[ALERT] file not found.\n")

    print("SECURE PRESERVATION:")

    try:
        with open(file_name, "a") as file:
            file.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
    except IOError:
        print("[ALERT] Failed to edit the file.")

    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
