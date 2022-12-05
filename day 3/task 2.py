# https://adventofcode.com/2022/day/3#part2

# I can use itertools grouper(), but for the sake of a challenge I'll implement my own version of it, kinda.
def group_iterable(n, iterable):
    start, stop = 0, n
    while stop <= len(iterable):
        yield iterable[start:stop]
        start += n
        stop += n


def solution(input_file):
    result = 0
    uppercase_offset = 38
    lowercase_offset = 96

    with open(input_file, 'r', encoding='utf-8') as file:
        task_input = file.read()

    for group in group_iterable(3, task_input.split('\n')):
        first, second, third = set(group[0]), set(group[1]), set(group[2])
        # We can do it since we know that there is always one and only one common item
        common = first.intersection(second.intersection(third)).pop()
        if common.isupper():
            result += ord(common) - uppercase_offset
        elif common.islower():
            result += ord(common) - lowercase_offset

    return result
