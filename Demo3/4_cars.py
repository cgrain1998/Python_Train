# todo  2019年5月15日

# 条件测试


data_lists = ["cgrain", "webapi", "c#", ".net"]

# todo 下面 这段代码 是循环 出来 datalist  然后 if 判断 有没有.net 如果有 则全大写，否则第一个字母大写
for data_list in data_lists:
    if ".net" in data_list:
        print(data_list.upper())
    else:
        print(data_list.title())
# 这里早早的用到了 if （if是下一个py文件才讲）
# 本文件主要是认识条件判断  如下：

# todo  条件判断

print("\n==")
#  ==  相等

demo1 = 111

print(demo1 == 111)

print("！=")
# !=  不等于
print(demo1 != 111)

print("and")
# and 多个条件都必须满足

print(demo1 == 111 and demo1 != 0)

print("or")
#  or  只要满足其中一个条件即可
print(demo1 == 111 or demo1 > 0)

print("in")
# 判断 是否包含
demo2 = demo1 in data_lists
print(demo2)
