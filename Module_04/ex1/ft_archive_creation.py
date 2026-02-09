def archive_creation():
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

        filename = "new_discovery.txt"
        print(f"Initializing new storage unit: {filename}")

        with open(filename, "w") as f:
            f.write("[ENTRY 001] New quantum algorithm discovered\n")
            f.write("[ENTRY 002] Efficiency increased by 347%\n")
            f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")
        f = open(filename)
        print(f.read())
        f.close()

        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except FileNotFoundError:
        print("ERROR: Archive not found.")


if __name__ == "__main__":
    archive_creation()
