from typing import Final


def load_data(path: str) -> list[str]:
    return [line.strip() for line in open(path).readlines()]


def split_compartments(rucksacks: list[str]) -> list[list[str]]:
    return [[rucksack[:int(len(rucksack) // 2)], rucksack[int(len(rucksack) // 2):]]
        for rucksack in rucksacks]


def divide_into_groups_of_size(rucksacks: list[str], group_size: int) -> list[list[str]]:
    if group_size < 2:
        raise ValueError('Group size must be at least two.')
    return [rucksacks[i:i + group_size] for i in range(0, len(rucksacks), group_size)]


def get_badges_for_groups(rucksack_groups: list[list[str]]) -> list[str]:
    
    def get_badge(groups: list[str]) -> str:
        for candidate in groups[0]:
            if all(candidate in group for group in groups[1:]):
                return candidate
        raise ValueError('Cannot find common element.') 

    return [get_badge(group) for group in rucksack_groups]


def count_sum_of_priority(items: list[str]) -> int:
    return sum(ord(item) - 96 if item.islower() else ord(item) - 38 
            for item in items)


def main() -> None:
    data = load_data(r'input.txt')
    
    rucksacks = split_compartments(data)
    badges = get_badges_for_groups(rucksacks)
    print(f'Sum of priorities in both compartments for each rucksack: {count_sum_of_priority(badges)}.')

    GROUP_SIZE: Final[int] = 3
    rucksacks = divide_into_groups_of_size(data, GROUP_SIZE)
    badges = get_badges_for_groups(rucksacks)
    print(f'Sum of priorities for each three-Elf group: {count_sum_of_priority(badges)}.')



if __name__ == '__main__':
    main()