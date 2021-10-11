from resources import *
from math_funcs import *
from random import choice
"""
场景设计模组
制作流程：
    def load_scene_sample(scene):     # 定义加载函数
        scene.set_style(choice(colors))  # 随机进行场景风格化
        scene.set_decorations(decorations)  # 添加装饰
        scene.set_texts(texts)        # 添加文本
        scene.set_bricks(bricks)      # 添加砖块
        scene.set_thorns(thorns)      # 添加尖刺
        scene.set_savers(savers)      # 添加保存点
        scene.set_endings(endings)    # 添加通关点
        def trigger_act_i():
            pass                             # 制作触发器动作函数
        scene.set_triggers(triggers)  # 添加触发器
        scene.set_kid()               # 初始化kid
        scene.append_objects()        # 汇总objects
    scenes.append(Scene(load_scene_sample))     # 将新建场景加到场景list中，将加载函数传给场景，以便随时加载
    
    其中 decorations,texts,bricks,thorns,savers,endings,triggers 为tuple组成的tuple或list
    每个元素tuple需要包含初始化对应实体的必要参数，具体可见resources.py中的scene类的对应接口方法
    具体实例如下
"""

VERSION = '1.5'  # 用于展示的版本号
scenes = []  # 初始一个空场景列表
colors = ['yellow', 'red', 'purple', 'orange', 'grey', 'green', 'cyangreen', 'cyanblue',]

"""------------------------------------SCENE_INIT--------------------------------------"""

def load_scene_init(scene):

    scene.waiting_j = True

    # DECORATIONS
    scene.set_style('purple0')

    scene.set_decorations((
        ('initial_menu', 0, 0),
    ))

    scene.set_texts((
        ("Welcome to", (WIDTH / 2, 70), 'center', 100, 'white'),

        ("I wanna be the dinosaur", (WIDTH / 2, 150), 'center', 50, 'white'),

        # ("Press A/D to move\nPress K to jump", (135, 535), 'left', 24, 'white'),

        ("Press J to continue...", (WIDTH / 2 + 240, 550), 'center', 20, 'white'),
    ))

    # BLOCKS
    scene.set_bricks(
        [(x + 10, 13) for x in range(7)] +
        [(x + 10, 19) for x in range(7)] +
        [(10, x + 14) for x in range(5)] +
        [(16, x + 14) for x in range(5)]
    )

    # LAYOUTS
    scene.set_savers((
        (13, 18, 1, 4),
    ))

    # KID
    scene.set_kid()

    scene.append_objects()

"""-----------------------------------SCENE_START-------------------------------------"""

def load_scene_start(scene):

    # DECORATIONS
    scene.set_style(choice(colors))

    scene.set_decorations((
        ('scene1', 0, 0),
    ))

    scene.set_texts((
        ("Press A/D to move left and right\nPress K for longer or shorter time and for once or twice to get\n\tfamiliar with the sensitivity of jumping\nPress R to go back to the loaded rebirth point when you need\nPress J at flagpole to load or at cup to choose the difficulty", (WIDTH / 2, 120), 'left', 19, 'white'),
        ("EASY", (get_x(5.5), get_y(14)), 'center', 16, 'white'),
        ("NORMAL", (get_x(12), get_y(14)), 'center', 16, 'white'),
        ("HARD", (get_x(17.5), get_y(14)), 'center', 16, 'white')
    ))

    # BLOCKS
    scene.set_bricks(
        [(x + 1, 19) for x in range(24)] +
        [(x + 2, 1) for x in range(24)] +
        [(1, x + 1) for x in range(19)] +
        [(25, x + 2) for x in range(18)] +
        [(x + 2, 9) for x in range(23)] +
        [(x + 2, 15) for x in range(21)]
    )

    # LAYOUTS
    scene.set_savers((
        (3, 18, 1, 4),
        (21, 14, 2, 4)
    ))

    scene.set_endings((
        (4, 14),
        (10, 14),
        (16, 14)
    ))


    def set_dif_1():
        scene.set_difficulty(1)


    def set_dif_2():
        scene.set_difficulty(2)


    def set_dif_3():
        scene.set_difficulty(3)


    scene.set_triggers((
        (4, 14, set_dif_1),
        (10, 14, set_dif_2),
        (16, 14, set_dif_3),
    ))

    # KID
    scene.set_kid()

    scene.append_objects()

"""--------------------------------------SCENE1----------------------------------------"""

def load_scene1(scene):

    # DECORATIONS
    scene.set_style(choice(colors))

    scene.set_decorations((
        ('scene2', 0, 0),
    ))

    # BRICKS
    scene.set_bricks(
        [(x + 1, 19) for x in range(24)] +
        [(x + 2, 1) for x in range(24)] +
        [(1, x + 1) for x in range(19)] +
        [(25, x + 2) for x in range(18)] +
        [(x + 2, 15) for x in range(20)] +
        [(x + 5, 11) for x in range(20)] +
        [(x + 2, 6) for x in range(21)] +
        [
            (7, 2),
            (7, 3),
            (9, 2),
            (9, 3),
            (19, 3),
            (19, 4),
            (19, 5),
            (11, 9),
            (23, 10),
        ]
    )

    # THORNS
    scene.set_thorns((
        (6, 18, 'up'),
        (8, 18, 'up'),
        (10, 18, 'up'),
        (13, 18, 'up'),
        (16, 18, 'up'),
        (19, 17, 'up'),
        (19, 18, 'up'),
        (20, 18, 'up'),
        (22, 15, 'right'),
        (24, 15, 'left'),
        (19, 12, 'down'),
        (18, 14, 'up'),
        (15, 12, 'down'),
        (14, 14, 'up'),
        (13, 12, 'down'),
        (10, 14, 'up'),
        (9, 14, 'up'),
        (8, 14, 'up'),
        (7, 14, 'up'),
        (4, 14, 'up'),
        (2, 12, 'right'),
        (4, 11, 'left'),
        (8, 10, 'up'),
        (8, 7, 'down'),
        (8, 8, 'down'),
        (13, 10, 'up'),
        (13, 9, 'up'),
        (13, 8, 'up'),
        (15, 10, 'up'),
        (15, 7, 'down'),
        (17, 10, 'up'),
        (18, 10, 'up'),
        (19, 10, 'up'),
        (20, 10, 'up'),
        (21, 10, 'up'),
        (18, 7, 'down'),
        (19, 7, 'down'),
        (23, 6, 'right'),
        (17, 2, 'down'),
        (17, 5, 'up'),
        (16, 5, 'up'),
        (15, 5, 'up'),
        (12, 5, 'up'),
        (10, 5, 'up'),
        (8, 5, 'up'),
        (6, 5, 'up'),
        (17, 4, 'up'),
        (10, 3, 'right'),
        (6, 3, 'left')
    ))

    # LAYOUTS
    scene.set_savers((
        (3, 18, 1, 4),
        (21, 14, 2, 1),
        (5, 10, 3, 2),
        (22, 5, 4, 1)
    ))

    scene.set_endings((
        (3, 5),
    ))

    # KID
    scene.set_kid()

    scene.append_objects()

"""--------------------------------------SCENE2----------------------------------------"""

def load_scene2(scene):

    # BACKGOUND
    scene.set_style(choice(colors))

    scene.set_decorations((
        ('scene3', 0, 0),
    ))

    # BRICKS
    scene.set_bricks(
        [(x + 1, 19) for x in range(24)] +
        [(x + 1, 1 ) for x in range(24)] +
        [(1 , y + 1) for y in range(19)] +
        [(25, y + 1) for y in range(19)] +
        [(x + 18, 2 ) for x in range(5)] +
        [(x + 13, 4 ) for x in range(4)] +
        [(x + 19, 5 ) for x in range(4)] +
        [(x + 17, 6 ) for x in range(4)] +
        [(x + 15, 7 ) for x in range(4)] +
        [(x + 13, 8 ) for x in range(6)] +
        [(x + 13, 9 ) for x in range(5)] +
        [(x + 12, 10) for x in range(5)] +
        [(x + 12, 11) for x in range(4)] +
        [(x +  5, 11) for x in range(5)] +
        [(x + 4, 12) for x in range(16)] +
        [(x + 4, 13) for x in range(12)] +
        [(x + 10, 14) for x in range(8)] +
        [(x + 9, 15) for x in range(3)] +
        [(x + 15, 16) for x in range(6)] +
        [
            (24,2),
            (16,3),
            (17,3),
            (9,7),
            (10,7),
            (3,8),
            (4,8),
            (8,8),
            (9,8),
            (7,9),
            (8,9),
            (6,10),
            (7,10),
            (8,10),
            (3,14),
            (4,14),
            (6,14),
            (6,15),
            (3,15),
            (19,14),
            (19,15),
            (21,13),
            (21,14),
            (21,15),
            (23,13),
            (23,14),
            (23,15),
            (12,17),
            (13,17),
            (14,17),
            (8,16),
            (9,16),
            (8,17),
            (8,18),
            (2,18)
        ]
    )

    # THORNS
    scene.set_thorns((
        (18, 3, 'down'),
        (19, 3, 'down'),
        (20, 3, 'down'),
        (21, 3, 'down'),
        (22, 3, 'down'),
        (24, 3, 'left'),
        (24, 4, 'left'),
        (24, 5, 'left'),
        (24, 6, 'left'),
        (24, 7, 'left'),
        (24, 8, 'left'),
        (24, 9, 'left'),
        (24, 10, 'left'),
        (21, 10, 'up'),
        (22, 10, 'up'),
        (23, 10, 'up'),
        (17, 4, 'down'),
        (13, 5, 'down'),
        (14, 5, 'down'),
        (9, 6, 'up'),
        (10, 6, 'up'),
        (7, 7, 'up'),
        (7, 8, 'up'),
        (5, 10, 'up'),
        (3, 12, 'left'),
        (11, 11, 'up'),
        (13, 7, 'up'),
        (3, 18, 'up'),
        (5, 18, 'up'),
        (13, 16, 'up'),
        (19, 11, 'up'),
        (19, 13, 'up'),
        (20, 15, 'up'),
        (22, 15, 'up'),
        (16, 18, 'up'),
        (19, 18, 'up'),
        (21, 18, 'up'),
        (22, 18, 'up'),
        (24, 18, 'up'),
        (21, 6, 'down'),
        (22, 6, 'down')
    ))

    # LAYOUTS
    scene.set_savers((
        (5, 15, 1, 4),
        (10, 9, 2, 1),
        (23, 2, 3, 2),
        (17, 10, 4, 1)
    ))

    scene.set_endings((
        (16, 13),
    ))
    # KID
    scene.set_kid()

    scene.append_objects()

"""--------------------------------------SCENE3----------------------------------------"""

def load_scene3(scene):

    # BACKGOUND
    scene.set_style(choice(colors))

    scene.set_decorations((
        ('scene4', 0, 0),
    ))

    # BRICKS
    scene.set_bricks(
        [(x + 1, 19) for x in range(24)] +
        [(x + 1, 1 ) for x in range(24)] +
        [(1 , y + 1) for y in range(19)] +
        [(25, y + 1) for y in range(19)] +
        [(x + 17, 3) for x in range(6)] +
        [(x + 7, 3) for x in range(2)] +
        [(x + 18, 4) for x in range(2)] +
        [(x + 13, 8) for x in range(3)] +
        [(x + 13, 9) for x in range(3)] +
        [(x + 10, 10) for x in range(13)] +
        [(x + 17, 11) for x in range(3)] +
        [(x + 18, 12) for x in range(3)] +
        [(x + 18, 14) for x in range(5)] +
        [(x + 12, 13) for x in range(4)] +
        [(x + 15, 15) for x in range(9)] +
        [(x + 14, 18) for x in range(3)] +
        [(x + 10, 18) for x in range(3)] +
        [(x + 10, 15) for x in range(4)] +
        [(x + 3, 16) for x in range(3)] +
        [(x + 3, 15) for x in range(4)] +
        [(x + 6, 14) for x in range(5)] +
        [(x + 4, 13) for x in range(6)] +
        [(x + 5, 12) for x in range(3)] +
        [
            (7, 2),
            (5,6),
            (4,7),
            (18,5),
            (14,6),
            (14,7),
            (20,7),
            (19,8),
            (20,8),
            (18,9),
            (19,9),
            (9,8),
            (9,9),
            (10,9),
            (7,10),
            (2,11),
            (3,11),
            (5,11),
            (6,11),
            (10,11),
            (10,12),
            (9,12),
            (4,14),
            (21,13),
            (15,14),
            (12,16),
            (12,17),
            (16,17),
            (21,16),
            (22,16),
            (22,17),
            (23,17)

        ]
    )

    # THORNS
    scene.set_thorns((
        (24, 2, 'left'),
        (24, 3, 'left'),
        (24, 4, 'left'),
        (24, 5, 'left'),
        (24, 6, 'left'),
        (24, 7, 'left'),
        (2, 12, 'down'),
        (2, 13, 'down'),
        (13, 16, 'down'),
        (14, 11, 'down'),
        (15, 11, 'down'),
        (2, 10, 'up'),
        (5, 10, 'up'),
        (6, 10, 'up'),
        (10, 8, 'up'),
        (11, 9, 'up'),
        (12, 9, 'up'),
        (15, 7, 'up'),
        (16, 9, 'up'),
        (17, 9, 'up'),
        (18, 8, 'up'),
        (19, 7, 'up'),
        (21, 7, 'up'),
        (22, 7, 'up'),
        (8, 11, 'up'),
        (8, 12, 'up'),
        (12, 12, 'up'),
        (16, 13, 'up'),
        (16, 14, 'up'),
        (17, 14, 'up'),
        (4, 18, 'up'),
        (5, 18, 'up'),
        (7, 18, 'up'),
        (8, 18, 'up'),
        (9, 18, 'up'),
        (8, 17, 'up'),
        (9, 17, 'up'),
        (15, 17, 'up'),
        (17, 17, 'up'),
        (17, 18, 'up'),
        (19, 17, 'up'),
        (19, 18, 'up'),
        (18, 18, 'up'),
        (20, 18, 'up'),
        (23, 10, 'right'),
        (24, 13, 'left')
    ))

    # LAYOUTS
    scene.set_savers((
        (8, 15, 1, 4),
        (14, 5, 2, 1),
        (24,18, 3, 2),
        (13,18, 4, 1)

    ))

    scene.set_endings((
        (20, 13),
    ))

    # KID
    scene.set_kid()

    scene.append_objects()

"""--------------------------------------SCENE4----------------------------------------"""

def load_scene4(scene):
    scene.set_style(choice(colors))
    # BACKGOUND
    scene.set_decorations((
        ('scene5', 0, 0),
    ))

    # BRICKS
    scene.set_bricks(
        [(x + 9, 1) for x in range(3)] +
        [(x + 7, 3) for x in range(5)] +
        [(13, y + 3) for y in range(3)] +
        [(x + 2, 5) for x in range(7)] +
        [(x + 11, 5) for x in range(2)] +
        [(1, y + 6) for y in range(3)] +
        [(1, y + 12) for y in range(3)] +
        [(x + 8, 10) for x in range(11)] +
        [(7, y + 11) for y in range(3)] +
        [(x + 2, 15) for x in range(6)] +
        [(7, y + 16) for y in range(4)] +
        [(x + 11, 19) for x in range(3)] +
        [(x + 15, 19) for x in range(3)] +
        [(19, y + 1) for y in range(8)] +
        [(x + 20, 5) for x in range(5)] +
        [(25, y + 6) for y in range(3)] +
        [(x + 18, 9) for x in range(3)] +
        [(x + 17, 13) for x in range(2)] +
        [(23, y + 9) for y in range(5)] +
        [(x + 21, 11) for x in range(2)] +
        [(25, y + 12) for y in range(3)] +
        [(10, y + 12) for y in range(5)] +
        [(x + 13, 15) for x in range(12)] +
        [(13, y + 16) for y in range(2)] +
        [(x + 14, 17) for x in range(6)] +
        [(19, y + 18) for y in range(2)] +

        [
            (7, 1),
            (2, 6),
            (2, 14),
            (8, 7),
            (9, 8),
            (9, 9),
            (8, 11),
            (18, 5),
            (24, 6),
            (24, 14),
            (11, 16)

        ]
    )

    # THORNS
    scene.set_thorns((
        (1, 1, 'right'),
        (1, 2, 'right'),
        (1, 3, 'right'),
        (1, 4, 'right'),
        (2, 1, 'down'),
        (3, 1, 'down'),
        (4, 1, 'down'),
        (5, 1, 'down'),
        (6, 1, 'down'),
        (6, 3, 'left'),
        (8, 1, 'down'),
        (9, 5, 'up'),
        (10, 5, 'up'),
        (12, 1, 'down'),
        (13, 1, 'down'),
        (14, 1, 'down'),
        (14, 4, 'up'),
        (15, 4, 'up'),
        (16, 4, 'up'),
        (14, 7, 'right'),
        (15, 7, 'right'),
        (17, 7, 'left'),
        (18, 7, 'left'),
        (16, 9, 'up'),
        (12, 8, 'up'),
        (12, 9, 'up'),
        (1, 9, 'right'),
        (1, 10, 'right'),
        (1, 11, 'right'),
        (3, 12, 'right'),
        (5, 12, 'left'),
        (6, 12, 'left'),
        (4, 14, 'up'),
        (8, 19, 'up'),
        (9, 19, 'up'),
        (10, 19, 'up'),
        (14, 19, 'up'),
        (18, 19, 'up'),
        (12, 14, 'left'),
        (13, 14, 'up'),
        (14, 11, 'left'),
        (15, 11, 'down'),
        (15, 12, 'down'),
        (19, 13, 'right'),
        (20, 12, 'down'),
        (21, 14, 'up'),
        (21, 9, 'right'),
        (23, 8, 'up'),
        (25, 9, 'left'),
        (25, 10, 'left'),
        (24, 13, 'up')
    ))

    # LAYOUTS
    scene.set_savers((
        (2, 2, 1, 4),
        (18, 2, 2, 1),
        (2, 13, 3, 2),
        (23, 14, 4, 1)

    ))

    scene.set_endings((
        (25, 11),
    ))

    # KID
    scene.set_kid()

    scene.append_objects()

"""--------------------------------------SCENE5----------------------------------------"""


def load_scene5(scene):

    # BACKGOUND
    scene.set_style(choice(colors))

    scene.set_decorations((
        ('scene6', 0, 0),
    ))

    # BRICKS
    scene.set_bricks(
        [(x + 15, 19) for x in range(10)] +
        [(x + 6, 15) for x in range(3)] +
        [(14, y + 12) for y in range(5)] +
        [(8, y + 10) for y in range(3)] +
        [(13, x + 8) for x in range(3)] +
        [(x + 23, 12) for x in range(3)] +
        [(x + 5, 7) for x in range(3)] +
        [(x + 9, 7) for x in range(3)] +
        [(17, x + 1) for x in range(4)] +
        [(x + 11, 0) for x in range(6)] +
        [
            (21, 1),
            (13, 2),
            (14, 2),
            (23, 2),
            (8, 3),
            (12, 4),
            (21, 4),
            (24, 4),
            (2, 5),
            (13, 6),
            (16, 5),
            (23, 5),
            (20, 7),
            (22, 7),
            (3, 8),
            (20, 9),
            (22, 9),
            (10, 10),
            (22, 11),
            (7, 12),
            (21, 12),
            (4, 14),
            (11, 14),
            (23, 14),
            (2, 15),
            (18, 15),
            (2, 16),
            (10, 16),
            (11, 16),
            (25, 16),
            (3, 17),
            (13, 17),
            (17, 17),
            (10, 19),
            (11, 19),
            (3, 10),
            (14, 11),
            (19, 10),
            (20, 3),
            (14, 18),
            (13, 7),
            (12, 7),
    ]
    )

    # THORNS
    scene.set_thorns((
        (9, 19, 'left'),
        (11, 18, 'up'),
        (19, 18, 'up'),
        (20, 18, 'up'),
        (21, 18, 'up'),
        (22, 18, 'up'),
        (23, 18, 'up'),
        (16, 17, 'left'),
        (20, 17, 'up'),
        (22, 17, 'up'),
        (17, 16, 'up'),
        (4, 15, 'down'),
        (10, 15, 'up'),
        (11, 15, 'up'),
        (2, 14, 'left'),
        (3, 14, 'left'),
        (7, 14, 'up'),
        (8, 14, 'up'),
        (13, 14, 'left'),
        (18, 14, 'up'),
        (4, 13, 'up'),
        (6, 12, 'left'),
        (9, 12, 'right'),
        (15, 12, 'right'),
        (22, 12, 'down'),
        (7, 11, 'up'),
        (9, 11, 'right'),
        (25, 11, 'left'),
        (20, 10, 'down'),
        (22, 10, 'down'),
        (25, 10, 'left'),
        (14, 9, 'right'),
        (23, 9, 'right'),
        (25, 9, 'left'),
        (4, 8, 'down'),
        (5, 8, 'down'),
        (6, 8, 'down'),
        (7, 8, 'down'),
        (8, 8, 'down'),
        (9, 8, 'down'),
        (10, 8, 'down'),
        (11, 8, 'down'),
        (28, 8, 'right'),
        (20, 8, 'left'),
        (22, 8, 'right'),
        (25, 8, 'left'),
        (8, 7, 'up'),
        (21, 8, 'up'),
        (25, 7, 'left'),
        (2, 6, 'down'),
        (6, 6, 'up'),
        (7, 6, 'up'),
        (9, 6, 'up'),
        (10, 6, 'up'),
        (23, 6, 'down'),
        (2, 4, 'up'),
        (8, 4, 'down'),
        (16, 4, 'up'),
        (23, 3, 'down'),
        (7, 2, 'left'),
        (9, 2, 'right'),
        (21, 2, 'down'),
        (7, 1, 'left'),
        (9, 1, 'right'),
        (13, 5, 'up'),
        (13, 3, 'down'),
        (15, 5, 'left'),
        (16, 6, 'down'),
        (21, 5, 'down'),
        (8, 16, 'down'),
        (8, 17, 'down'),
        (8, 18, 'down'),
        (12, 8, 'down')
    ))

    # LAYOUTS
    scene.set_savers((
        (3, 16, 1, 4),
        (8, 9, 2, 1),
        (11, 6, 3, 2),
        (19, 9, 4, 1),

    ))

    scene.set_endings((
        (23, 11),
    ))

    # KID
    scene.set_kid()

    scene.append_objects()



"""----------------------------------SCENE_TERMINAL------------------------------------"""

def load_scene_terminal(scene):

    scene.need_press_j = True

    # DECORATIONS
    scene.set_style('red0')

    scene.set_decorations((
        ('scene_terminal', 0, 0),
    ))
    scene.set_texts((
        ("Thanks for your enjoying\nMore scenes are coming...\n\nPress J to exit", (500, 130), 'center', 30, 'white'),
        ("I wanna be the dinosaur\nVersion:{}".format(VERSION), (WIDTH / 2, 360), 'center', 40, 'white'),
        ("Contact us: habibzhu@foxmail.com".format(VERSION), (WIDTH / 2, 440), 'center', 25, 'white'),
        ("Difficulty:{}".format({'0':'Cheat', '1':'Easy', '2':'Normal', '3':'Hard'}[str(scene.difficulty)]), (200, 490), 'left', 25, 'red'),
        ("Death:{} times".format(scene.sum_death), (540, 490), 'left', 25, 'red')
    ))

    # BLOCKS
    scene.set_bricks(
        [(x + 2, 9) for x in range(23)] +
        [(x + 2, 18) for x in range(23)] +
        [(2, x + 10) for x in range(8)] +
        [(24, x + 10) for x in range(8)]
    )

    # LETHALS
    scene.set_thorns(
        [(x+2, 8, 'up') for x in range(23)] +
        [(x+2, 19, 'down') for x in range(23)] +
        [(1, x + 9, 'left') for x in range(10)] +
        [(25, x + 9, 'right') for x in range(10)]
    )

    # LAYOUTS
    scene.set_savers((
        (13, 17, 1, 4),
    ))

    # KIDkr
    scene.set_kid()

    scene.append_objects()


"""--------------------------------------SCENES----------------------------------------"""

scenes.append(Scene(load_scene_init))
scenes.append(Scene(load_scene_start))
scenes.append(Scene(load_scene1))
scenes.append(Scene(load_scene2))
scenes.append(Scene(load_scene3))
scenes.append(Scene(load_scene4))
scenes.append(Scene(load_scene5))
scenes.append(Scene(load_scene_terminal))
