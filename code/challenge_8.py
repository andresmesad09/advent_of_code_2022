from pathlib import Path
import numpy as np


def check_side(item, side_list):
    is_visible_on_side = 0
    for e in side_list:
        if item > int(e):
            is_visible_on_side += 1
    if is_visible_on_side == len(side_list):
        return True
    return False


def check_amount_of_trees(item, side_list):
    is_tree_visible = 0
    for e in side_list:
        if item > int(e):
            is_tree_visible += 1
        elif item <= int(e):
            return is_tree_visible + 1
        else:
            break
    return is_tree_visible


def is_visible(item_row, item_col, forest):
    target_item = int(forest[item_row][item_col])
    items_on_top = [forest[i][item_col] for i in range(item_row)]
    items_below = [forest[i][item_col]
                   for i in range(item_row + 1, len(forest))]
    items_left = [forest[item_row][i] for i in range(item_col)]
    items_right = [forest[item_row][i]
                   for i in range(item_col + 1, len(forest[0]))]

    is_visible_top = check_side(target_item, items_on_top)
    is_visible_below = check_side(target_item, items_below)
    is_visible_left = check_side(target_item, items_left)
    is_visible_right = check_side(target_item, items_right)

    if is_visible_top or is_visible_below or is_visible_left or is_visible_right:
        return True
    return False


def check_scene(item_row, item_col, forest):
    target_item = int(forest[item_row][item_col])
    items_on_top = [forest[i][item_col] for i in range(item_row)][::-1]
    items_below = [forest[i][item_col]
                   for i in range(item_row + 1, len(forest))]
    items_left = [forest[item_row][i] for i in range(item_col)][::-1]
    items_right = [forest[item_row][i]
                   for i in range(item_col + 1, len(forest[0]))]

    # print(items_on_top, items_below, items_left, items_right)

    is_visible_top = check_amount_of_trees(target_item, items_on_top)
    is_visible_below = check_amount_of_trees(target_item, items_below)
    is_visible_left = check_amount_of_trees(target_item, items_left)
    is_visible_right = check_amount_of_trees(target_item, items_right)
    visible_trees = is_visible_top * is_visible_below * \
        is_visible_left * is_visible_right
    # print(is_visible_top, is_visible_below,  is_visible_left, is_visible_right)
    return visible_trees


def first_part(env: str = 'dev'):
    file_name = "input_8.csv" if env != 'dev' else "input_8_small.csv"
    input_file = Path().cwd() / "data" / file_name
    with input_file.open(mode='r', encoding='utf-8') as file:
        forest = [l.strip('\n') for l in file.readlines()]

    visible_trees = (len(forest[0]) * 2) + (len(forest[1:-1]) * 2)
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest[0]) - 1):
            if is_visible(row, col, forest):
                visible_trees += 1
    return visible_trees


def second_part(env: str = 'dev'):
    file_name = "input_8.csv" if env != 'dev' else "input_8_small.csv"
    input_file = Path().cwd() / "data" / file_name
    with input_file.open(mode='r', encoding='utf-8') as file:
        forest = [l.strip('\n') for l in file.readlines()]

    scenic_scores = []
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            # print(f"Item: {forest[row][col]}")
            # print(check_scene(row, col, forest))
            scenic_scores.append(check_scene(row, col, forest))
    return max(scenic_scores)


if __name__ == '__main__':
    print(first_part(""))
    print(second_part(""))
