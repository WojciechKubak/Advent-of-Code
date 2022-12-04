# https://adventofcode.com/2022/day/4

def load_file(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.readlines()


def extract_ranges(assignment: str) -> tuple[range, range]:
    
    def generate_range(section: str) -> range:
        start, end = section.split('-')
        return range(int(start), int(end) + 1)

    return tuple(generate_range(section) for section in assignment.split(','))


def get_assignments(pairs: list[str]) -> list[tuple[range, range]]:
    return [extract_ranges(pair) for pair in pairs]


def count_fully_contained_ranges(assignments: list[tuple[range, range]]) -> int:
    def is_fully_contained(first_section: range, second_section: range) -> bool:
        return (first_section[0] in second_section and first_section[-1] in second_section) or \
            (second_section[0] in first_section and second_section[-1] in first_section)

    return sum(is_fully_contained(*assignment) for assignment in assignments)


def count_overlapping_ranges(assignments: list[tuple[range, range]]) -> int:
    def is_overlapping(first_section: range, second_section: range) -> bool:
        for element in first_section:
            if element in second_section:
                return True
        return False

    return sum(is_overlapping(*assignment) for assignment in assignments)



def main() -> None:
    sections = load_file(r'Camp Cleanup\input.txt')
    assignments = get_assignments(sections)
    print(f'Fully contained ranges counter: {count_fully_contained_ranges(assignments)}.')
    print(f'Overlapping ranges counter: {count_overlapping_ranges(assignments)}.')

if __name__ == '__main__':
    main()

