from typing import NamedTuple, List, Set


class Pair(NamedTuple):
    unique_values: List[str]
    display_values: List[str]

    def __iter__(self):
        return iter((self.unique_values, self.display_values))


def load_input() -> List[Pair]:
    pairs: List[Pair] = []
    with open('input.txt') as f:
        for row in f:
            uniques, disp = row.split('|')
            pairs.append(Pair(unique_values=uniques.strip().split(),
                              display_values=disp.strip().split()))

    return pairs


def detect_by_count(values: List[str], num: int) -> List[str]:
    return list(filter(lambda k: len(k) == num, values))


def detect_one(values: List[str]) -> str:
    return detect_by_count(values, 2)[0]


def detect_four(values: List[str]) -> str:
    return detect_by_count(values, 4)[0]


def detect_seven(values: List[str]) -> str:
    return detect_by_count(values, 3)[0]


def detect_eight(values: List[str]) -> str:
    return detect_by_count(values, 7)[0]


def detect_digits_values(values: List[str]) -> List[Set[str]]:
    #     0
    #  1     2
    #     3
    #  4     5
    #     6

    one = set(detect_one(values))

    four = set(detect_four(values))

    seven = set(detect_seven(values))

    seg_25 = seven.intersection(one)

    two_three_or_five = [set(n) for n in detect_by_count(values, 5)]

    three = [comb
             for comb in two_three_or_five
             if comb.intersection(seg_25) == seg_25][0]
    two_three_or_five.remove(three)
    two_or_five = two_three_or_five

    zero_six_or_nine = [set(n) for n in detect_by_count(values, 6)]

    six = [comb
           for comb in zero_six_or_nine
           if comb.intersection(seg_25) != seg_25][0]

    nine = [comb
            for comb in zero_six_or_nine
            if comb.intersection(three) == three][0]

    zero_six_or_nine.remove(six)
    zero_six_or_nine.remove(nine)
    zero = zero_six_or_nine[0]

    five = [comb
            for comb in two_or_five
            if len(comb.intersection(nine)) == 5][0]
    two_or_five.remove(five)
    two = two_or_five[0]

    eight = set(detect_eight(values))

    return [
        zero, one, two, three, four, five, six, seven, eight, nine
    ]


def main():
    pairs = load_input()

    part_1_result = 0
    for values, disp in pairs:
        combinations = detect_digits_values(values)
        part_1_to_count = [combinations[1], combinations[4],
                           combinations[7], combinations[8]]

        for digit in disp:
            if set(digit) in part_1_to_count:
                part_1_result += 1

    print(f"Part 1 result: {part_1_result}")

    part_2_result = 0
    for values, disp in pairs:
        combinations = detect_digits_values(values)
        value = int(
            ''.join([str(combinations.index(set(d))) for d in disp]))
        part_2_result += value

    print(f"Part 2 result: {part_2_result}")


if __name__ == '__main__':
    main()
