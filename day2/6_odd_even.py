# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 23:03
# @Author  : Scavenger
# @FileName: 6_odd_even.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

"""
奇偶排序可以多线程
适用于身高排序
"""


def oddEven(lst):
    n = len(lst)
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(1, n - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                isSorted = False
        for i in range(0, n - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                isSorted = False
    return lst


if __name__ == "__main__":
    lst = [3, 1, 5, 4, 7, 6, 8, 0]
    lst = oddEven(lst)
    print(lst)
    """
    [0, 1, 3, 4, 5, 6, 7, 8]
    """
