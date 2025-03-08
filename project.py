#六个房间
rooms = {
        '门厅': {
        'name': '门厅',
        'description': '你身处古堡的阴暗门厅。头顶一盏布满蜘蛛网的吊灯微微摇晃，投下忽明忽暗的光芒。空气中弥漫着潮湿的霉味,脚下是冰冷的大理石地面。北面是一扇沉重的橡木门，门上雕刻着狰狞的怪兽头像，东面则是一条通向黑暗深处的走廊。',
        'items': ['门厅地毯下的纸条(一张陈旧的纸条，似乎是从某本书页上撕下来的，上面潦草地写着 ‘光芒指引方向’。)'],
        'exits': {'北': '大厅', '东': '走廊'}
    },
        '大厅': {
        'name': '大厅',
        'description': '你推开橡木门，进入了古堡的宏伟的大厅。尽管岁月流逝，依稀可见昔日的辉煌。一个巨大的水晶吊灯（虽然已经缺了几盏灯泡）仍然悬挂在高耸的天花板上。彩色玻璃窗阻挡了外界的光线，使得大厅内光线昏暗。南面是你进来的门厅，西面是一扇装饰华丽的木门，通往图书馆，东面则是一道拱形石门，通向餐厅。',
        'items': ['壁炉拨火棍(一根沉重的铁制拨火棍，顶端装饰着狮子头。)'],
        'exits': {'南': '门厅', '西': '图书馆', '东': '餐厅'}
    },
        '走廊': {
        'name': '走廊',
        'description': '你沿着昏暗的走廊前行，脚踩在吱吱作响的木地板上。墙壁上挂着褪色的家族画像，画像中的人物表情模糊不清，仿佛在注视着你。走廊尽头似乎传来微弱的滴水声。西面是门厅。”',
        'items': ['生锈的铁钥匙(一把锈迹斑斑的铁钥匙，看起来年代久远，也许能打开古堡的某扇门。)'],
        'exits': {'西': '门厅'}
    },
        '图书馆': {
        'name': '图书馆',
        'description': '你推开装饰华丽的木门，走进了布满灰尘的图书馆。高耸的书架一直延伸到天花板，上面堆满了布满灰尘的书籍。空气中弥漫着浓重的旧书和皮革的味道，令人昏昏欲睡。阳光透过高窗洒进来，照亮了书架上零星散落的金箔。东面是通往大厅的木门。”',
        'items': ['一本厚重的古书(一本皮面精装的古书，书页已经泛黄，封面上用难以辨认的文字写着书名。翻开书页，里面似乎是关于古堡历史的记载。)'],
        'exits': {'东': '大厅'}
    },
        '餐厅': {
        'name': '餐厅',
        'description': '你穿过拱形石门，来到了宽敞的餐厅。长长的橡木餐桌上布满了厚厚的灰尘，锈迹斑斑的银质餐具散落在桌面上，仿佛一场盛宴突然中断。墙壁上挂着巨大的狩猎场景油画，画布已经开始剥落。西面是通往大厅的拱形石门，北面是一扇破旧的木门，通向厨房。',
        'items': ['餐桌上的银色烛台(一个精致的银色烛台，上面镶嵌着一些宝石，但大部分已经脱落。)'],
        'exits': {'西': '大厅', '北': '厨房'}
    },
        '厨房': {
        'name': '厨房',
        'description': '你推开破旧的木门，进入了阴冷潮湿的厨房。腐烂的气味扑鼻而来，令人作呕。生锈的厨具散落在各处，巨大的壁炉已经冰冷，炉膛里堆满了黑色的灰烬。南面是餐厅。地板中央，你注意到一块不寻常的木板，似乎可以移动，也许是一个隐蔽的活板门，通往地下。',
        'items': ['壁炉旁的火柴(一盒潮湿的火柴，看起来还能用，也许可以点燃什么。),水桶(一个破旧的木水桶，里面积满了浑浊的雨水。)'],
        'exits': {'南': '门厅', '下': 'escape'}
    },
}
#help指令:获取帮助信息
def help():
    print("可用指令：")
    print("help-显示帮助信息")
    print("look-查看当前房间的详细描述")
    print("go[方向]: 向指定方向移动(例如: north, south, east, west, down)")
    print("take[物品名称]: 拾取房间内物品")
    print("inventory: 查看背包中的物品")
    print("quit: 退出游戏")

# look指令:查看当前房间
def look(fangjian):
    print(f"{fangjian['name']}")
    print(fangjian['description'])
    if fangjian['items']:
        print("房间里有:")
        for item in fangjian["items"]:
            print(item)
    else:
        print("房间中没有物品")
    print("您可以往这里走:")
    for direction, title in fangjian["exits"].items():
        print(f"{direction} -> {title}")

#go[方向]指令:移动到其他房间
def go(fx,fangjian):
    for direction,room2 in rooms[fangjian]["exits"].items():
        if room2 == fx:
            print(f"你进入了{room2}")
            return room2
        elif direction == "下" and fx =="down":
            return "down"
    print("此路不通!")
    return fangjian

#take[物品名称]指令:拾取房间内的物品
def take(title,fangjian,beibao):
    wupin1 = rooms[fangjian]["items"]
    for item in wupin1:
        if title in item:
            print(f"你拿起了{item}")
            beibao.append(item)
            wupin1.remove(item)
            return
    print("这里没有东西")

#inventory指令:查看背包
def inventory(beibao):
    if not beibao:
        print("Nothing!")
    else:
        print("你的背包里有：")
        for i in beibao:
            print(i)

#主函数
def main():
    print("欢迎进入神秘的古堡!")
    chushi="门厅"
    beibao1 = []
    look(rooms[chushi])
    tw = True
    while tw:
        control = input("")
        if control == "help":
            help()
        elif control == "look":
            look(rooms[chushi])
        elif control.startswith("go "):
            tw1 = control[3:].strip()
            room2 = go(tw1,chushi)
            chushi = room2
            if room2 == "down":
                print("你逃出了古堡！")
                return None
            else:
                look(rooms[chushi])
        elif control.startswith("take "):
            items = control[5:].strip()
            take(items,chushi,beibao1)
        elif control == "inventory":
            inventory(beibao1)
        elif control == "quit" or "exit":
            tw = False
            print("感谢游玩!再见!")
        else:
            print("请重新输入")

main()