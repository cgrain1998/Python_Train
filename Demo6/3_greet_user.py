#  函数 传递 列表

def fun1(usernamelists):
    for usernamelist in usernamelists:
        print("Hello:" + usernamelist)


# 函数调用

print("-----函数调用------")
userlists = ["Cgrain", "Web", "Python"]
fun1(userlists)

print("\n-----函数中修改  列表-------")


def fun2(datalists):
    updatelist = []

    while datalists:
        datalist = datalists.pop()
        updatelist.append(datalist)
        print("正在替换：" + datalist)

    print("替换：")
    print(updatelist)


datalists = ["Python", "WebApi", "C#"]

print("原来数据：" + str(datalists))

fun2(datalists)
