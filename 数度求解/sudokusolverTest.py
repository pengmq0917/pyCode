import copy

question1 = [
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

question2 = [
    [0, 0, 1, 0, 2, 0, 3, 0, 7, -1, -1, -1, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 7, 6, 2, 0, -1, -1, -1, 0, 0, 2, 7, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0, -1, -1, -1, 7, 0, 0, 1, 5, 0, 0, 0, 6],
    [0, 0, 4, 5, 1, 9, 0, 7, 0, -1, -1, -1, 0, 1, 0, 0, 0, 9, 8, 0, 0],
    [0, 0, 0, 4, 0, 3, 2, 9, 0, -1, -1, -1, 2, 0, 0, 5, 0, 0, 0, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 6, 1, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 4, 3, 0, 0, 0, 9],
    [0, 7, 0, 0, 9, 0, 0, 6, 0, 0, 0, 0, 0, 7, 0, 9, 2, 6, 3, 4, 0],
    [0, 0, 6, 8, 0, 0, 7, 0, 2, 8, 6, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1],
    [-1, -1, -1, -1, -1, -1, 0, 0, 4, 0, 1, 3, 0, 0, 2, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 6, 0, 0, 0, 0, 0, 0, 1, 0, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 0, 0, 0, 9, 2, 0, 0, 0, 5, -1, -1, -1, -1, -1, -1],
    [5, 9, 2, 0, 7, 0, 0, 4, 0, 0, 0, 8, 0, 0, 7, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 1, 0, 0, 0, 5, 0, 3, 0, 4, 1, 0, 0, 0, 0, 4, 0, 0, 3],
    [3, 0, 6, 5, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 2, 0, 0, 0],
    [8, 0, 0, 0, 2, 0, 0, 0, 0, -1, -1, -1, 8, 0, 0, 3, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 8, 0, 3, -1, -1, -1, 0, 0, 0, 4, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 0, 6, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 2, 0, 1, 0, 4],
    [0, 0, 0, 0, 6, 0, 0, 0, 9, -1, -1, -1, 0, 0, 2, 0, 0, 7, 0, 5, 8],
    [0, 4, 0, 0, 0, 0, 1, 0, 0, -1, -1, -1, 0, 0, 6, 0, 0, 0, 0, 4, 0],
    [0, 5, 0, 9, 0, 0, 7, 0, 4, -1, -1, -1, 9, 0, 5, 0, 0, 0, 2, 0, 1]

]


# 打印图表
def print_map(target_map):
    """
    打印单部分 即9*9数独
    :param target_map: 要打印的9*9数独
    :return:
    """
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            if target_map[row_index][column_index] == 0:
                print(f"*\t", end="")
            elif target_map[row_index][column_index] == -1:
                print(f" \t", end="")
            else:
                print(f"{target_map[row_index][column_index]}\t", end="")
        print('')


def pre_index(row1, column1, map_index1):
    """
    查找上一步
    :param row1: 当前行号
    :param column1: 当前列号
    :param map_index1: 当前是哪部分  0 中间 、1 左上 、2 右上 、3 左下 、4 右下
    :return:
    """
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


def next_index(row1, column1, map_index1):
    """
    查找下一步
    :param row1: 当前行号
    :param column1: 当前列号
    :param map_index1: 当前是哪部分  0 中间 、1 左上 、2 右上 、3 左下 、4 右下
    :return:
    """
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


def print_result(middle, left_top, right_top, left_bottom, right_bottom):
    """
    打印答案
    :param middle: 中间部分数独
    :param left_top: 左上部分数独
    :param right_top: 右上部分数独
    :param left_bottom: 左下部分数独
    :param right_bottom: 右下部分数独
    :return:
    """
    for row1 in range(0, 21):
        for column1 in range(0, 21):
            if row1 < 6:
                if column1 < 9:
                    print(f"{left_top[row1][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f" \t", end="")
                else:
                    print(f"{right_top[row1][column1 - 12]}\t", end="")
            if 5 < row1 < 9:
                if column1 < 9:
                    print(f"{left_top[row1][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f"{middle[row1 - 6][column1 - 6]}\t", end="")
                else:
                    print(f"{right_top[row1][column1 - 12]}\t", end="")
            if 8 < row1 < 12:
                if column1 < 6:
                    print(f" \t", end="")
                elif 5 < column1 < 15:
                    print(f"{middle[row1 - 6][column1 - 6]}\t", end="")
                else:
                    print(f" \t", end="")
            if 11 < row1 < 15:
                if column1 < 9:
                    print(f"{left_bottom[row1 - 12][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f"{middle[row1 - 6][column1 - 6]}\t", end="")
                else:
                    print(f"{right_bottom[row1 - 12][column1 - 12]}\t", end="")
            if row1 > 14:
                if column1 < 9:
                    print(f"{left_bottom[row1 - 12][column1]}\t", end="")
                elif 8 < column1 < 12:
                    print(f" \t", end="")
                else:
                    print(f"{right_bottom[row1 - 12][column1 - 12]}\t", end="")
        print("")


def fill(row1, column1, map_index1):
    """
    探测哪个数值可以填入
    :param row1: 行号
    :param column1: 列号
    :param map_index1: 当前是哪部分 0 中间 、1 左上 、2 右上 、3 左下 、4 右下
    :return: 0 代表填入失败  调用者根据返回值为0 进行回退一步操作
             1 代表填入成功  调用者根据返回值为0 进行前进一步操作
    """
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


def resolve_edge():
    """
    解答边缘四个部分
    :return:
    """
    answer_list_list = [[], [], [], []]  # 各个部分的解列表  分别为左上、右上、左下、右下
    for i in range(1, 5):
        print(f"循环到{i}")
        row2 = 0
        column2 = 0
        map_index = i
        answer_count = 0
        while True:
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
                    answer_count += 1
                    print(f"边缘{i}的第{answer_count}个解")
                    answer_list_list[map_index - 1].append(copy.deepcopy(question_maps[map_index]))
                else:
                    row2 = row_temp
                    column2 = column_temp
        if answer_count <= 0:  # 若有一部分一个解都的不出 则本题无解
            print("本题无解")
    # print(answer_list_list)
    # 遍历打印出所有解
    for i in range(0, len(answer_list_list[0])):
        for j in range(0, len(answer_list_list[1])):
            for k in range(0, len(answer_list_list[2])):
                for l in range(0, len(answer_list_list[3])):
                    print_result(
                        map_middle,
                        answer_list_list[0][i],
                        answer_list_list[1][j],
                        answer_list_list[2][k],
                        answer_list_list[3][l]
                    )
    # print_result()


def fill_question_map():
    """
    把中间部分解的结果填充进边缘重叠部分
    :return:
    """
    for row1 in range(0, 3):
        for column1 in range(0, 3):
            question_maps_mirror[1][row1 + 6][column1 + 6] = map_middle[row1][column1]
            question_maps[1][row1 + 6][column1 + 6] = map_middle[row1][column1]
        for column1 in range(6, 9):
            question_maps[2][row1 + 6][column1 - 6] = map_middle[row1][column1]
            question_maps_mirror[2][row1 + 6][column1 - 6] = map_middle[row1][column1]
    for row1 in range(6, 9):
        for column1 in range(0, 3):
            question_maps[3][row1 - 6][column1 + 6] = map_middle[row1][column1]
            question_maps_mirror[3][row1 - 6][column1 + 6] = map_middle[row1][column1]
        for column1 in range(6, 9):
            question_maps[4][row1 - 6][column1 - 6] = map_middle[row1][column1]
            question_maps_mirror[4][row1 - 6][column1 - 6] = map_middle[row1][column1]


def resolve():
    """
    解答中间部分 并在计算出每一种可能后去解答边缘部分 可能有多个解 则边缘部分解答多次
    :return:
    """
    map_index = 0  # question_maps索引为0 代表中间部分列表  先求中间部分
    row = 0
    column = 0
    answer_count = 0  # 中间部分解的个数
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
                # 根据中间部分的每种答案的可能  把数填入边缘四个部分重叠的地方 再求边缘四个部分
                answer_count += 1
                print(f"中间部分第{answer_count}个解  继续求解边缘！")
                fill_question_map()
                resolve_edge()
                # break
            else:
                row = row_temp
                column = column_temp
    if answer_count <= 0:  # 若有一部分一个解都的不出 则本题无解
        print("本题无解")


def cut_question(entirety_map):
    """
    对整体题目进行切片  分成中间、左上、右上、左下、右下
    :param entirety_map:
    :return:
    """
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            map_left_top[row_index][column_index] = entirety_map[row_index][column_index]
        for column_index in range(12, 21):
            map_right_top[row_index][column_index - 12] = entirety_map[row_index][column_index]
    for row_index in range(6, 15):
        for column_index in range(6, 15):
            map_middle[row_index - 6][column_index - 6] = entirety_map[row_index][column_index]
    for row_index in range(12, 21):
        for column_index in range(0, 9):
            map_left_bottom[row_index - 12][column_index] = entirety_map[row_index][column_index]
        for column_index in range(12, 21):
            map_right_bottom[row_index - 12][column_index - 12] = entirety_map[row_index][column_index]


def data_initial(entirety_map):
    """
    初始化各个工具数组
    :param entirety_map:
    :return:
    """
    # 撑开五个部分的数组 使其成为9*9二维数组
    for row_init_index in range(0, 9):
        for column_init_index in range(0, 9):
            if column_init_index == 0:
                map_middle.append([])
                map_left_top.append([])
                map_right_top.append([])
                map_left_bottom.append([])
                map_right_bottom.append([])
            map_middle[row_init_index].append(0)
            map_left_top[row_init_index].append(0)
            map_right_top[row_init_index].append(0)
            map_left_bottom[row_init_index].append(0)
            map_right_bottom[row_init_index].append(0)

    cut_question(
        entirety_map)  # 对题目进行切片  把五个部分分布复制到 map_middle、  map_left_top、 map_right_top、 map_left_bottom、 map_right_bottom
    global question_maps
    question_maps = [
        map_middle,
        map_left_top,
        map_right_top,
        map_left_bottom,
        map_right_bottom
    ]
    global question_maps_mirror
    question_maps_mirror = copy.deepcopy(question_maps)


if __name__ == '__main__':
    map_middle = []  # 用于存储题目中部
    map_left_top = []  # 用于存储题目左上部
    map_right_top = []  # 用于存储题目右上部
    map_left_bottom = []  # 用于存储题目左下部
    map_right_bottom = []  # 用于存储题目右下部

    data_initial(question2)  # 初始化各工具数组
    # 求解
    resolve()
