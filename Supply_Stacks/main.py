import re
from typing import Final

# https://adventofcode.com/2022/day/5/input 

def load_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.readlines()


def get_stacks(data: list[str], to_line: int) -> list[list[str]]:
    for i in range(len(stacks := data[:to_line])):
        stacks[i] = stacks[i].replace('[', '').replace(']', ''). \
            replace('    ', '0').replace(' ', '').strip()

    return [re.findall('[A-Z]', ''.join(stack)) for stack in list(zip(*stacks))]


def get_instructions(data: list[str], from_line: int) -> list[list[str]]:
    
    def extract_digits(instruction: str) -> list[int]:
        return [int(digit) for digit in re.findall(r'\d+', instruction)] 

    return [extract_digits(instruction) for instruction in data[from_line:]]


def perform_instruction(stacks: list[list[str]], instructions: list[list[int]]):

    def move_crate(from_stack: str, to_stack: str) -> tuple[str, str]:
        return stacks[from_stack - 1][n:], stacks[from_stack - 1][:n][::-1] + stacks[to_stack - 1]

    for instruction in instructions:
        n, start, end = instruction
        stacks[start - 1], stacks[end - 1] = move_crate(stacks[start - 1], stacks[end - 1])
    return stacks


def get_top_of_stacks(stacks: list[list[str]]) -> str:
    return ''.join(stack[0] for stack in stacks)


def main() -> None:
    STACK_LINE_END: Final[int] = 8
    INSTRUCTIONS_LINE_START: Final[int] = 10

    data = load_data('input.txt')
    stacks, instructions = get_stacks(data, STACK_LINE_END), get_instructions(data, INSTRUCTIONS_LINE_START)
    
    moved_stacks = perform_instruction(stacks, instructions)
    print(f'Top of each stack: {get_top_of_stacks(moved_stacks)} ')

if __name__ == '__main__':
    main()
