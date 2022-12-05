# https://adventofcode.com/2022/day/2#part2

def solution(input_file):
    result = 0
    score_map = {'A': 1, 'B': 2, 'C': 3}
    losing_map = {'A': 'C', 'B': 'A', 'C': 'B'}
    winning_map = {'A': 'B', 'B': 'C', 'C': 'A'}

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        enemy_figure, expected_outcome = line.split(' ')
        # if we need to lose
        if expected_outcome == 'X':
            result += score_map[losing_map[enemy_figure]]
        # if we need to draw
        elif expected_outcome == 'Y':
            result += score_map[enemy_figure] + 3
        # if we need to win
        elif expected_outcome == 'Z':
            result += score_map[winning_map[enemy_figure]] + 6

    return result

print(ord('a'))