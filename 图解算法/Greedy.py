# 贪婪算法：P123
"""
    贪婪算法(贪心算法)是指在对问题进行求解时，在每一步选择中都采取最好或者最优(即最有利)的选择，
        从而希望能够导致结果是最好或者最优的算法。
    贪婪算法所得到的结果往往不是最优的结果(有时候会是最优解)，但是都是相对近似(接近)最优解的结果。

    其基本的解题思路为：
        1.建立数学模型来描述问题
        2.把求解的问题分成若干个子问题
        3.对每一子问题求解，得到子问题的局部最优解
        4.把子问题对应的局部最优解合成原来整个问题的一个近似最优解

    贪婪算法的时间复杂度为 O(n^2)
"""

# 传入一个数组，并转换为集合
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'za'])

# 建立可供选择的广播清单
stations = {} 
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] =  set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# 最终选择的广播台
final_stations = set()

# # 选出一个覆盖最广的州
# best_stations = None
# states_covered = set()      # 包含该广播台覆盖的州
# for station, state_for_station in stations.items():
#     covered = states_needed & state_for_station      # & 计算两者的交集， | 计算两者的并集
#     if len(covered) > len(states_covered):
#         best_stations = station
#         states_covered = covered
#
# states_needed -= states_covered
# final_stations.add(best_stations)

# 循环上面的步骤,直到所有的州都被覆盖：
while states_needed:
    best_stations = None
    states_covered = set()      # 包含该广播台覆盖的州
    for station, state_for_station in stations.items():
        covered = states_needed & state_for_station      # & 计算两者的交集， | 计算两者的并集
        if len(covered) > len(states_covered):
            best_stations = station
            states_covered = covered

    states_needed -= states_covered                     # - 计算两者的差集
    final_stations.add(best_stations)

print(final_stations)