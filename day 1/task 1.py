# https://adventofcode.com/2022/day/1

def solution(input_file):
    result = temporary_result = 0

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        if not line:
            result = max(result, temporary_result)
            temporary_result = 0
            continue

        temporary_result += int(line)

    return result
