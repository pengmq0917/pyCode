def test():
    return 0,1

if __name__ == '__main__':
    row1 = 7
    column1 = 10
    min_row_9 = int(int(row1 / 3) * 3)  # 求出该元素所在九宫格的范围
    max_row_9 = int(((int(row1 / 3) + 1) * 3) - 1)
    min_column_9 = int(int(column1 / 3) * 3)
    max_column_9 = int(((int(column1 / 3) + 1) * 3) - 1)
    print(f"{min_row_9}```{max_row_9}")
    print(f"{min_column_9}```{max_column_9}")