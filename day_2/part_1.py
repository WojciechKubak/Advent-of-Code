

# A -> rock, B -> paper, C -> scissors
# X -> rock, Y -> paper, Z -> scissors



def get_sum_of_points(path: str) -> int:
    round_combinations = {'A X': 3, 'A Y': 6, 'A Z': 0,
                             'B X': 0, 'B Y': 3, 'B Z': 6, 
                             'C X': 6, 'C Y': 0, 'C Z': 3,}

    choices = {'X': 1, 'Y': 2, 'Z': 3}

    choice_points, round_points = 0, 0

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            choice_points += choices[line.split()[-1]]
            round_points += round_combinations[line]
            
    return choice_points + round_points


def main() -> None:
    points = get_sum_of_points(r'input.txt')
    print(rf"Points obtained: {points}.")

if __name__ == '__main__':
    main()
