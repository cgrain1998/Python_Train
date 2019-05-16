# 2019年5月15日


# todo 切片  截取  列表部分元素

player = ["WebApi", "Python", "C#", ".NET", "Cgrain", "Whatarey"]

print("player[:3]")
print(player[:3])

print("player[1:3]")
print(player[1:3])

print("player[1:]")
print(player[1:])

print("player[:]  -> 复制列表功能")
players = player[:]

player.append("小半")
players.append("光")
print("player"+str(player))

print("players"+str(players))
