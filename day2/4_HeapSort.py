# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 14:18
# @Author  : Scavenger
# @FileName: 4_HeapSort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

"""
堆排序里面的存储结构是数组  逻辑结构是二叉树

"""


def HeapSortMax(lst, n):
    # 找出最大值登顶对顶
    # n = len(lst)
    if n <= 1:
        return lst
    depth = n // 2 - 1  # 这个深度是0~depth
    # 下面开始调整堆 从最后一个非终端节点开始调整
    for i in range(depth, -1, -1):
        topmax = i
        leftchild = 2 * i + 1
        rightchild = 2 * i + 2  # 左右孩子节点
        # 从这三个节点里面选出最大值 还要不能越界才得行
        if leftchild <= n - 1 and lst[leftchild] > lst[topmax]:
            topmax = leftchild
        if rightchild <= n - 1 and lst[rightchild] > lst[topmax]:
            topmax = rightchild
        if i != topmax:
            lst[topmax], lst[i] = lst[i], lst[topmax]
    return lst


def HeapSort(lst):
    n = len(lst)
    for i in range(n):
        lastmesslen = n - i
        # 每次登顶了数组长度就少了一个了
        HeapSortMax(lst, lastmesslen)
        # print(lst)
        if i < n:
            lst[0], lst[lastmesslen - 1] = lst[lastmesslen - 1], lst[0]
            # 这个位置为什么是lastmesslen-1呢?道理很简单
            # 最后一个元素本来就是lastmesslen-1，lastmesslen已经越界了
        # print("ex", lst)

    return lst


if __name__ == "__main__":
    lst = [3, 1, 5, 4, 7, 6, 8, 0]
    # lst = HeapSortMax(lst)
    lst = HeapSort(lst)
    print(lst)
