# -----

# 2019年5月14日


# todo  需要了解列表中一些方法的使用

print("创建一个列表")
data_list = ["奇妙能力歌", "易燃易爆炸", "种种", "少年时代心目中的英雄", "光"]
print("列表 原始状态\n")
print(data_list)
# todo sort()   永久改变 列表循序
data_list.sort()
print("====使用 sort()方法之后=====\n")
print(data_list)
data_list.sort(reverse=True)  # 相反循序排列
print(data_list)

print("====上面是使用sort()排序===")

print("====下面是使用sorted()排序===\n")
# todo  sortde()  临时排序

data_list2=["奇妙能力歌", "易燃易爆炸", "种种", "少年时代心目中的英雄", "光"]
print("原始列表循序")
print(data_list2)
print("=====使用sorted()=====\n")
print(sorted(data_list2))

print("恢复初始列表\n")
print(data_list2)


print("  反转打印\n")
#  todo  反转打印
print("  列表初始\n")

data_list3=["奇妙能力歌", "易燃易爆炸", "种种", "少年时代心目中的英雄", "光"]

print(data_list3)
data_list3.reverse()  # todo reverse()也是永久性的，使用方法和 sort 一样，但是只需要再来一次reverse 又可以返回原来列表循序
print(data_list3)

print(" 反转复原\n")
data_list3.reverse()
print(data_list3)

# todo 查看列表长度
print(" 查看列表长度 ")
print(len(data_list3))




