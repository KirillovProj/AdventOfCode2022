# https://adventofcode.com/2022/day/4

def solution(input_file):
    result = 0

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        first, second = line.split(',')
        first_start, first_end = [int(i) for i in first.split('-')]
        second_start, second_end = [int(i) for i in second.split('-')]
        if first_start > second_start:
            if second_end >= first_end:
                result += 1
        elif first_start < second_start:
            if first_end >= second_end:
                result += 1
        # If starting points are equal, one of the ranges is guaranteed to be subrange of another range
        else:
            result += 1

    return result
