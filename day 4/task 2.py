# https://adventofcode.com/2022/day/4#part2

def solution(input_file):
    result = 0

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        first, second = line.split(',')
        first_start, first_end = [int(i) for i in first.split('-')]
        second_start, second_end = [int(i) for i in second.split('-')]
        first_range = set(range(first_start, first_end+1))
        second_range = set(range(second_start, second_end+1))
        if first_range.intersection(second_range):
            result += 1

    return result


print(solution('input.txt'))