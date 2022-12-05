# https://adventofcode.com/2022/day/3

def solution(input_file):
    result = 0
    uppercase_offset = 38
    lowercase_offset = 96

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for line in task_input.split('\n'):
        # Splitting given string in halves and transforming it to set for easy intersection finding
        left, right = set(line[:len(line)//2]), set(line[len(line)//2:])
        # Since we know that there is one and only one common element, we can safely
        # pop random item from intersection - it will always be right
        common = left.intersection(right).pop()
        if common.isupper():
            result += ord(common) - uppercase_offset
        elif common.islower():
            result += ord(common) - lowercase_offset

    return result
