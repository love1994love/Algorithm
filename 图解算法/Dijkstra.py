# 狄克斯特拉算法：P108
"""
    广度优先算法解决的是段数最少的路径，而狄克斯特拉则是找出最快的路径
    对比两者，可以发现，狄克斯特拉算法是加权了的广度优先算法，找出的是总权重最小的路径
    狄克斯特拉算法包含四个步骤：
        1、找出“最便宜”的节点，即可在最短时间到达的节点
        2、对于该节点的邻居，检查是否有前往它们的更短的路径，如果有，就跟新其开销
        3、重复这个过程，直到对图中的每个节点都这样做了
        4、计算最终路径

    计算非加权图中的最短路径，可使用广度优先搜索，计算加权图中的最短路径，可使用狄克斯特拉算法
    狄克斯特拉算法只适用于有向但是无环(无环图就是双向图)的图，且不能包含负权边的图

    狄克斯特拉算法的时间复杂度为 O(n^2)
"""

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# print(graph['start'].items())   # dict_items([('a', 6), ('b', 2)])

# 添加其他点及其邻居
graph['a'] = {}
graph['a']['final'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['final'] = 5

graph['final'] = {}      # 终点没有任何邻居

# print(graph)
# dict_items([('a', 6), ('b', 2)])
# {'start': {'a': 6, 'b': 2}, 'a': {'final': 1}, 'b': {'a': 3, 'final': 5}, 'final': {}}

# 创建开销表
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['final'] = infinity

# 存储父节点的散列表
parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['final'] = None

# 创建一个数组用于记录处理过的节点
processed = []

# 算法实现
'''

            流程图
                    1、只要还有要处理的节点
                    2、获取离起点最近的节点
                    3、更新其邻居的开销
                    4、如果有邻居的开销被更新，同时更新其父节点
                    5、将该节点标记为处理过，然后返回第一步

'''

# 找出开销最低的节点
def find_lower_cost_node(costs):
    lowerest_cost = float('inf')
    lowerest_node = None
    for node in costs:      # 遍历所有节点
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过
        if cost < lowerest_cost and node not in processed:
            lowerest_cost = cost
            lowerest_node = node        # 将其视为开销最低的点
    return lowerest_node

# 在未处理的节点中找出开销最小的节点
node = find_lower_cost_node(costs)
while node is not None:             # 该while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():      # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:     # 如果经当前节点前往该邻居更近
            costs[n] = new_cost     # 就更新该邻居的开销
            parents[n] = node       # 同时将该邻居的父节点设置为当前节点
    processed.append(node)          # 将当前节点标记为处理过
    node = find_lower_cost_node(costs)      # 找出接下来要处理的节点，并循环

print(parents)      # start -> b -> a -> final
