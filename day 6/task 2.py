# https://adventofcode.com/2022/day/6#part2

def solution(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for n in range(len(task_input) - 14):
        # set length will be 4 only when substring has 4 different characters
        if len(set(task_input[n:n + 14])) == 14:
            return n + 14
        n += 1

print(solution('input.txt'))