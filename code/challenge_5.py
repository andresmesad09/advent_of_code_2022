from pathlib import Path
from typing import List
import numpy as np


def display_stacks(stacks):
    print("\nStacks\n")
    for s in stacks:
        print(s, stacks[s])


def load_stacks(stacks, stack_strings, indexes):
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1
    return stacks


def empty_stacks(stacks):
    for stack_num in stacks:
        stack_num[stack_num].clear()
    return stacks


def get_stack_end(stacks):
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer


def first_part(env: str = "test"):
    file_name = "input_5_sample.csv" if env == 'test' else "input_5.csv"
    input_path = Path().cwd() / "data" / file_name
    with input_path.open(mode='r', encoding='utf-8') as file:
        stack_strings, instructions = (i.splitlines()
                                       for i in file.read().strip('\n').split('\n\n'))

    stacks = {int(digit): [] for digit in stack_strings[-1].replace(' ', '')}
    indexes = [index for index, char in enumerate(
        stack_strings[-1]) if char != " "]
    stacks = load_stacks(stacks, stack_strings, indexes)

    for instruction in instructions:
        instruction = instruction.replace('move', "").replace(
            "from", "").replace("to ", "").split()
        instruction = [int(i) for i in instruction]

        crates = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]

        for _ in range(crates):
            crate_removed = stacks[from_stack].pop()
            stacks[to_stack].append(crate_removed)
    return get_stack_end(stacks)


def second_part(env: str = "test"):
    file_name = "input_5_sample.csv" if env == 'test' else "input_5.csv"
    input_path = Path().cwd() / "data" / file_name
    with input_path.open(mode='r', encoding='utf-8') as file:
        stack_strings, instructions = (i.splitlines()
                                       for i in file.read().strip('\n').split('\n\n'))

    stacks = {int(digit): [] for digit in stack_strings[-1].replace(' ', '')}
    indexes = [index for index, char in enumerate(
        stack_strings[-1]) if char != " "]
    stacks = load_stacks(stacks, stack_strings, indexes)

    for instruction in instructions:
        instruction = instruction.replace('move', "").replace(
            "from", "").replace("to ", "").split()
        instruction = [int(i) for i in instruction]

        crates = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]

        crates_to_remove = stacks[from_stack][-crates:]
        stacks[from_stack] = stacks[from_stack][:-crates]

        for crate in crates_to_remove:
            stacks[to_stack].append(crate)
    return get_stack_end(stacks)


if __name__ == '__main__':
    print(first_part("prod"))
    print(second_part("prod"))
