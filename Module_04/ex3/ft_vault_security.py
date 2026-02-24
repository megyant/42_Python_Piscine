def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")

    try:
        classified = "classified_data.txt"
        security = "security_protocols.txt"

        print("Vault connection established with failsafe protocols")

        print("\nSECURE EXTRACTION:")
        with open(classified, "r") as f1:
            print(f1.read())

        print("\nSECURE PRESERVATION:")
        with open(security, "r") as f2:
            print(f2.read())

        print("Vault automatically sealed upon completion")

        print("\nAll vault operations completed with maximum security.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    vault_security()
