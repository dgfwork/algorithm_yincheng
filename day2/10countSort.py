# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 9:05
# @Author  : Scavenger
# @FileName: 9countSort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def SelectSortMax(arr):
    """

    :param arr:传入参数为数组
    :return: 返回数组里面的最大值
    """
    n = len(arr)
    if n <= 1:
        return arr
    max = 0
    for i in range(0, n):
        if arr[i] > arr[max]:
            max = i
    return arr[max]


def CountSort(arr):
    """
    银行 没人都有存款
    800W考生分数排序
    10亿人身高排序
    lst = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81] 这种数组采取本算法也是可以的
    不过呢 这个效率实在是太低了
    :param arr: 待排数组
    :return: 有序数组
    """
    max = SelectSortMax(arr)
    n = len(arr)
    sortedarr = [0 for i in range(n)]
    countarr = [0 for i in range(n)]
    for v in arr:
        countarr[v] += 1
    print("第一次统计数:", countarr)

    for i in range(1, max + 1):
        countarr[i] += countarr[i - 1]
    print("叠加次数:", countarr)
    for v in arr:
        sortedarr[countarr[v] - 1] = v  # 展开数据
        countarr[v] -= 1  # 递减
        print("zkcount", countarr)
        print("zk", sortedarr)
    return sortedarr


if __name__ == "__main__":
    # lst = [13, 12, 544, 3564, 57437, 3226, 234558, 30]
    # lst = [73, 22, 33, 33, 93, 43, 55, 14, 28, 65, 39, 81]
    lst = [1, 2, 3, 4, 3, 2, 1, 2, 5, 5, 3, 4, 3, 2, 1]
    # 说白了就是统计每个数字出现了多少次
    lst = CountSort(lst)
    print(lst)
