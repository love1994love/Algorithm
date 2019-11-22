# 广度优先算法：P2
"""
    解决最短路径问题的算法被称为广度优先算法
    明白什么是图，包含节点和边，什么是邻居，
    广度优先算法可回答两类问题：一是有路径嘛？二是那条路径最短？
    队列，不能随机访问队列中的元素，队列只支持两种操作：入队和出队
    队列类似于栈，不同的是，栈是一种先进后出，而队列是先进先出

    广义优先算法的时间复杂度为 O(V+E)  : V:vertice(顶点-->人数) E:edge(边)
"""

# 图的实现
# 一层图的实现
graph = {}
graph['you'] = ['love', 'leo', 'wen']
# 多层图的实现
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# 实现算法
'''
            流程图
                    1、创建一个队列，用于存储要检查的人
                    2、从队列中弹出第一个人
                    3、检查这个人是否是要找的人
                        是-->返回成功
                        否-->将这个人的所有邻居都加入到队列中，并返回到第二步
                    4、如果队列为空，就说明你的人际关系网中没有你要找的人
'''
# # 初始版本
# from collections import deque
# search_queue = deque()              # 创建一个队列
# search_queue += graph['you']
#
# while search_queue:                 # 只要队列不为空
#     person = search_queue.popleft() # 取出其中的第一个人
#     if person_is_seller(person):    # 检查这个人是否是芒果经销商
#         print(person + " is a mango seller!")
#         return True
#     else:
#         search_queue += graph[person]   # 不是芒果经销商，将这个人的朋友加入到搜索队列中
# return False                    # 如果到达了这里，就说明队列中没有芒果经销商

def person_is_seller(name):
    return name[-1] == 'm'        # 名字以m结果，就是芒果经销商


# 最终代码
# #主要是为了防止无限循环，加入了检查步骤，检查一个人之前首先确认之前没有检查过他再加入队列中
from collections import deque
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []                        # 这个数组用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:      # 仅当这个人没有被检查过时才检查
            if person_is_seller(person):
                print(person + ' is a manguo seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)         # 将这个人标记为检查过
    return False

# 测试
search('you')