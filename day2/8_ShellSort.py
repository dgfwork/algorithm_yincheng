# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 7:38
# @Author  : Scavenger
# @FileName: 8_ShellSort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/


def ShellSortStep(lst, start, gap):
    n = len(lst)
    for i in range(start + gap, n, gap):
        backup = lst[i]
        j = i - gap
        while j >= 0 and backup < lst[j]:
            lst[j + gap] = lst[j]
            j -= gap
        lst[j + gap] = backup


def ShellSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        gap = n // 2
        while gap > 0:
            for i in range(gap):
                ShellSortStep(lst, i, gap)
            gap = gap // 2
            # 或者步长-1
    return lst


if __name__ == "__main__":
    lst = [3, 1, 5, 4, 7, 6, 8, 0]
    lst = ShellSort(lst)
    print(lst)
