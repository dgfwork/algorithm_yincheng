# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 23:07
# @Author  : Scavenger
# @FileName: selectsort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/


def SelectSortMax(arr):
    n = len(arr)
    if n <= 1:
        return arr
    min = 0
    for i in range(0, n):
        if arr[i] > arr[min]:
            min = i
    return arr[min]


def selectsort(arr):
    # 本算法的思想就是每一趟找出一个最小值
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(0, n - 1):  # 这里面只剩一个元素不需要挑选
        min = i  # 我假设这个元素是这一趟里面的最小值
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                min = j  # 保存每一趟的极小值
        if i != min:
            arr[min], arr[i] = arr[i], arr[min]
        print(arr)
    return arr


if __name__ == "__main__":
    lst = [7, 1, 6, 9, 8]
    ret = selectsort(lst)
    max = SelectSortMax(lst)
    print(ret, max)
