# 2019年5月16日

'''
编写一个 名为 make_album()的函数，他创建一个描述音乐专辑的字典，
这个函数u应该接受歌手的名字和专辑名，并返回一个包含这两项信息的字典
调用，并打印返回值，
给函数  make_album() 添加一个可选参数，存储专辑包含的歌曲数
如果  有歌曲数目，则添加到字典，打印出来，否则不打印
'''


def make_album(name, namemake, count=0):
    music_dirs = {}
    music_dirs[name] = namemake
    # print(music_dirs)
    if count > 0:

        music_dirs[count] = count
        print("歌手:{0}\n歌曲:{1}\n歌曲数:{2}".format(
            name,
            music_dirs[name],

            str(count)))
    else:
        for key, value in music_dirs.items():
            print("歌手:" + str(key) + "\n歌曲:" + str(value))


# 函数 调用
make_album("陈粒", "奇妙能力歌")
make_album("陈粒2", "光")
make_album("陈粒3", "种种")
make_album("陈粒4", "1q", count=2)

# todo 在这里， 我遇到了一个问题 就是没有把  字典 的组成这个 概念 弄清楚
# todo  歌手 music_dirs[name]  歌曲 music_dirs[namemake], 然后一直报错
# todo 突然顿悟  字典 是 key- value   ....  music_dirs[name]
#  todo 不就是存储歌曲的嘛？至于music_dirs[namemake] 这是什么鬼


# todo 2

'''
使用 while 循环 让用户输入，歌手，歌曲，歌曲数（默认为0），
直到用户停止输入打印出用户所输入的信息
'''

print("\n----------------")


def make_albums(musiccount=0):
    config = True
    # config_input = True
    dir_Music = {}
    while config:
        print("请输入你喜欢的歌手名字:")
        musicname = input()
        print(dir_Music.items())
        # 注意Key 不能重复
        for key in dir_Music.keys():
            if musicname in str(key):
                print("此歌手已经存在,请换一个：")
                break  # 使用 break  退出 这个 for 循环， ~~ 这里 我也 讲不清楚
                # continue  貌似没用
                # config_input = False   也可以使用 标志
        # if config_input:
        print("请输入歌手的代表歌曲：")
        music = input()
        dir_Music[musicname] = music

        if musiccount == 0:
            print("请输入此歌曲你所拥有不同歌手唱的歌曲数：")
            dic_musiccount = int(input())
            dir_Music[musicname + music] = dic_musiccount
        else:
            dir_Music[musicname + music] = musiccount

        print("是否继续输入?(y/n)")
        configs = input()
        if configs == "n":
            config = False
            print("""你所输入的值有：
                     
                     歌手:{0}
                     歌曲：{1}
                     歌曲数：{2}
            """.format(musicname, dir_Music[musicname], str(dir_Music[musicname + music])))


# make_albums()

make_albums(5)
