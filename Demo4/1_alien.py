# todo 字典

#  { }  的就是字典
alien = {"键": "值", "key": "value"}
print("字典 键值队")

print(alien["键"])
print(alien["key"])

#  字典增删改查


# 增加
alien["key1"] = "这是添加字典的值"
print("输出添加操作，显示字典")
print(alien)

# 删除
print("删除")
del alien["key"]
print(alien)

print(" del  字典 是全部删除")

# 修改

alien["键"] = "修改"
print("修改操作 输出字典")
print(alien)

# 查询字典
print("字典查询 ")
print(alien)

# todo 遍历字典
print("==========")

for key in alien:
    print(key + "---")

# 只能把key 输出


# todo 遍历字典  key 与value 都输出 使用items

print("\n遍历 key and value")
for key, value in alien.items():
    print(key + "---" + value)

# 只是遍历出 key  使用  keys() 方法
print("\n# 只是遍历出 key  使用  keys() 方法")
for key in alien.keys():
    print(key)

# 只是要value  使用 values()
print("\n 只是要value  使用 values()")
for value in alien.values():
    print(value)

# 使用 循序排列  demo 2 列表集合练习 用到的 sorted

print("\n使用 循序排列  demo 2 列表集合练习 用到的 sorted")
for key in sorted(alien.keys()):
    print(key)

# 字典 value 重复  元素 筛选  todo  注意  key 绝对 不会 重复，重复的只有 value

# todo  为了好测试， 我们 加多 几个重复的元素

alien["Cgrain"] = "Grain"

alien["Have  a Try"] = "Yes"
alien["cgrain"] = "Grain"
print(alien)

# 现在 print 看看

print("-----分界线------")
for value in alien.values():
    print(value)

print("-----对比------")

for value in set(alien.values()):
    print(value)

# todo 嵌套

# 字典嵌套列表

dirs = {"Key": "1", "data_list": ["num1", "num2"], "Key2": "2"}

print(dirs)

# 列表 嵌套 字典

data_list = ["num", {"key": 1, "key1": 2}, "num"]

print(data_list)

#

data_list2 = [value for value in range(0, 10)]
print(data_list2)
