def score_analysis():
    import sys
    try:
        if (len(sys.argv) < 2):
            raise ValueError("No scores provided."
                             f" Usage: python3 {sys.argv[0]} "
                             "<score1> <score2> ...")
    except ValueError as e:
        print(e)
        return

    try:
        scores = [int(arg) for arg in sys.argv[1:]]
        print(f"Scores processed: {scores}")
    except ValueError:
        print("All arguments must be integers. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return

    print(f"Total players: {len(sys.argv[1:])}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores)/len(sys.argv[1:])}")
    print(f"High Score: {max(scores)}")
    print(f"Low Score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analysis()
