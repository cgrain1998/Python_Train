# todo


class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        # 初始化
        self.make = make
        self.model = model
        self.year = year
        # todo 1 新增一个 默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''返回整洁的 描述性信息'''
        print("Year:" + str(self.year) + "mack:" + self.make + "model:" + self.model)

    # todo  1-1 创建 一个新方法 来打印他
    def read_odometer(self):
        print("初始值：" + str(self.odometer_reading))

    # todo 2 通过 方法 修改 初始值

    def update_odometer(self, mileage):
        # todo 3 禁止输入 小于 0 的数字
        if mileage < 0:
            print("错误")
        else:
            self.odometer_reading = mileage

    # todo  4 通过方法 增加

    def insert_odometer(self, insert_mileage):
        if insert_mileage > 0:
            self.odometer_reading += insert_mileage


car = Car("audi", "a8", 2017)
car.get_descriptive_name()
# todo 1-2  打印输出
car.read_odometer()

print("""修改""")

# todo 2-1 调用方法 修改

car.update_odometer(-30)

# todo 2-2 打印
car.read_odometer()

print("""增加""")
# todo  4-1  增加

car.insert_odometer(43)

car.read_odometer()

car.insert_odometer(43)
car.read_odometer()

# todo 代码 阅读 循序
# todo 1  --> todo 1-1  --> todo 1-2  一步一步看 ...
