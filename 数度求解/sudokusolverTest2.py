import copy

# map_left_top = [
#     [0, 0, 1, 0, 2, 0, 3, 0, 7],
#     [0, 4, 0, 0, 0, 7, 6, 2, 0],
#     [0, 0, 0, 0, 0, 0, 9, 0, 0],
#     [0, 0, 4, 5, 1, 9, 0, 7, 0],
#     [0, 0, 0, 4, 0, 3, 2, 9, 0],
#     [0, 6, 0, 0, 0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0, 5, 0, 0, 0],
#     [0, 7, 0, 0, 9, 0, 0, 6, 0],
#     [0, 0, 6, 8, 0, 0, 7, 0, 2],
# ]
map_left_top = [
    [0, 0, 1, 0, 2, 0, 3, 0, 7],
    [0, 4, 0, 0, 0, 7, 6, 2, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 4, 5, 1, 9, 0, 7, 0],
    [0, 0, 0, 4, 0, 3, 2, 9, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 5, 4, 8, 9],
    [0, 7, 0, 0, 9, 0, 5, 6, 3],
    [0, 0, 6, 8, 0, 0, 7, 1, 2],
]

map_right_top = [
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 7, 0, 3, 0, 0, 0],
    [7, 0, 0, 1, 5, 0, 0, 0, 6],
    [0, 1, 0, 0, 0, 9, 8, 0, 0],
    [2, 0, 0, 5, 0, 0, 0, 6, 0],
    [0, 0, 0, 6, 1, 0, 0, 0, 0],
    [5, 0, 0, 4, 3, 0, 0, 0, 9],
    [0, 7, 0, 9, 2, 6, 3, 4, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 1]
]

# map_right_top = [
#     [0, 9, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 2, 7, 0, 3, 0, 0, 0],
#     [7, 0, 0, 1, 5, 0, 0, 0, 6],
#     [0, 1, 0, 0, 0, 9, 8, 0, 0],
#     [2, 0, 0, 5, 0, 0, 0, 6, 0],
#     [0, 0, 0, 6, 1, 0, 0, 0, 0],
#     [5, 2, 6, 4, 3, 0, 0, 0, 9],
#     [8, 7, 1, 9, 2, 6, 3, 4, 0],
#     [9, 3, 4, 0, 0, 0, 0, 0, 1]
# ]

map_middle = [
    [0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [7, 0, 2, 8, 6, 0, 0, 0, 4],
    [0, 0, 4, 0, 1, 3, 0, 0, 2],
    [6, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 9, 2, 0, 0, 0, 5],
    [0, 4, 0, 0, 0, 8, 0, 0, 7],
    [0, 5, 0, 3, 0, 4, 1, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0]
]

map_left_bottom = [
    [5, 9, 2, 0, 7, 0, 0, 4, 0],
    [0, 0, 0, 1, 0, 0, 0, 5, 0],
    [3, 0, 6, 5, 0, 0, 9, 0, 0],
    [8, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 8, 0, 3],
    [0, 2, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 9],
    [0, 4, 0, 0, 0, 0, 1, 0, 0],
    [0, 5, 0, 9, 0, 0, 7, 0, 4]
]

map_right_bottom = [
    [0, 0, 7, 0, 0, 0, 0, 0, 9],
    [1, 0, 0, 0, 0, 4, 0, 0, 3],
    [0, 0, 0, 9, 0, 2, 0, 0, 0],
    [8, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 2, 0, 1, 0, 4],
    [0, 0, 2, 0, 0, 7, 0, 5, 8],
    [0, 0, 6, 0, 0, 0, 0, 4, 0],
    [9, 0, 5, 0, 0, 0, 2, 0, 1]
]

question_maps = [
    map_middle,
    map_left_top,
    map_right_top,
    map_left_bottom,
    map_right_bottom
]
question_maps_mirror = copy.deepcopy(question_maps)


# 打印图表
def print_map(target_map):
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            if target_map[row_index][column_index] == 0:
                print(f"*\t", end="")
            elif target_map[row_index][column_index] == -1:
                print(f" \t", end="")
            else:
                print(f"{target_map[row_index][column_index]}\t", end="")
        print('')


def fill(row1, column1, map_index1):
    target_map = question_maps[map_index1]
    if target_map[row1][column1] > 9:  # 若值超过了9，则说明上一步有错
        target_map[row1][column1] = 0  # 上一步有错,则初始化本单元格的值
        return 0
    next_num = target_map[row1][column1] + 1  # 防止循环出现range(10，10)
    if next_num > 9:
        target_map[row1][column1] = 0
        return 0
    is_assign = False  # 用来记录本轮是否被赋值
    for num in range(next_num, 10):  # 尝试下一个值能否满足
        is_repeat = False
        for column_index in range(0, 9):  # 检查同一行是否重复
            if target_map[row1][column_index] == num:
                is_repeat = True
                break
        if not is_repeat:
            for row_index in range(0, 9):  # 检查同一列是否重复
                if target_map[row_index][column1] == num:
                    is_repeat = True
                    break
        if not is_repeat:
            min_row_9 = int(int(row1 / 3) * 3)  # 求出该元素所在九宫格的范围
            max_row_9 = int(((int(row1 / 3) + 1) * 3) - 1)
            min_column_9 = int(int(column1 / 3) * 3)
            max_column_9 = int(((int(column1 / 3) + 1) * 3) - 1)
            for row_index in range(min_row_9, max_row_9 + 1):
                for column_index in range(min_column_9, max_column_9 + 1):
                    if target_map[row_index][column_index] == num:
                        is_repeat = True
                        break
        if not is_repeat:
            target_map[row1][column1] = num  # 如果都不重复，则赋值到此单元格
            is_assign = True
            break
    if not is_assign:  # 如果本轮没被赋值，则说明上一轮赋值有错
        return 0
    else:
        return 1


def pre_index(row1, column1, map_index1):
    map_mirror = question_maps_mirror[map_index1]
    if row1 == 0 and column1 == 0:
        # print("出错啦")
        return -1, -1
    if column1 >= 1:  # 若列号大于等于一 则上一轮是本行的上一列
        column1 -= 1
    else:  # 若列号小于一 则上一轮是上一行的最后一列
        row1 -= 1
        column1 = 8
    # print(f"{row1}----{column1}")
    if map_mirror[row1][column1] != 0:  # 若上一个单元格内原本的数不是0，说明不是要求解的单元格，继续探测上一个的索引   # 这里用map_mirror代表最原始的题目的单元格状态
        row1, column1 = pre_index(row1, column1, map_index1)
        return row1, column1
    else:
        return row1, column1


def next_index(row1, column1, map_index1):  # 用来探测下一轮的索引
    map_mirror = question_maps_mirror[map_index1]
    if row1 == 8 and column1 == 8:
        return -1, -1
    if column1 < 8:  # 若列号小于8 则下一轮是本行的下一列
        column1 += 1
    else:  # 若列号等于8 则下一轮是下一行的第一列
        row1 += 1
        column1 = 0
    if map_mirror[row1][column1] != 0:  # 若下一个单元格内原本的数不是0，说明不是要求解的单元格，继续探测下一个的索引   # 这里用map_mirror代表最原始的题目的单元格状态
        row1, column1 = next_index(row1, column1, map_index1)
        return row1, column1
    else:
        return row1, column1


def fill_question_map():
    def fill_question_map():
        for row1 in range(0, 3):
            for column1 in range(0, 3):
                question_maps_mirror[1][row1 + 6][column1 + 6] = map_middle[row1][column1]
                question_maps[1][row1 + 6][column1 + 6] = map_middle[row1][column1]
            for column1 in range(6, 9):
                question_maps[2][row1 + 6][column1 - 6] = map_middle[row1][column1]
                question_maps_mirror[2][row1 + 6][column1 - 6] = map_middle[row1][column1]
        # print_map(map_right_top)
        for row1 in range(6, 9):
            for column1 in range(0, 3):
                question_maps[3][row1 - 6][column1 + 6] = map_middle[row1][column1]
                question_maps_mirror[3][row1 - 6][column1 + 6] = map_middle[row1][column1]
            for column1 in range(6, 9):
                question_maps[4][row1 - 6][column1 - 6] = map_middle[row1][column1]
                question_maps_mirror[4][row1 - 6][column1 - 6] = map_middle[row1][column1]


def resolve_edge():
    for i in range(1, 5):
        print(f"循环到{i}")
        row2 = 0
        column2 = 0
        map_index = i
        result_map = []  # 同一9*9数独的多个解的列表
        while True:
            result = 0
            if question_maps_mirror[map_index][row2][column2] == 0:
                result = fill(row2, column2, map_index)
            else:
                result = 1
            if result == 0:
                question_maps[map_index][row2][column2] = 0
                row2, column2 = pre_index(row2, column2, map_index)
                if row2 == -1 and column2 == -1:
                    print("结束---！")
                    break
            if result == 1:
                row_temp, column_temp = next_index(row2, column2, map_index)
                if row_temp == -1 and column_temp == -1:
                    # result_q = copy.deepcopy(question_maps[map_index])
                    # result_map.append(result_q)
                    print("答案之一  继续求解中！")
                    break
                else:
                    row2 = row_temp
                    column2 = column_temp
                    # break
        # if len(result_map) <= 0:  # 若单个9*9数独都无解  那么整体无解
        #     print("本题无解")
        # break
        # else:
        #     fill_question_map(i)
        for i in range(len(result_map)):
            print(f"2答案{i}")
            print_map(result_map[i])
            # question_maps[map_index] = result_map[i]


def resolve_middle():
    map_index = 0
    row = 0
    column = 0
    # result_map = []  # 同一9*9数独的多个解的列表
    while True:
        if question_maps_mirror[map_index][row][column] == 0:
            result = fill(row, column, map_index)
        else:
            result = 1
        if result == 0:
            question_maps[map_index][row][column] = 0
            row, column = pre_index(row, column, map_index)
            if row == -1 and column == -1:
                print("结束！")
                break
        if result == 1:
            row_temp, column_temp = next_index(row, column, map_index)
            if row_temp == -1 and column_temp == -1:
                # result = copy.deepcopy(question_maps[map_index])
                # result_map.append(result)
                print("答案之一  继续求解中！")
                fill_question_map()
                resolve_edge()
                break
                # print("adasdasd")
                # print_map(question_maps[])
                # print_map(question_maps[1])
            else:
                row = row_temp
                column = column_temp


def print_result():
    for row1 in range(0, 21):
        for column1 in range(0, 21):
            if row1 < 6:
                if column1 < 9:
                    print(f"{map_left_top[row1][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f" \t", end="")
                else:
                    print(f"{map_right_top[row1][column1 - 12]}\t", end="")
            if 5 < row1 < 9:
                if column1 < 9:
                    print(f"{map_left_top[row1][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f"{map_middle[row1-6][column1-6]}\t", end="")
                else:
                    print(f"{map_right_top[row1][column1 - 12]}\t", end="")
            if 8 < row1 < 12:
                if column1 < 6:
                    print(f" \t", end="")
                elif 5 < column1 < 15:
                    print(f"{map_middle[row1-6][column1-6]}\t", end="")
                else:
                    print(f" \t", end="")
            if 11 < row1 < 15:
                if column1 < 9:
                    print(f"{map_left_bottom[row1 - 12][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f"{map_middle[row1 - 6][column1 - 6]}\t", end="")
                else:
                    print(f"{map_right_bottom[row1-12][column1-12]}\t", end="")
            if row1 > 14:
                if column1 < 9:
                    print(f"{map_left_bottom[row1 - 12][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f" \t", end="")
                else:
                    print(f"{map_right_bottom[row1 - 12][column1 - 12]}\t", end="")
        print("")

if __name__ == '__main__':
    resolve_middle()
    print_result()
    # resolve_edge()
    # print_map(question_maps[0])
    # print()
    # print_map(question_maps[1])
    # print()
    # print_map(question_maps[2])
    # print()
    # print_map(question_maps[3])
    # print()
    # print_map(question_maps[4])
    # resolve_edge()
    # results = resolve9_9(0) # 先解出中间所有可能的情况
    # for result in results:
    # result_map_map = []  # 各个9*9数独的解列表的列表
    # for i in range(1,5):
    #     row = 0
    #     column = 0
    #     map_index = i
    #     result_map = []  # 同一9*9数独的多个解的列表
    #     while True:
    #         if question_maps_mirror[map_index][row][column] == 0:
    #             result = fill(row, column, map_index)
    #         else:
    #             result = 1
    #         if result == 0:
    #             question_maps[map_index][row][column] = 0
    #             row, column = pre_index(row, column, map_index)
    #             if row == -1 and column == -1:
    #                 print("结束！")
    #                 break
    #         if result == 1:
    #             row_temp, column_temp = next_index(row, column, map_index)
    #             if row_temp == -1 and column_temp == -1:
    #                 result = copy.deepcopy(question_maps[map_index])
    #                 result_map.append(result)
    #                 print("答案之一  继续求解中！")
    #             else:
    #                 row = row_temp
    #                 column = column_temp
    #                 # break
    #     if len(result_map) <= 0:  # 若单个9*9数独都无解  那么整体无解
    #         print("本题无解")
    #         break
    #     # else:
    #     #     fill_question_map(i)
    #     for i in range(len(result_map)):
    #         print(f"答案{i}")
    #         print_map(result_map[i])
    # result_map_map.append(result_map)  # 本轮9*9数独的解列表存储进各个9*9数独的解列表的列表
    # print(map_mirror)
