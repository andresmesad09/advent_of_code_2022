"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions,
and so a few items now need to be rearranged.

Each rucksack has two large compartments.
All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors.
Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line.
A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment,
while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr,
while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.

The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""

from pathlib import Path
import string

LETTERS = string.ascii_lowercase + string.ascii_uppercase


def get_priority(item):
    return LETTERS.index(item) + 1


def first_part():
    input_path = Path().cwd() / "data" / "input_3.csv"
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    rucksacks = [elf.replace('\n', '') for elf in file_content]
    sum = 0
    for r in rucksacks:
        len_items = len(r)
        compartiment_1 = set(r[0:len_items // 2])
        compartiment_2 = set(r[len_items // 2:])
        duplicated_item = list(compartiment_1.intersection(compartiment_2))[0]
        sum += get_priority(item=duplicated_item)

    return sum


def second_part():
    input_path = Path().cwd() / "data" / "input_3.csv"
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    rucksacks = [elf.replace('\n', '') for elf in file_content]
    sum_priorities = 0
    for i in range(0, len(rucksacks), 3):
        team = rucksacks[i:i+3]
        elf_items_1 = set(team[0])
        elf_items_2 = set(team[1])
        elf_items_3 = set(team[2])
        badge = list(elf_items_1.intersection(
            elf_items_2).intersection(elf_items_3))[0]
        priority_team = get_priority(item=badge)
        sum_priorities += priority_team

    return sum_priorities


if __name__ == '__main__':
    answer_1 = first_part()
    print(answer_1)
    answer_2 = second_part()
    print(answer_2)
