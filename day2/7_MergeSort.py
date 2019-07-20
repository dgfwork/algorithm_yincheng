# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 23:45
# @Author  : Scavenger
# @FileName: 7_MergeSort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def Merge(leftlst, rightlst):
    leftIndex = 0
    rightIndex = 0
    lastlst = []
    while leftIndex < len(leftlst) and rightIndex < len(rightlst):
        if leftlst[leftIndex] < rightlst[rightIndex]:
            lastlst.append(leftlst[leftIndex])
            leftIndex = leftIndex + 1
        elif leftlst[leftIndex] > rightlst[rightIndex]:
            lastlst.append(rightlst[rightIndex])
            rightIndex = rightIndex + 1
        else:
            lastlst.append(leftlst[leftIndex])
            lastlst.append(rightlst[rightIndex])
            leftIndex = leftIndex + 1
            rightIndex = rightIndex + 1

    while leftIndex < len(leftlst):
        lastlst.append(leftlst[leftIndex])
        leftIndex = leftIndex + 1
    while rightIndex < len(rightlst):
        lastlst.append(rightlst[rightIndex])
        rightIndex = rightIndex + 1
    return lastlst


# def func(lst):
#     n = len(lst)
#     if n <= 1:
#         return lst
#     for i in range(1, n):
#         backup = lst[i]  # 当前要排序的元素
#         # 在前面有序的序列里面找一个适当的位置插进去
#         j = i - 1
#         while j >= 0 and backup < lst[j]:
#             # 当前元素和前一个元素比较
#             # 小的排在前面 只要比当前大的都要排在后面
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = backup  # 怎么确定这个位置的下标呢
#         # 这个实际上很简单 因为前面j移动到后一个位置了
#         # 而最后然后j又减一了所以实际上空的是j-1
#         print(lst)
#     return lst


def MergeSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    # elif n >= 2 and n <= 5:
    #     return func(lst)
    else:
        mid = n // 2
        leftlst = MergeSort(lst[:mid])
        print(leftlst)
        rightlst = MergeSort(lst[mid:])
        print(rightlst)
        return Merge(leftlst, rightlst)


if __name__ == "__main__":
    lst = [3, 1, 5, 4, 7, 6, 8, 0]
    lst = MergeSort(lst)
    print(lst)
