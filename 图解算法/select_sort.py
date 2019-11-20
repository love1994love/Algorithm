# 选择排序：P25
"""
    链表的优势在于插入和删除
    数组的优势在于随机访问成员

    运行时间( O(n)==>线性时间   O(1)==>常量时间 )
    数组：读取O(1)、插入O(n)、删除O(n)
    链表：读取O(n)、插入O(1)、删除O(1)

    选择排序的时间复杂度为 O(n^2)
"""

def findSmallest(arr):
    smallest = arr[0]       # 存储最小的值
    smallest_index = 0      # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 对数组进行排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

myArr = [5, 3, 6, 2, 10]
print(selectionSort(myArr))