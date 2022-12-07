# https://adventofcode.com/2022/day/6

def solution(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for n in range(len(task_input) - 4):
        # set length will be 4 only when substring has 4 different characters
        if len(set(task_input[n:n + 4])) == 4:
            return n + 4
        n += 1
