# region # todo  本次练习主要是使用 列表的方法使用
# endregion
'''
把你想去的地方用列表存储，使用 sorted()排序
使用reverse =True 排序
使用 reverse() 排序
使用sort() 排序
使用 reverse =True
使用 len() 计算你想去的城市个数


'''

print("创建一个列表")
# 我想去的地方
data_list = ["贵州", "北京", "重庆"]
print("原始循序\n")
print(data_list)
# todo 1
print("\n使用sorted()")
print(sorted(data_list))
print("\n再次打印原始数据")
print(data_list)
print("\n使用sorted(reverse=True)排序")
print(sorted(data_list, reverse=True))

# todo 2

print("\n再次打印原始数据")
print(data_list)
print("\n使用 reverse")
data_list.reverse()
print(data_list)

print("\n恢复为原始数据")
data_list.reverse()
print(data_list)

# todo  使用 sort()

data_list.sort()
print("\n使用 sort()")
print(data_list)

print("\n使用 reverse=True")
data_list.sort(reverse=True)
print(data_list)

print("使用len()")
print("我想去", data_list, end="")  # 加end 表示不换行
print("共有", len(data_list), end="个地方想去")

