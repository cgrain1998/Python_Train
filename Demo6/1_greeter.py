# todo 这个文件是定义python 函数的

# 2019年5月16日20:25:44


# 函数定义
def fun():
    print("Hello  Python")


# 函数调用
# fun()


# todo  函数  接受 参数

def fun2(name):  # 这个叫形参
    print("Hello," + name)  # 这个叫实参


fun2("World")
print("-------------------")

#  函数可以一次定义，多次调用

print("函数可以一次定义，多次调用,比如下面多次调用  fun2 函数")
fun2("World")
fun2("World")

print("--------------")

# todo  参数定位传递
print("我们命名一个 fun3(name,age) 的函数--> 注意他们的参数！")
print("""
假如我们这样调用  fun3("23","cgrain"),会发生什么？
""")


def fun3(name, age):
    print(name + "已经" + age + "岁了")


fun3("23", "cgrain")
print(" 23已经 cgrain岁了，\n 我的天，这肯定是错误的")
fun3("cgrain", "23")
print("\n这样子才正确的，那我们怎么办？才能按照所想的？")
fun3(name="Cgrain", age="23")
fun3(age="23", name="Cgrain")
print("\n这样子就解决了！")

# todo 函数 设置 默认值！

print("\n函数设置默认值")
print(
    """
    我有一份名单，里面有我认识的，也有我不认识的，认识的
    我知道其性别，不认识的就写未知，然后打印,但是我看了名单，认识的就几个，
    我只写我知道的，不知道的默认未知
    """
)


def fun4(name, sex="未知"):
    if sex == "未知":
        print(name + "的性别我不是特别清楚，请来登记.")
    else:
        print(name + "的性别为：" + sex)


fun4(name="Cgrain", sex="男")  # 默认值将会被你传的形参所替换
fun4(name="cgrain")

print("这就是默认值的好处")

print("-----------")
# todo 函数 返回  简单值

print(
    """
    函数不一定，只能 print()
    还能 返回你所想要的类型的值
    """
)


def fun5(name, sex):
    return name + "是" + sex


name_sex = fun5("Cgrain", "男")
print(name_sex)

# todo 函数 返回  字典

print("---------")
print("函数 返回  字典")


def fun6():
    return {"1": "1", "2": "2"}


print(fun6())

# todo 函数 返回  列表

print("---------")
print("函数 返回  列表")


def fun7():
    return [1, 2, 3, 4, 5]


print(fun7())

# 函数内使用 while

print("\n# 函数内使用 while")


def fun8():
    count = 0
    while count < 5:
        print("---------")
        count += 1


fun8()
