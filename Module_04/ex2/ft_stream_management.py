import sys


def stream_management() -> None:
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    id = sys.stdin.readline().strip()  # strip filters \t and \n

    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    report = sys.stdin.readline().strip().capitalize()

    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {report}\n")

    sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                     "verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    sys.stdout.write("\nThree-channel communication test successful\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    stream_management()
