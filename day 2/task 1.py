# https://adventofcode.com/2022/day/2

def solution(input_file):
    score_map = {'X': 1, 'Y': 2, 'Z': 3}
    draw_map = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    winning_map = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    result = 0

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        enemy_figure, my_figure = line.split(' ')
        result += score_map[my_figure]
        if enemy_figure == draw_map[my_figure]:
            result += 3
        elif enemy_figure == winning_map[my_figure]:
            result += 6

    return result
