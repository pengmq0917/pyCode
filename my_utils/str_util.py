"""
字符串相关模块
"""


def str_reverse(s):
    """
    功能：将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反专制和的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    功能：将字符串按照给定的下标完成给定字符串的切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("pengmq"))
    print(substr("pengmq",1,3))
