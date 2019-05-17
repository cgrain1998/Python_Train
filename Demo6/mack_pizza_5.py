#  todo 主要演示 函数模块引用， 需要使用到 pizza_4.py 文件


# 使用 import  导入 一个模块

import pizza_4

pizza_4.ceshi1()


# 使用 import 导入一个模块的某个方法

from  pizza_4   import  ceshi1  # 不需要加 ()

ceshi1()


# 导入一个模块 然后 重新命名

import   pizza_4 as  p4

p4.ceshi1()


# 导入一个模块  的某个 方法 重新命名

from   pizza_4  import  ceshi1  as  cs1

cs1()


# 导入 某个 模块 所有 函数

from   pizza_4 import  *       # 不建议 这样子使用



#todo 函数  编写 规范

# todo 1  使用小写字母 和下划线

# todo  2   言简意赅 ,别让猜