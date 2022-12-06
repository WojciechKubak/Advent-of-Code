from typing import Final

# https://adventofcode.com/2022/day/6adventofcode

def load_data(path: str) -> str:
    return open(path).readline().strip()


def detect_marker(datastream: str, signal_length: int) -> int:
    if signal_length < 2:
        raise ValueError('Signal size must be at least two.')
    
    for i in range(len(datastream := list(datastream)) - signal_length):
        if len(set(datastream[i: i + signal_length])) == signal_length:
            return i + signal_length
    return 0


def main() -> None:
    SIGNAL_LENGTH: Final[int] = 14
    datastream = load_data(r'input.txt')
    print(f'Marker detected at position: {detect_marker(datastream, SIGNAL_LENGTH)}.')

if __name__ == '__main__':
    main()