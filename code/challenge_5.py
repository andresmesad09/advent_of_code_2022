from pathlib import Path
from typing import List


def apply_movement(stacks: List, clean_movements: List, qty: int, from_stack: int, to_stack: int):
    for m in clean_movements:
        m_split = m.split(' ')
        qty = int(m_split[1])
        from_stack = int(m_split[3]) - 1
        to_stack = int(m_split[5]) - 1
        stacks[to_stack] =


def first_part(env: str = "test"):
    file_name = "input_5_sample.csv" if env == 'test' else "input_5.csv"
    input_path = Path().cwd() / "data" / file_name
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    # get the index of the empty line minus 1
    position_of_stacks = file_content[file_content.index('\n') - 1]
    number_of_stacks = int(position_of_stacks
                           # split by space to get each item in a list.
                           # Then get the last position
                           .split()[-1]
                           )
    high_of_stacks = file_content.index('\n') - 1
    print(position_of_stacks)
    print(number_of_stacks)
    print(high_of_stacks)

    clean_rows = [line.replace('\n', '')
                  for line in file_content[:high_of_stacks]]
    stacks = []
    for _ in range(number_of_stacks):
        stacks.append([])

    for row, stack_pos in zip(clean_rows, range(len(stacks))):
        for i in range(number_of_stacks):
            item_in_stack = row[i*4:(i*4)+4]
            stacks[stack_pos].append(item_in_stack)

    clean_movements = [move.replace('\n', '')
                       for move in file_content[high_of_stacks+2:]]
    print(stacks)

    apply_movement(stacks, clean_movements, qty, from_stack, to_stack)


if __name__ == '__main__':
    first_part()
