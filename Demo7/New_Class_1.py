# todo 这个模块 我们 是 创建与使用类！！

# 创建 类 和方法 差不多， 但是  一个 是用 class 一个是用 def
# class 创建类 时， 第一个字母都是大写 ，而方法 都是小写

mes = '''
  面向对象编程师最有效的软件编写方法之一。
\n  背景：
 对于大多数狗而言， 他们都会有 年龄，性别
 
 他们都会叫 和跑

'''


# 类的定义 如下：

class Dog():
    def __init__(self, age, sex):  # 这是 类的 默认方法
        self.age = age
        self.sex = sex
        # 定义属性

    def jiao(self):
        print("我是一只{0}狗,我今年{1},我会叫".format(self.sex, self.age))
        # pass

    def pao(self):
        print("我会跑")
        # pass


# 调用  由于 你传参数了 所以 需要 你传参数  与函数类似！
dog=Dog("2","m")
#dog.jiao()
dog.pao()
print(dog.age)