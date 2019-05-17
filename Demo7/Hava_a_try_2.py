# todo 这是 测试！

#  调用随机数 模块
import random

'''
 创建一个 Rstaurant 的类
 init 方法有两个 属性
 restaurant_name  cuisine_type
 创建 一个 describe_restaurant() 的方法和
 open_restaurant()  其中前者 打印出属性的 值
 后者 打印一条 消息
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Hello world  --> 这是 open_restaurant()方法")


# 调用
restaurant = Restaurant("Python", "Good")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print("\n\n\n\n")
'''
创建一个 User 的类  其中 包含 属性 first_name  last_name
还有 用户简介 通常 会存储的几个其他属性  
在类 User 定义 一个edescribe_user()  方法
打印 用户 信息摘要  在定义 一个 greet_user()
它向 用户 发出 个性化 的 问候 
'''


class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
# 扩张 更新， 请 看了 car_3.py 在回顾看这里
        # todo 1 更新一个字段
        self.number_served=0


    def edescribe_user(self):
        usermesage = """
               First_name:{0}
               Last_name:{1}
               age:{2} 
               sex:{3}
        """
        print(usermesage.format(self.first_name, self.last_name, self.age, self.sex))

    # todo 1-1  增加一个方法
    def insert_number(self):
        self.number_served+=1
        print("你是饭店当前吃饭人数的第："+str(self.number_served))


    #        pass  #todo  pass  表示占位   主要作用就是 让代码不报错
    def greet_user(self):
        mess_hell = ["Hello World", "Hello :" + self.first_name, "Hello:" + self.last_name]
        # 用随机数的
        i = random.randint(0, 2)
        print(mess_hell[i])


#  类的使用
user = User("ceshi", "Python", "12", "男")
user.edescribe_user()
user.greet_user()


# todo 1-2 多次调用

user.insert_number()

user.insert_number()

user.insert_number()

user.insert_number()