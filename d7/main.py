from typing import List, Tuple


def load_crabs_positions() -> List[int]:
    with open('input.txt') as f:
        return [int(v) for v in f.readline().split(',')]


def calculate_fuel_p1(positions: List[int], target_position: int) -> int:
    return sum([abs(target_position - pos) for pos in positions])


def calculate_fuel_p2(positions: List[int], target_position: int) -> int:
    deltas = [abs(target_position - pos) for pos in positions]
    return sum([sum(range(1, delta+1)) for delta in deltas])


def minimize_fuel(positions: List[int], starting_pos: int, fuel_function) -> Tuple[int, int]:
    current_target_pos = starting_pos
    current_pos_fuel = fuel_function(positions, current_target_pos)
    while True:
        left_pos = current_target_pos - 1 or 0
        right_pos = current_target_pos + 1

        left_fuel = fuel_function(positions, left_pos)
        right_fuel = fuel_function(positions, right_pos)

        if left_fuel > current_pos_fuel < right_fuel:
            return current_target_pos, current_pos_fuel

        if left_fuel < current_pos_fuel:
            current_target_pos = left_pos
            current_pos_fuel = left_fuel

        else:
            current_target_pos = right_pos
            current_pos_fuel = right_fuel


def main():
    crabs = load_crabs_positions()
    starting_pos = int(sum(crabs)/len(crabs))

    pos, fuel = minimize_fuel(crabs, starting_pos, calculate_fuel_p1)
    print(f'Part 1: Align position is {pos}, speding a total {fuel} fuel')

    pos, fuel = minimize_fuel(crabs, starting_pos, calculate_fuel_p2)
    print(f'Part 2: Align position is {pos}, speding a total {fuel} fuel')


if __name__ == '__main__':
    main()
