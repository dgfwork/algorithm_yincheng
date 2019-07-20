# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 12:49
# @Author  : Scavenger
# @FileName: insertsort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

"""
[3, 1, 2, 6, 5]

[1, 3, 2, 6, 5]

[1, 2, 3, 6, 5]

[1, 2, 3, 5, 6]
"""


def func(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        backup = lst[i]  # 当前要排序的元素
        # 在前面有序的序列里面找一个适当的位置插进去
        j = i - 1
        while j >= 0 and backup < lst[j]:
            # 当前元素和前一个元素比较
            # 小的排在前面 只要比当前大的都要排在后面
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = backup  # 怎么确定这个位置的下标呢
        # 这个实际上很简单 因为前面j移动到后一个位置了
        # 而最后然后j又减一了所以实际上空的是j-1
        print(lst)
    return lst


if __name__ == "__main__":
    lst = [3, 1, 2, 6, 5]
    ret = func(lst)
    print(ret)