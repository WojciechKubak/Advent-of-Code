import re
from typing import Final

# https://adventofcode.com/2022/day/5/input 

def load_data(path: str) -> list[str]:
    return open(path).readlines()


def get_stacks(data: list[str], end_line: int) -> list[list[str]]:
    if end_line <= 0:
        raise ValueError('Ending line number must me positive.')

    for i in range(len(stacks := data[:end_line])):
        stacks[i] = stacks[i].replace('[', '').replace(']', ''). \
            replace('    ', '0').replace(' ', '').strip()

    return [re.findall('[A-Z]', ''.join(stack)) for stack in list(zip(*stacks))]


def get_instructions(data: list[str], start_line: int) -> list[list[int]]:
    if start_line <= 0:
        raise ValueError('Starting line number must me positive.')
    
    def extract_digits_from_instruction(instruction: str) -> list[int]:
        return [int(digit) - 1 if i != 0 else int(digit) \
            for i, digit in enumerate(re.findall(r'\d+', instruction))] 

    return [extract_digits_from_instruction(instruction) for instruction in data[start_line:]]


def perform_instructions(stacks: list[list[str]], instructions: list[list[int]], is_new_crate: bool) -> list[str]:
    stacks, step_size = stacks.copy(), 1 if is_new_crate else -1

    for instruction in instructions:
        n, start, end = instruction
        stacks[start], stacks[end] = stacks[start][n:], \
            stacks[start][:n][::step_size] + stacks[end]
    
    return stacks


def show_tops(stacks: list[list[str]], instructions: list[list[int]]) -> None:

    def get_top_of_stack(stacks: list[list[str]]) -> str:
        return ''.join(stack[0] for stack in stacks)

    moved_stacks = perform_instructions(stacks, instructions, False)
    print(f'Top of each stack (old crate): {get_top_of_stack(moved_stacks)} ')
        
    moved_stacks = perform_instructions(stacks, instructions, True)
    print(f'Top of each stack (new crate): {get_top_of_stack(moved_stacks)} ')


def main() -> None:
    STACK_LINE_END: Final[int] = 8
    INSTRUCTIONS_LINE_START: Final[int] = 10

    data = load_data('Supply_Stacks\input.txt')
    stacks, instructions = get_stacks(data, STACK_LINE_END), get_instructions(data, INSTRUCTIONS_LINE_START)

    show_tops(stacks, instructions)

if __name__ == '__main__':
    main()
