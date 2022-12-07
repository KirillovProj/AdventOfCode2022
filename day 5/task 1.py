# https://adventofcode.com/2022/day/5


# The worst part of this task is formatting input to match some structure that program can work with.
def solution(input_file):
    stacks = [[], [], [], [], [], [], [], [], []]

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n')[7::-1]:
        stack_index = 0
        for char in line[1::4]:
            if char == ' ':
                stack_index += 1
                continue
            stacks[stack_index].append(char)
            stack_index += 1

    for line in task_input.split('\n')[10:]:
        split_line = line.split(' ')
        move_number = int(split_line[1])
        source = int(split_line[3]) - 1  # -1 is needed to match indexes of stacks list
        target = int(split_line[5]) - 1

        for i in range(move_number):
            stacks[target].append(stacks[source].pop())

    return [stack[-1] for stack in stacks]
