import sys

sys.setrecursionlimit(100000)

map = [
    [0, 2, 3, 0, 0, 7, 5, 0, 0],
    [0, 0, 7, 0, 0, 0, 1, 0, 0],
    [0, 0, 4, 0, 0, 3, 8, 0, 0],
    [3, 0, 0, 0, 6, 8, 0, 9, 0],
    [1, 0, 0, 0, 7, 2, 6, 0, 5],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 4, 5, 7],
    [0, 9, 0, 0, 0, 0, 3, 2, 6],
    [0, 4, 6, 0, 0, 0, 9, 8, 1],
]

map_mirror = [
    [0, 2, 3, 0, 0, 7, 5, 0, 0],
    [0, 0, 7, 0, 0, 0, 1, 0, 0],
    [0, 0, 4, 0, 0, 3, 8, 0, 0],
    [3, 0, 0, 0, 6, 8, 0, 9, 0],
    [1, 0, 0, 0, 7, 2, 6, 0, 5],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 4, 5, 7],
    [0, 9, 0, 0, 0, 0, 3, 2, 6],
    [0, 4, 6, 0, 0, 0, 9, 8, 1],
]  # 用来探测数字


# 打印图表
def print_map():
    for row_index in range(0, 9):
        for column_index in range(0, 9):
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
    is_assign = False  # 用来记录本轮是否被赋值
    for num in range(map[row1][column1] + 1, 10):  # 尝试下一个值能否满足
        is_repeat = False
        for column_index in range(0, 9):  # 检查同一行是否重复
            if map[row1][column_index] == num:
                is_repeat = True
                break
        if not is_repeat:
            for row_index in range(0, 9):  # 检查同一列是否重复
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
        return 0

    if is_assign:  # 如果被赋值了，则可进入下一个单元格
        return 1


def pre_index(row1, column1):
    if row1 == 0 and column1 == 0:
        print("出错啦")
        return -1,-1
    if column1 >= 1:  # 若列号大于等于一 则上一轮是本行的上一列
        column1 -= 1
    else:  # 若列号小于一 则上一轮是上一行的最后一列
        row1 -= 1
        column1 = 8
    # print(f"{row1}----{column1}")
    if map_mirror[row1][column1] != 0:  # 若上一个单元格内原本的数不是0，说明不是要求解的单元格，继续探测上一个的索引   # 这里用map_mirror代表最原始的题目的单元格状态
        row1, column1 = pre_index(row1, column1)
        return row1, column1
    else:
        return row1, column1


def next_index(row1, column1):  # 用来探测下一轮的索引
    if row1 == 8 and column1 == 8:
        return -1,-1
    if column1 < 8:  # 若列号小于20 则下一轮是本行的下一列
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
            # if row == -1 and column == -1:
            #     print("结束！")
            #     break
            map[row][column] = 0
            row, column = pre_index(row, column)
            if row == -1 and column == -1:
                print("结束！")
                break
        if result == 1:
            # if (row == -1 and column == -1):
            #     print("结束！")
            #     break
            row, column = next_index(row, column)
            if(row == -1 and column == -1):
                print("结束！")
                break

    print_map()
    print(map_mirror)
