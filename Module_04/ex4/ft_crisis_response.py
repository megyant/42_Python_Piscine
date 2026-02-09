def crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    lost = "lost_archive.txt"
    classified = "classified_vault.txt"
    standard = "standard_archive.txt"

    print(f"CRISIS ALERT: Attempting acess to '{lost}'...")

    try:
        with open(lost, "r") as f_lost:
            print(f"Archive recovered - '{f_lost.read()}'...")
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    print(f"CRISIS ALERT: Attempting acess to '{classified}'...")

    try:
        with open(classified, "r") as f_classified:
            print(f"Archive recovered - '{f_classified.read()}'...")
        print("STATUS: Normal operations resumed\n")
    except (FileNotFoundError, PermissionError):
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    print(f"CRISIS ALERT: Attempting acess to '{standard}'...")
    try:
        with open(standard, "r") as f_standard:
            print(f"Archive recovered - '{f_standard.read()}'")
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
