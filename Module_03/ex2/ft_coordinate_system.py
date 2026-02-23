import sys
import math


def parse_coordinates(coords_str: str) -> tuple[int, int, int]:
    try:
        values = coords_str.split(',')
        pos = tuple([int(v) for v in values])
        if len(pos) != 3:
            raise ValueError("Exactly 3 coordinates required")
        return pos
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def calculate_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> int:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    diff_x = (x2 - x1) ** 2
    diff_y = (y2 - y1) ** 2
    diff_z = (z2 - z1) ** 2

    distance = math.sqrt(diff_x + diff_y + diff_z)

    return distance


def coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)

    spawn = (10, 20, 5)
    print(f"Position created: {spawn}")
    dist1 = calculate_distance(origin, spawn)
    print(f"Distance between {origin} and {spawn}: {dist1:.2f}")

    print()

    if len(sys.argv) > 1:
        input_str = sys.argv[1]
    else:
        input_str = "3,4,0"

    print(f'Parsing coordinates: "{input_str}"')
    parsed_pos = parse_coordinates(input_str)
    print(f"Pased position: {parsed_pos}")

    if parsed_pos is not None:
        dist2 = calculate_distance(origin, parsed_pos)
        print(f"Distance between {origin} "
              f"and {parsed_pos}: {dist2:.1f}")

    input_str_in = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{input_str_in}"')
    parse_coordinates(input_str_in)

    if parsed_pos is not None:
        x, y, z = parsed_pos
        print("\nUnpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system()
