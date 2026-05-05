def ft_ancient_text() -> None:
    file_name = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {file_name}")

    try:
        file = open(file_name, "r")
        content = file.read()

        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(content)

        file.close()
        print("\n")
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    ft_ancient_text()
