# https://adventofcode.com/2022/day/1#part2
import sys


def solution(input_file):
    temporary_result = 0
    first = second = third = -sys.maxsize

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        if not line:
            # Easy way out here would be just collect everything in array and then sort it,
            # But for the sake of a challenge I will do the task without creating new array
            if temporary_result > first:
                third, second, first = second, first, temporary_result
            elif temporary_result > second:
                third, second = second, temporary_result
            elif temporary_result > third:
                third = temporary_result
            temporary_result = 0
            continue

        temporary_result += int(line)

    return first + second + third
