# 二分查找：
"""
    输入是一个有序的元素列表，如果查找的元素包含在列表中，
    二分查找返回其位置，否则返回null。

    二分查找，每次从中间开始，所以每次可以将剩下的一般排除，所以以2为底，
    用二分查找最多需要log2(n)步，其时间复杂度是log2(n)
"""

def binary_search(list, item):
    # low 和 high 用于跟踪要在其中查找的列表的部分
    low = 0
    high = len(list) - 1

    while low < high:                   # 只要范围没有缩小到只包含一个元素
        mid = (low + high) // 2         # 就查找中间元素，若(low+high)不是偶数,python自动往下取整
        guess = list[mid]
        if guess == item:               # 找到了元素
            return mid
        if guess > item:                # 猜大了
            high = mid - 1
        else:
            low = mid + 1
    return None

# 测试
import numpy as np
my_list = np.arange(0,20,2)
print(my_list)
print(binary_search(my_list, 8))
print(binary_search(my_list,20))