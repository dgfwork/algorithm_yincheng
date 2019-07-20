# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 14:01
# @Author  : Scavenger
# @FileName: bublesort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

"""

//11,9,2,8,3,7,4,6,5,10
//9 11 2 8 3 7 4 6 5 10
//9 2 11 8 3 7 4 6 5 10
//9 2 8 11 3 7 4 6 5 10
//9 2 8 3 11 7 4 6 5 10
//9 2 8 3 7 11  4 6 5 10
//9 2 8 3 7 4  11 6 5 10
//9 2 8 3 7 4  6 11  5 10
//9 2 8 3 7 4  6  5 11 10
//9 2 8 3 7 4  6  5 10 11
//2 9 8 3 7 4  6  5 10 11
//
"""


def bublesort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(n - 1):  # 只剩最后一个不需要冒泡
        isneedexchange = False
        for j in range(n - 1 - i):  # 两两比较  这样将大的数放到后面 每一趟比上一趟少一个
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                isneedexchange = True

        # 走一趟如果没有交换的话  就结束掉外层循环
        if isneedexchange == False:
            break
    return lst


if __name__ == "__main__":
    lst = [3, 1, 2, 6, 5]
    ret = bublesort(lst)
    print(ret)
