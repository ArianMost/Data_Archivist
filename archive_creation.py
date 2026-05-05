def ft_archive_creation() -> None:
    file_name = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit:", file_name)

    file = open(file_name, "w")

    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")

    entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
    entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee\n"
    file.write(entry1)
    file.write(entry2)
    file.write(entry3)
    file.close()

    try:
        file = open(file_name, "r")
        content = file.read()
        print(content)
        file.close()

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
