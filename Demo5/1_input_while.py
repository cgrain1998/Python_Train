# todo 本文件  使用 input() 接受 用户输入


message = input("输入你想说的话")

print(message)

# todo     demo2
print("\n\n\n\n -----------")
num1 = int(input("输入一个数字"))
if num1 > 10:
    print("Hello world")

else:
    print("Hello Python")

print("\n\n===========")

print("请输入一个数字：")
num2 = int(input())

if num2 % 2 == 0:
    print("这是一个偶数")
else:
    print("这是一个奇数")

# while 循环

print("\n\n\n 请输入一个值：")
message = input()
count = 0
while count < 5:
    print("你输入的是：" + message)
    count += 1

# 选择退出循环 使用 break

while True:
    print("请输入一个你觉得最帅的男人的名字：")
    name = input()
    if name == "Cgrain" or name == "cgrain":
        print("已经退出")
        break;
    print("您输入的是：" + name + "\n (tips:输入Cgrain 或者 cgrain 可退出)")

# while 跳出 本次循环，

while True:
    print("陈粒是我女神，对吗？(输入 Y/N or y/n)")
    input_s = input()
    if input_s == "Y" or input_s == "y":
        print("好哒！")
        break
    if input_s == "N" or input_s == "n":
        print("再给你一次机会！\n")
        continue
    else:
        print("嗯???\n")

# 使用 标志


Bools = True

while Bools:
    print("摸摸你的良心，我帅不？(y/n)")
    input_s1 = input()
    if input_s1 == "y":
        print("猜中l！")
        Bools = False


    else:
        print("造反？(不输入y 不给出！！)")

# 使用 while 输入值到字典

print("\n\n  while+ 字典")

dir_data = {}
configs = True

while configs:
    print("请输入科目：")
    Subject = input()
    print("请输入科目成绩：")
    dir_data[Subject] = input()
    print("是否继续输入？（y/n）")
    config_input = input()
    if config_input == "n":
        configs = False
        
    print("是否查询字典？(y/n)")
    config_select = input()
    if config_select == "y":
        print(dir_data)
