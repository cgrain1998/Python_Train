# 2019年5月15日

# todo 主题 ：遍历for 循环打印


data_lists = ["Cgrain", "WebApi", "Python", "C#", ".NET"]

for data_list in data_lists:
    print(data_list + "觉得你的表演太棒了！")
    print(data_list + "说下次还要来！\n")
print("魔术师再一次感谢观众！")

# todo  打印数字
print("打印数字")
for num in range(0, 10):
    print(num, end="\t")

# todo 打印列表
print("打印列表")
list_datas = list(range(1, 4))
print(list_datas)

# todo 列表解析
print("-----列表解析-----")
data_list3 = [value ** 2 for value in range(1, 10)]
print(data_list3)

print("""   -     -  """)


print(min(data_list3))

print(max(data_list3))
print(sum(data_list3))

