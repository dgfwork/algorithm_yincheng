# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 20:14
# @Author  : Scavenger
# @FileName: 5_QuickSort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def QuickSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    splitdata = lst[0]  # 以第一个为基准
    low = []
    high = []
    mid = []
    mid.append(splitdata)
    for i in range(1, n):
        if lst[i] < splitdata:
            low.append(lst[i])
        elif lst[i] > splitdata:
            high.append(lst[i])
        else:
            mid.append(lst[i])
        low, high = QuickSort(low), QuickSort(high)
    mylst = low + mid + high
    return mylst


if __name__ == "__main__":
    lst = [3, 1, 5, 4, 7, 6, 8, 0]
    # lst = HeapSortMax(lst)
    lst = QuickSort(lst)
    print(lst)

