def crisis_handler(file_name: str, mode: str = "r") -> None:
    status = ""

    try:
        with open(file_name, mode) as file:
            content = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - ``{content}''")
            status = "STATUS: Normal operations resumed"
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        status = "STATUS: Crisis handled, system stable"
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        status = "STATUS: Crisis handled, security maintained"
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Unexpected system anomaly detected")
        status = "STATUS: Crisis handled, system stable"
    finally:
        print(status, end="\n\n")


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_data.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
