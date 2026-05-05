import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    sys.stderr.write("\n")
    sys.stdout.write(
        f"[STANDARD] Archive status "
        f"from {archivist_id}: {status_report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: "
        "Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stderr.write("\n")
    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    ft_stream_management()
