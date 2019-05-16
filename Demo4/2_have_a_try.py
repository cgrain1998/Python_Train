
# todo 这个文件 是 字典 的练习 题目

# 2019年5月15日

# todo  创建 多个 动物 字典， 存放 动物姓名 与 主人名字， 并打印出啦,重要代码注意别复制


Dog_dic ={"Dog1":"xiao"}
Cat_dic={"Cat1":"xiaoer"}
Pig_dic={"Pig1":"xiaosan"}

for key,value in Dog_dic.items():
    print(key+"的主人是："+value)


for key,value  in  Cat_dic.items():
    print(key+"的主人是："+value)


for  key,value  in Pig_dic.items():
    print(key+"的主人是："+value)

# ----------
print("---------------")

favorite_places={
    "xiaoming":["湖南","北京","杭州"],
    "xiaohon": ["郴州", "澳门", "广州"],
    "xiaohei": ["上海", "湖北", "杭州"],
}

for key,value in favorite_places.items():
    print(key+"喜欢去："+str(value))


# todo 字典 添加， 修改， 需要 与用户交互，所以。。。 你懂的