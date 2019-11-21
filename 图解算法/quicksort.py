# 快速排序：P25
"""
    分而治之(divide and conquer)——一种著名的递归式问题解决方法，包含两个步骤：
    1、找出基线条件，这种条件必须尽可能简单
    2、不断将问题分解(或者说缩小规模)，直到符合基线条件

"""
# # 例子1
# def sum(list):
#     if len(list) == 0:
#         return 0
#     return list[0] + sum(list[1:])
# # 测试
# mylist = [1,2,3,4,5]
# print(sum(mylist))

# # 例子：编写一个递归函数来计算列表包含的元素数
# def count(list):
#     if list == []:
#         return 0
#     return 1 + count(list[1:])
# mylist = [1,2,3,4,5]
# print(count(mylist))

# # 例子：找出列表中最大的数字
# def findLargest(list):
#     largest = list[0]
#     largest_index = 0
#     for i in range(1,len(list)):
#         if list[i] > largest:
#             largest = list[i]
#             largest_index = i
#     return largest_index
# mylist = [1,2,3,4,5]
# print(findLargest(mylist))

# 快速排序
'''

    步骤：
        1、选择基准值
        2、将数组分为两个子数组，小于基准值的元素组成的子数组和大于基准值的元素组成的子数组
        3、对这两个子数组进行快速排序

    快速排序的时间复杂度为 O(nlogn)
'''
def quicksort(array):
    if len(array) < 2:
        return array            # 基线条件：为空或者只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]        # 选择基准值

        # 由所有小于等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([3,1,4,9,2]))

