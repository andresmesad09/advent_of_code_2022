"""
    --- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp.
Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap.
To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7,
and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other,
one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration.
In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
"""

from pathlib import Path
from typing import List


def check_pairs(elf_pair: List):
    first_pair = elf_pair[0]
    start_first_pair = int(first_pair.split('-')[0])
    end_first_pair = int(first_pair.split('-')[1])

    second_pair = elf_pair[1]
    start_second_pair = int(second_pair.split('-')[0])
    end_second_pair = int(second_pair.split('-')[1])

    first_pair_tasks = list(range(start_first_pair, end_first_pair+1))
    second_pair_tasks = list(range(start_second_pair, end_second_pair+1))

    check_first_pair = 0
    for i in range(start_first_pair, end_first_pair+1):
        if i in second_pair_tasks:
            check_first_pair += 1

    check_second_pair = 0
    for i in range(start_second_pair, end_second_pair+1):
        if i in first_pair_tasks:
            check_second_pair += 1

    if check_first_pair == len(first_pair_tasks) or check_second_pair == len(second_pair_tasks):
        return True

    return False


def check_pairs_overlap(elf_pair: List):
    first_pair = elf_pair[0]
    start_first_pair = int(first_pair.split('-')[0])
    end_first_pair = int(first_pair.split('-')[1])

    second_pair = elf_pair[1]
    start_second_pair = int(second_pair.split('-')[0])
    end_second_pair = int(second_pair.split('-')[1])

    first_pair_tasks = list(range(start_first_pair, end_first_pair+1))
    second_pair_tasks = list(range(start_second_pair, end_second_pair+1))

    check_first_pair = 0
    for i in range(start_first_pair, end_first_pair+1):
        if i in second_pair_tasks:
            check_first_pair += 1

    check_second_pair = 0
    for i in range(start_second_pair, end_second_pair+1):
        if i in first_pair_tasks:
            check_second_pair += 1

    if check_first_pair > 0 or check_second_pair > 0:
        return True

    return False


def first_part(env: str = "test"):
    file_name = "input_4_small.csv" if env == 'test' else "input_4.csv"
    input_path = Path().cwd() / "data" / file_name
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    clean_content = [raw.replace('\n', '') for raw in file_content]
    sum = 0
    for elf_pair in clean_content:
        if check_pairs(elf_pair.split(',')):
            sum += 1

    return sum


def second_part(env: str = "test"):
    file_name = "input_4_small.csv" if env == 'test' else "input_4.csv"
    input_path = Path().cwd() / "data" / file_name
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    clean_content = [raw.replace('\n', '') for raw in file_content]
    sum = 0
    for elf_pair in clean_content:
        if check_pairs_overlap(elf_pair.split(',')):
            sum += 1

    return sum


if __name__ == '__main__':
    print(second_part("p"))
