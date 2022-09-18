import sys

sys.setrecursionlimit(100000)

map = [
    [0, 2, 3, 0, 0, 7, 5, 0, 0, -1, -1, -1, 3, 0, 4, 0, 0, 7, 0, 2, 0],
    [0, 0, 7, 0, 0, 0, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 2, 0, 0, 8, 0],
    [0, 0, 4, 0, 0, 3, 8, 0, 0, -1, -1, -1, 0, 8, 0, 5, 0, 1, 0, 0, 0],
    [3, 0, 0, 0, 6, 8, 0, 9, 0, -1, -1, -1, 5, 0, 0, 0, 0, 0, 3, 0, 0],
    [1, 0, 0, 0, 7, 2, 6, 0, 5, -1, -1, -1, 6, 2, 0, 4, 0, 0, 0, 0, 1],
    [0, 0, 0, 5, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 0, 6, 0, 0, 5],
    [0, 9, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 8, 9, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 0, 0, 0, 8, 0, 2, 0, 3, 4, 0, 0, 8, 1, 3, 7, 0, 0],
    [-1, -1, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0, 9, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 0, 0, 4, 0, 0, 0, 6, 0, 3, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 0, 0, 5, 0, 0, 0, 0, 2, 1, -1, -1, -1, -1, -1, -1],
    [0, 8, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 3, 5, 0, 0, 7, 0, 0, 9, 0, 0, 8, 3, 5, 7, 8, 0, 2, 0, 0, 0],
    [0, 0, 4, 0, 2, 5, 8, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 7, 0, 1, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 8, -1, -1, -1, 0, 0, 0, 0, 2, 0, 0, 9, 0],
    [0, 6, 9, 0, 0, 0, 4, 2, 0, -1, -1, -1, 5, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, -1, 6, 0, 0, 0, 8, 3, 0, 0, 0],
    [6, 7, 0, 8, 0, 0, 0, 0, 1, -1, -1, -1, 8, 0, 2, 4, 0, 0, 7, 0, 0],
    [0, 4, 0, 2, 0, 0, 0, 0, 5, -1, -1, -1, 0, 0, 0, 0, 9, 0, 2, 0, 0],
    [0, 0, 1, 0, 7, 0, 3, 0, 0, -1, -1, -1, 0, 4, 3, 0, 0, 5, 0, 0, 0]
]

map_mirror = [
    [0, 2, 3, 0, 0, 7, 5, 0, 0, -1, -1, -1, 3, 0, 4, 0, 0, 7, 0, 2, 0],
    [0, 0, 7, 0, 0, 0, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 2, 0, 0, 8, 0],
    [0, 0, 4, 0, 0, 3, 8, 0, 0, -1, -1, -1, 0, 8, 0, 5, 0, 1, 0, 0, 0],
    [3, 0, 0, 0, 6, 8, 0, 9, 0, -1, -1, -1, 5, 0, 0, 0, 0, 0, 3, 0, 0],
    [1, 0, 0, 0, 7, 2, 6, 0, 5, -1, -1, -1, 6, 2, 0, 4, 0, 0, 0, 0, 1],
    [0, 0, 0, 5, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 0, 6, 0, 0, 5],
    [0, 9, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 8, 9, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 0, 0, 0, 8, 0, 2, 0, 3, 4, 0, 0, 8, 1, 3, 7, 0, 0],
    [-1, -1, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0, 9, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 0, 0, 4, 0, 0, 0, 6, 0, 3, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 0, 0, 5, 0, 0, 0, 0, 2, 1, -1, -1, -1, -1, -1, -1],
    [0, 8, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 3, 5, 0, 0, 7, 0, 0, 9, 0, 0, 8, 3, 5, 7, 8, 0, 2, 0, 0, 0],
    [0, 0, 4, 0, 2, 5, 8, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 7, 0, 1, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 8, -1, -1, -1, 0, 0, 0, 0, 2, 0, 0, 9, 0],
    [0, 6, 9, 0, 0, 0, 4, 2, 0, -1, -1, -1, 5, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, -1, 6, 0, 0, 0, 8, 3, 0, 0, 0],
    [6, 7, 0, 8, 0, 0, 0, 0, 1, -1, -1, -1, 8, 0, 2, 4, 0, 0, 7, 0, 0],
    [0, 4, 0, 2, 0, 0, 0, 0, 5, -1, -1, -1, 0, 0, 0, 0, 9, 0, 2, 0, 0],
    [0, 0, 1, 0, 7, 0, 3, 0, 0, -1, -1, -1, 0, 4, 3, 0, 0, 5, 0, 0, 0]
]  # 用来探测数字


# def copy_map():
#     for (r_index, row) in enumerate(map):
#         for (c_index, item) in enumerate(row):
#             map_mirror[r_index][c_index] = item
# map_bak = map  # 用来备份原题

# 打印图表
def print_map():
    for row_index in range(0, 21):
        for column_index in range(0, 21):
            if map[row_index][column_index] == 0:
                print(f"*\t", end="")
            elif map[row_index][column_index] == -1:
                print(f" \t", end="")
            else:
                print(f"{map[row_index][column_index]}\t", end="")
        print('')


def fill(row1, column1):
    if map[row1][column1] >= 10:  # 若值超过了9，则说明上一步有错
        map[row1][column1] = 0  # 上一步有错,则初始化本单元格的值
        # if row == 0 and column == 0:
        #     return
        # row, column = pre_index(row, column)
        # fill(row, column)
        return 0
    is_assign = False  # 用来记录本轮是否被赋值
    for num in range(map[row1][column1] + 1, 10):  # 尝试下一个值能否满足
        is_repeat = False
        min_column, max_column = column_index_range(row1, column1)
        for column_index in range(min_column, max_column + 1):  # 检查同一行是否重复
            if map[row1][column_index] == num:
                is_repeat = True
                break
        if not is_repeat:
            min_row, max_row = row_index_range(row1, column1)
            for row_index in range(min_row, max_row + 1):  # 检查同一列是否重复
                if map[row_index][column1] == num:
                    is_repeat = True
                    break
        if not is_repeat:
            min_row_9 = int(int(row1 / 3) * 3)  # 求出该元素所在九宫格的范围
            max_row_9 = int(((int(row1 / 3) + 1) * 3) - 1)
            min_column_9 = int(int(column1 / 3) * 3)
            max_column_9 = int(((int(column1 / 3) + 1) * 3) - 1)
            for row_index in range(min_row_9, max_row_9 + 1):
                for column_index in range(min_column_9, max_column_9 + 1):
                    if map[row_index][column_index] == num:
                        is_repeat = True
                        break
        if not is_repeat:
            map[row1][column1] = num  # 如果都不重复，则赋值到此单元格
            is_assign = True
            break
    if not is_assign:  # 如果本轮没被赋值，则说明上一轮赋值有错
        # if row == 0 and column == 0:
        #     return  # 求解失败
        # row, column = pre_index(row, column)
        # map[row][column] += 1  # 上一轮赋值有错,则尝试下一个值
        return 0
        # fill(row, column)

    if is_assign:  # 如果被赋值了，则可进入下一个单元格
        # if row == 20 and column == 20:
        #     return  # 求解成功
        # row, column = next_index(row, column)
        # fill(row, column)
        return 1


def row_index_range(row1, column1):  # 计算要对比的行
    print(f"{row}+++++++{column}")
    if row1 < 6:
        return 0, 8
    if 5 < row1 < 9 and (column1 < 6 or column1 > 14):
        return 0, 8
    if 5 < row1 < 9 and (5 < column1 < 9 or 11 < column1 < 15):
        return 0, 14
    if 5 < row1 < 9 and (8 < column1 < 12):
        return 6, 14
    if 8 < row1 < 12:
        return 9, 11
    if 11 < row1 < 15 and (column1 < 6 or column1 > 14):
        return 12, 20
    if 11 < row1 < 15 and (5 < column1 < 9 or 11 < column1 < 15):
        return 6, 20
    if 11 < row1 < 15 and (8 < column1 < 12):
        return 6, 14
    if row1 > 14:
        return 12, 20


def column_index_range(row1, column1):  # 计算要对比的列
    if column1 < 6:
        return 0, 8
    if 5 < column1 < 9 and (row1 < 6 or row1 > 14):
        return 0, 8
    if 5 < column1 < 9 and (5 < row1 < 9 or 11 < row1 < 15):
        return 0, 14
    if 5 < column1 < 9 and (8 < row1 < 12):
        return 6, 14
    if 8 < column1 < 12:
        return 9, 11
    if 11 < column1 < 15 and (row1 < 6 or row1 > 14):
        return 12, 20
    if 11 < column1 < 15 and (5 < row1 < 9 or 11 < row1 < 15):
        return 6, 20
    if 11 < column1 < 15 and (8 < row1 < 12):
        return 6, 14
    if column1 > 14:
        return 12, 20


def pre_index(row1, column1):
    if row1 == 0 and column1 == 0:
        return -1,-1
    if column1 > 0:  # 若列号大于等于一 则上一轮是本行的上一列
        column1 -= 1
    else:  # 若列号小于一 则上一轮是上一行的最后一列
        row1 -= 1
        column1 = 20
    # print(f"{row1}----{column1}")
    if map_mirror[row1][column1] != 0:  # 若上一个单元格内原本的数不是0，说明不是要求解的单元格，继续探测上一个的索引   # 这里用map_mirror代表最原始的题目的单元格状态
        row1, column1 = pre_index(row1, column1)
        return row1, column1
    else:
        return row1, column1


def next_index(row1, column1):  # 用来探测下一轮的索引
    if row1 == 20 and column1 == 20:
        return -1,-1
    if column1 < 20:  # 若列号小于20 则下一轮是本行的下一列
        column1 += 1
    else:  # 若列号等于20 则下一轮是下一行的第一列
        row1 += 1
        column1 = 0
    if map_mirror[row1][column1] != 0:  # 若下一个单元格内原本的数不是0，说明不是要求解的单元格，继续探测下一个的索引   # 这里用map_mirror代表最原始的题目的单元格状态
        row1, column1 = next_index(row1, column1)
        return row1, column1
    else:
        return row1, column1


if __name__ == '__main__':
    row = 0
    column = 0
    while True:
        # print_map()
        print(f"{row}------{column}")
        result = fill(row, column)
        print(result)
        if result == 0:
            map[row][column] = 0
            row, column = pre_index(row, column)
            if row == -1 and column == -1:
                print("结束！")
                break
        if result == 1:
            row, column = next_index(row, column)
            if (row == -1 and column == -1):
                print("结束！")
                break

    print_map()
    print(map_mirror)
