# bicycles.py


# todo Python中  [ ]  --> 表示列表

# todo 1  创建一个列表

P_list = ["cgrain", "Cgrain", "Grain"]
'''上面这个就是列表'''
# 直接打印

print(P_list)

# todo  列表是个有序集合  所以 根据下标可访问元素，tips 大多数编程语言中 下标都是 从 0开始
# 通过下标打印
print(P_list[0])

# todo 通过 另外一种方式显示
print(P_list[-1])  # 打印出倒数第一个

print("# todo 列表 删改查")
# todo 列表 增删改查

list_data = [1, 2, 3, 4, 5, 6]
# 第一步，创建一个空列表

print("修改")
# 修改
list_data[0] = "2"
print(list_data)

print("添加")

list_data.append("NewAdd")
print(list_data)

print("插入")

list_data.insert(0, "NewAdd_top1")
print(list_data)

print("删除")
# todo  使用del 删除  删除指定
del list_data[0]
print(list_data)

# del list_data
# print(list_data)  #不加下标就会全删除
# todo 使用pop 删除  从后往前删除，也可以像del 这样加下标

list_data2 = list_data.pop()
print(list_data)
print(list_data2)

# todo remove   ->根据指定集合内容删除
# 加入你知道集合有什么值，但是不知道下标，就可以使用此方法

list_data.remove(4)  # 删除集合的4元素
print(list_data)



#todo  tips  注意 当你不知道列表元素 有多少个  注意使用len()方法哦


