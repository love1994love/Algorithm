# 递归：P25
"""
    每个递归函数都有两个部分：基线条件(base case) 和 递归条件(recursive case)
    递归条件指的是函数自己调用自己，基线条件则指的是函数不再调用自己，从而避免形成无限循环
"""
# 从盒子中找钥匙
# # 方法一: 伪代码
# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(tem)
#             elif item.is_a_key():
#                 print("found the key")

# # 方法二：伪代码
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print("found the key")

# 测试
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye.")