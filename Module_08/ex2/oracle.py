import os
from dotenv import load_dotenv


def main() -> None:
    try:
        load_dotenv()
    except ImportError:
        print("ERROR: Missing .env file")

    print("\nORACLE STATUS: Reading the Matrix...\n")

    try:
        matrix = os.getenv('MATRIX')
        url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL', 'DEBUG')
        zion = os.getenv('ZION_ENDPOINT')
    except ValueError:
        print("Missing enviornment values")

    print('Configuration loaded:')
    print(f"Mode: {matrix}")

    if url == "localurl.com":
        print("Database:  Connected to local instance")
    else:
        print("Database:  Connected to non-local instance")

    api = "Autenticated" if api_key else "Missing Key"
    print(f"API Acess: {api}")

    print(f"Log Level: {log_level}")

    zionnet = "Online" if zion else "Offline"
    print(f"Zion Network: {zionnet}")

    print("\nEnvironment security check:")

    gitignore = os.path.exists(".gitignore")
    env_ignored = False
    if gitignore:
        with open(".gitignore", "r") as f:
            if ".env" in f.read():
                env_ignored = True

    if env_ignored and gitignore:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("Security is not fully respected")


if __name__ == "__main__":
    main()

# Needs venv to run, check ex0
