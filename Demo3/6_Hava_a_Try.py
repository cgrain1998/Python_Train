# todo 2019年5月15日
# 这是练习
# todo 个人网站  https://blog.cgrain.top

# if 练习

print(" \nif 练习")
name = "Cgrain"

if name == "Cgrain":
    print("Hello," + name, end="\n")

# if ...else
print(" \nif... else 练习")

if name == "cgrain":
    print("Hello," + name)
else:
    print("Sorry," + name)

# if elif else

print(" \nif... elif else 练习")
if name == "grain":
    print("Hello" + name)
elif name == "Cgrain":
    print("Haha," + name)
else:
    print("Sorry" + name)

# if and  列表
print("\n if and  列表")
data_lists = ["Cgrain", "WebApi", "Python", "奇妙能力歌", "易燃易爆炸"]
demo_ = "Python"
if len(data_lists) > 0:
    if demo_ in data_lists:
        print("Hello," + demo_)
else:
    print("列表为空")

# for  and  if and 列表

print("# for  and  if and 列表")
if len(data_lists) > 0:
    for data_lists in data_lists:
        if demo_ in data_lists:
            print(demo_)
else:
    print("列表为空")


print("多个列表")
# 多个列表 and  for  and if
# data_list_2s 的数据 看看 data_list_1s 有木有
# todo 发现数据真难弄， 复制一下，在改一下
data_list_1s = ["Cgrain1", "WebApi2", "Python1", "奇妙能力歌2", "易燃易爆炸1"]
data_list_2s = ["Cgrain2", "WebApi2", "Python2", "奇妙能力歌2", "易燃易爆炸2"]

for data_list_2 in data_list_2s:
    if data_list_2 in data_list_1s:
        print(data_list_2+"有数据")
    else:
        print(data_list_2+"无数据")
