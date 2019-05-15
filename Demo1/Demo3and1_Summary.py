# todo 1 将用户名字存在一个变量，消息存在另外一个变量，然后拼接

# todo 1.1

name1 = "Cgrain"
mess1 = "是一个优秀的男孩子，怎么还没有女朋友？"
print(name1 + mess1)

# todo  2 将 Cgrain is a good boy. Why don't he have a girlfriend? 存进一个变量，在以小写，大写，首字母大写的方式输出

# todo 2.2

mess2 = "Cgrain is a good boy. Why don't he have a Girlfriend?"
print("首字母大写显示：->" + mess2.title())  # 首字母大写  需要用到 titie()
print("字母全部大写显示：->" + mess2.upper())  # 全部大写
print("全部小写显示：->" + mess2.lower())  # 全部小写

# todo 3  写下  人生苦短，我爱Python 并且写上你的名字
# todo 格式类似   "人生苦短，我爱Python" - Cgrain

# todo  3.3

mess3 = '"人生苦短，我爱Python"'
name3 = ' cgrain'
print(mess3 + "\t-" + name3.title())

# todo 4  将 ' cgrain  ' 打印出来，并且去除多余的空白+首字母大写

# todo 4.4

name4 = ' cgrain '
print("对比--" + name4 + "对比")

print("前面没空格--" + name4.lstrip().title() + "--后面有空格")
print("前面没空格--" + name4.strip().title() + "--后面没空格")
print("前面有空格--" + name4.rstrip().title() + "--后面没空格")

print("\n")
print("\n")
print("\n")
print("\n")

print("==========分界线==============")
name5 = """Cgrain """  # 注意是这个要消除
name6 = "Cgrain"

print("- 空白内容前面--" + name5 + "--空白内容后面-", end="\n")
print("-空白内容前面--" + name5.strip() + "--空白内容后面-", end="\n")

print("-空白内容前面--" + name5.rstrip() + "--空白内容后面-", end="\n")

print("-空白内容前面--" + name5.lstrip() + "--空白内容后面-", end="")
