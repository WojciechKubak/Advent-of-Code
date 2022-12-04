from typing import Final

# # https://adventofcode.com/2022/day/3

def get_data_from_file(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.readlines()


def group_rucksacks(rucksacks: list[str], group_size: int) -> list[list[str]]:
    if group_size <= 0:
        raise ValueError('Group size must me positive.')
    return [rucksacks[i:i + group_size] for i in range(0, len(rucksacks), group_size)]


def get_badges_for_groups(rucksack_groups: list[list[str]]) -> list[str]:

    def find_badge(group: str) -> str:
        first, second, third = group
        for candidate in first:
            if candidate in second and candidate in third:
                return candidate
        raise ValueError('Cannot find common element.') 

    return [find_badge(group) for group in rucksack_groups]


def count_sum_of_priority(items: list[str]) -> int:
    return sum(ord(item) - 96 if item.islower() else ord(item) - 38 
            for item in items)



def main() -> None:
    GROUP_SIZE: Final[int] = 3
    rucksacks = get_data_from_file(r'day_3\input.txt')
    groups = group_rucksacks(rucksacks, GROUP_SIZE)
    badges = get_badges_for_groups(groups)
    print(f'Sum of priorities: {count_sum_of_priority(badges)}.')

if __name__ == '__main__':
    main()