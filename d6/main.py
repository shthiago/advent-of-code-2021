from typing import Dict

REPRODUCING_FISH = 0
NEW_FISH = 8
RESET_FISH = 6

SIMULATED_DAYS = 256
STOP_DAYS = [79, 255]


def load_colony() -> Dict[int, int]:
    with open('input.txt') as f:
        fish_list = [int(i) for i in f.readline().split(',')]

    fishes: Dict[int, int] = {}
    for value in fish_list:
        if value in fishes:
            fishes[value] += 1

        else:
            fishes[value] = 1

    return fishes


def run_day(colony: Dict[int, int]) -> Dict[int, int]:
    new_colony: Dict[int, int] = {}
    new_fishes = 0
    for key, value in colony.items():
        if key == REPRODUCING_FISH:
            new_fishes = value

            if RESET_FISH in new_colony:
                new_colony[RESET_FISH] += value

            else:
                new_colony[RESET_FISH] = value

        else:
            new_key = key - 1
            if new_key in new_colony:
                new_colony[new_key] += value
            else:
                new_colony[new_key] = value

    new_colony[NEW_FISH] = new_fishes

    return new_colony


def main():
    colony = load_colony()
    for i in range(SIMULATED_DAYS):
        colony = run_day(colony)

        if i in STOP_DAYS:
            total_fishes = sum(colony.values())
            print(f"Total fishes after {i+1} days: {total_fishes}")


if __name__ == '__main__':
    main()
