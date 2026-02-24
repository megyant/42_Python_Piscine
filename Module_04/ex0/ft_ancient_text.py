def recover_ancient_text() -> None:
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        filename = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {filename}")

        f = open(filename)
        print("Connection established...")

        print("\nRECOVERED DATA:")
        print(f.read())

        f.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_text()
