# https://adventofcode.com/2022/day/3

def get_data_from_file(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.readlines()


def split_rucksacks_for_compartments(rucksacks: list[str]) -> list[tuple[str, str]]:
    
    def get_two_compartments(rucksack: str) -> tuple[str, str]:
        split_index = len(rucksack) // 2
        return rucksack[:split_index], rucksack[split_index:]

    return [get_two_compartments(rucksack) for rucksack in rucksacks]


def get_common_items_in_rucksacks(rucksacks: list[tuple[str, str]]) -> list[str]:

    def find_common_item(first: str, second: str) -> str:
        first, second = list(first), list(second)
        for character in first:
            if character in second:
                return character
        raise ValueError('Cannot find common element.')

    return [find_common_item(*compartments) for compartments in rucksacks]


def count_sum_of_priority(items: list[str]) -> int:
    return sum(ord(item) - 96 if item.islower() else ord(item) - 38 
            for item in items)



def main() -> None:
    contents = get_data_from_file(r'day_3\input.txt')
    contents_divided = split_rucksacks_for_compartments(contents)
    repetetives = get_common_items_in_rucksacks(contents_divided)
    print(f'Sum of priorities: {count_sum_of_priority(repetetives)}.')

if __name__ == '__main__':
    main()