
 #   1,    2,    3 
# A -> rock, B -> paper, C -> scissors
# X -> lose, Y -> draw, Z -> win





def get_sum_of_points(path: str) -> int:
    round_combinations = {'A X': 0, 'A Y': 3, 'A Z': 6,
                             'B X': 0, 'B Y': 3, 'B Z': 6, 
                             'C X': 0, 'C Y': 3, 'C Z': 6,}

    
    choice = {'A X': 3, 'A Y': 1, 'A Z': 2,
                'B X': 1, 'B Y': 2, 'B Z': 3, 
                'C X': 2, 'C Y': 3, 'C Z': 1,}

    choice_points, round_points = 0, 0

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            round_points +=  round_combinations[line]
            choice_points += choice[line]
            
    return choice_points + round_points


def main() -> None:
    points = get_sum_of_points(r'input.txt')
    print(rf"Points obtained: {points}.")

if __name__ == '__main__':
    main()
