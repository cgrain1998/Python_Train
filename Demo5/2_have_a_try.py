# 2019年5月16日18:02:50


#  todo  列表值移动  使用 pop()-->Demo2文件的 1_列表.py文件;
#  todo 使用pop 删除  从后往前删除，也可以像del 这样加下标

data_list1 = ["cgrain", "cgrain2", "crain3", "21a4", "5s"]
data_list2 = []

print("data_list1列表：" + str(data_list1))
print("data_list2原来列表：" + str(data_list2))
while data_list1:  # 列表 元素会逐渐为空~
    data_list1_pop = data_list1.pop()
    print("正在移动：" + str(data_list1_pop))
    data_list2.append(data_list1_pop)
print("data_list2转移之后：" + str(data_list2))

# todo if  you could visit on place in the world where would you go?
# todo 如果你能去世界的某个地方，你会去哪里？
print("todo if  you could visit on place in the world where would you go?")

data_list3 = []

Configs = True

while Configs:
    print("if  you could visit on place in the world where would you go?Please  input:")
    print("如果你能去世界的某个地方，你会去哪里？请输入：")
    city = input()
    data_list3.append(city)
    print("Whether to continue，(y/n)？")
    print(" 是否继续？(y/n)")
    Config_y_n = input()
    if Config_y_n == "n":
        Configs = False
        for i in range(1, 4):
            print("正在自动生成" + "." * i)

        print("你所想去的地方有：" + str(data_list3))
    print("\n")
