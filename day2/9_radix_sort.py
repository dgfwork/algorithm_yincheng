# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 7:59
# @Author  : Scavenger
# @FileName: 9_radix_sort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

"""
银行 没人都有存款

800W考生分数排序

1亿人身高排序

"""


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


def RadixSort(lst):
    # 第一步 找到极大值
    max = SelectSortMax(lst)
    print("max", max)
    bit = 1
    while max // bit > 0:
        # 按照数量级分段  每个数量级别的循环一次
        # 每次处理一个级别的排序，先处理个位数的排序，再处理十位数的排序
        lst = BitSort(lst, bit)
        print("每趟排序结果:", lst)
        bit = bit * 10
    return lst


def BitSort(lst, bit):
    n = len(lst)
    # 开辟数组保存余数相等的个数
    bitcounts = [0 for i in range(10)]
    for i in range(n):
        num = (lst[i] // bit) % 10
        bitcounts[num] += 1  # 计算余数相等的个数
    print("统计余数相等的结果:", bitcounts)

    # 累加数据长度 叠加  计算位置

    """
    0   1   2   3   4   5   6
    1   0   2   3   0   0   4
    1   1   3   6   6   6   10
    """
    for i in range(1, 10):
        bitcounts[i] += bitcounts[i - 1]
    print("累加结果:", bitcounts)

    tmp = [0 for i in range(10)]
    for i in range(n - 1, -1, -1):
    # for i in range(0, n):
        # 上面的信息统计完后  刷一遍数组
        num = (lst[i] // bit) % 10  # 第一轮时  最后一个数是81 bit=1  那么num就是1
        # 这个就是取余数  查到相应位置
        tmp[bitcounts[num] - 1] = lst[i]  # 扫一遍 找到每个数的位置
        # 比如 39 第一次得到的num是9 这个实际上就是索引 因为N个数在数组里面的索引是0~N-1

        bitcounts[num] -= 1

    return tmp


if __name__ == "__main__":
    # lst = [13, 12, 544, 3564, 57437, 3226, 234558, 30]
    lst = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81]
    lst = RadixSort(lst)
    print(lst)
