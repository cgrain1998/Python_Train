#region   练习
# 1 创建一个列表
# 存储几个数值，打印出来
#
# 2
# 修改 其中一个数值为 XX ，比如 “Cgrain”
#
# 3
# 在添加一个数值  比如 “ 光 ”
# 3.1 可以添加到第一个，最后一个，或者中间位置
# 在打印出来
#
# 4 删除 一个数值
#
#
# 5 删除全部
#endregion

#region   都是第一个任务

#endtrgion
print('创建')
# todo 1 创建一个列表  存储几个数值，打印出来

name_list = ["小半", "种种", "奇妙能力歌", "易燃易爆炸"]
print(name_list)
print('修改')
# todo 2 修改 其中一个数值为 ，比如 “Cgrain”

# name_list[0]="Cgrain"  #修改二选一
name_list[-1] = "Cgrain"
print(name_list)

print('添加')
# todo 3

'''
在添加一个数值  比如 “ 光 ”
3.1 可以插入到第一个，最后一个，或者中间位置
在打印出来
'''
name_list.append("光")  # 追加到最后
print(name_list)

name_list.insert(0, "光0")
print(name_list)
# 中间 是 相对的~

# todo 4 删除 一个数值
print('删除')
del name_list[0]

print(name_list)

print('删除2')

name_list2=name_list.pop()
print(name_list)
print(name_list2)


print("删除3")
name_list.remove('小半')
print(name_list)
print("删除全部")
del   name_list

print(name_list)
