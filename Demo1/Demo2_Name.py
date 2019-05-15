# TODO 今天是学习字符串


name = 'cgrain'

print(name.title())  # todo 他会 自动转换大小写

name2 = "' leixiaoxiao  '"
print(name2.title())  # todo  符合一定规则的转换

# upprt 全部转换为大写
# lower 全部转换为小写

name3 = """
 Hello  world  !  
 
"""

print("这是转换为大写" + name3.upper())
print("这是转换为小写" + name3.lower())

name4 = '  Cgrain  '
# name4_data = name4.rstrip()
print(name4)
print(name4.lstrip())  # 删除前面空白
print(name4.strip())  # 删除 前后空白
print(name4.rstrip())  # 删除字符尾的 空白

# TODO  主要想说明的几点是
# TODO  1  Python 命名变量不需要自己自定义类型
# Todo  2 """ """ 与 ''' '''  或者说
# Todo  在Python 中 单引号，双引号  价值一样  ''  与''' ''' 的意义 是'' 只能一行显示，不能换行，而 '''''' 则可以多行显示，"" 与""""""原理一样  Demo3会讲这个
