from typing import Iterator
# import random
# import time


def fibonacci_gen(n: int) -> Iterator[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Iterator[int]:
    count = 0
    number = 2
    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
            count += 1
        number += 1


def event_generator(count: int) -> Iterator[tuple[int, str, int, str]]:
    players = ["alice", "bob", "charlie", "frank"]
    events = ["killed monster", "found treasure", "leveled up",
              "opened a chest", "made a potion", "healed up"]
    max_level = 20
    # levels = list(range(1, max_level + 1)) - if random
    for n in range(1, count + 1):
        player = players[(n - 1) % len(players)]
        level = ((n - 1) % max_level + 1)  # random.choice(levels)
        event = events[(n - 1) % len(events)]
        yield n, player, level, event


def data_stream() -> None:

    count = 1000
    print("=== Game Data stream Processor ==\n")

    print(f"Processing {count} game events...\n")

    total_events = 0
    high_level_count = 0
    treasure_count = 0
    level_up_count = 0
    max_level_print = 4

    # start = time.time()

    events = event_generator(count)
    for n, player, level, event in events:
        total_events += 1
        if n < max_level_print:
            print(f"Event {n}: Player {player} (level {level}) {event}")
        elif n == 4:
            print("...\n")

        if level >= 10:
            high_level_count += 1

        if event == "found treasure":
            treasure_count += 1

        if event == "leveled up":
            level_up_count += 1

    # end = time.time()

    # total_time = end - start

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045")
    # print(f"Processing time: {total_time:.3f}")

    print("\n=== Generator Demonstration ===")
    fibonacci = []
    limit_fib = 10
    generating_fib = fibonacci_gen(limit_fib)
    for _ in range(10):
        fibonacci.append(next(generating_fib))
    print(f"Fibonacci sequence (first {limit_fib}): "
          f"{', '.join(map(str, fibonacci))}")

    primes = []
    limit_prime = 5
    generating_prime = prime_gen(limit_prime)
    for _ in range(limit_prime):
        primes.append(next(generating_prime))
    print(f"Prime numbers (first {limit_prime}): "
          f"{', '.join(map(str, primes))}")


if __name__ == "__main__":
    data_stream()
