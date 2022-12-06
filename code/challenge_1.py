from pathlib import Path
from functools import reduce


def list_duplicates_of(seq, item):
    start_at = -1
    locs = [0]
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    locs.append(len(seq))
    return locs


def first_part():
    input_path = Path().cwd() / "data" / "input_1.csv"
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    elfs = {}
    groups = file_content.count('\n') + 1
    position_of_groups = list_duplicates_of(file_content, '\n')
    for i in range(groups):
        first_pos = position_of_groups[i] if i == 0 else position_of_groups[i] + 1
        last_pos = position_of_groups[i+1]
        raw_list = file_content[first_pos:last_pos]
        final_list_for_elf = [int(item.replace('\n', '')) for item in raw_list]
        elfs[i] = sum(final_list_for_elf)

    sorted_dict = {
        k: v for k, v in sorted(
            elfs.items(), key=lambda item: item[1], reverse=True
        )
    }
    top_elf = list(sorted_dict.values())[0]
    return top_elf


def second_part():
    input_path = Path().cwd() / "data" / "input_1.csv"
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()

    elfs = {}
    groups = file_content.count('\n') + 1
    position_of_groups = list_duplicates_of(file_content, '\n')
    for i in range(groups):
        first_pos = position_of_groups[i] if i == 0 else position_of_groups[i] + 1
        last_pos = position_of_groups[i+1]
        raw_list = file_content[first_pos:last_pos]
        final_list_for_elf = [int(item.replace('\n', '')) for item in raw_list]
        elfs[i] = sum(final_list_for_elf)

    sorted_dict = {
        k: v for k, v in sorted(
            elfs.items(), key=lambda item: item[1], reverse=True
        )
    }
    top_three_elfs = list(sorted_dict.values())[:3]
    return top_three_elfs


if __name__ == '__main__':
    top_elf = first_part()
    print(f"Top elf calories: {top_elf}")
    top_three = second_part()
    print(top_three)
    print(sum(top_three))
