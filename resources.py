from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds
#import pgzrun
from math import sqrt
from math_funcs import *
from pkg_resources.extern import packaging

# 方块尺寸
SIZE_X = 30
SIZE_Y = 30
# 方块坐标尺寸
N_X = 25
N_Y = 19
# 像素坐标尺寸
WIDTH = SIZE_X * N_X
HEIGHT = SIZE_Y * N_Y
# KID的运动参数
MAXIMUM_VELOCITY_X = 2
JUMP_INIT_VELOCITY = 3
JUMP_ACCELERATION = 0.3
ACCELERATING_PERIOD = 10
# 跳跃的反弹系数
COEFFICIENT_OF_RESTITUTION = 0.5
# 重力加速度
GRAVITY = 0.2
# KID碰撞半径
RADIUS_OF_KID = 5

class Actors(object):
    """Actor类作人物和子弹等可动物体父类

    :param image_name 外部素材图片文件名
    :param init_x, init_y 初始位置的方块坐标
    :param shape 碰撞箱形状

    """
    def __init__(self, image_name, init_x, init_y):
        self.x_velocity = 0
        self.y_velocity = 0
        self.shape = ''
        self.act = Actor(image_name, (init_x, init_y))


class Kid(Actors):
    """
    Kid类 用户操纵人物的单实例类

    :param jumping,jumped,has_jumped,jump1,jump1 用于实现可长按跳跃与二段跳跃算法的相关变量
    :param gravity 实现重力效果
    :param visible 可见性用于处理死亡事件
    :param rebirth_location 重生点用于处理存档、复活事件
    :param shape kid的碰撞箱形状为圆形
    :param radius radius为碰撞箱圆半径
    :param x_image, y_image 用于处理kid贴图
    """
    def __init__(self, image_name, init_x, init_y):
        """初始化实例"""

        super().__init__(image_name, init_x, init_y)
        self.visible = True
        self.rebirth_location = 1
        self.gravity = GRAVITY
        self.shape = 'circle'
        self.radius = RADIUS_OF_KID
        self.jumping = False
        self.jump1 = 0
        self.jump2 = 0
        self.jumped = False
        self.has_junmped = False
        self.x_image = 'right'
        self.y_image = 'stand'

    def move_x(self, scene):
        """处理左右移动事件"""

        self.layout_check(scene)
        if keyboard.d and not self.block_check('right', scene):
            self.x_velocity = MAXIMUM_VELOCITY_X
        elif keyboard.a and not self.block_check('left', scene):
            self.x_velocity = -MAXIMUM_VELOCITY_X
        else:
            self.x_velocity = 0
        self.act.x += self.x_velocity

    def jump(self, scene):
        """配合move_y处理跳跃事件"""

        if self.block_check('up', scene):
            self.y_velocity = -COEFFICIENT_OF_RESTITUTION * self.y_velocity
        if keyboard.k and self.jump1 == 0:
            self.y_velocity = -JUMP_INIT_VELOCITY
            self.jump1 += 1
            self.jumping = True
        if keyboard.k and self.jump1 != 0 and self.jump2 == 0:
            self.jump1 += 1
            if self.jump1 < ACCELERATING_PERIOD:
                self.y_velocity -= JUMP_ACCELERATION
        if not keyboard.k and self.jump1 != 0:
            self.jumped = True
        if keyboard.k and self.jumped and self.jump2 == 0:
            self.y_velocity = -JUMP_INIT_VELOCITY
            self.jump2 += 1
        if keyboard.k and self.jumped and self.jump2 != 0:
            self.jump2 += 1
            if self.jump2 < ACCELERATING_PERIOD:
                self.y_velocity -= JUMP_ACCELERATION
        if not keyboard.k and self.jump2 != 0:
            self.has_junmped = True
        if self.jump_check(scene) and self.jumped:
            self.jumped = False
            self.has_junmped = False
            self.jumping = False
            self.jump1 = 0
            self.jump2 = 0

    def fall(self, scene):
        """配合move_y处理重力下落"""

        if self.block_check('down', scene):
            self.y_velocity = 0
        else:
            self.y_velocity += self.gravity

    def move_y(self):
        """配合jumping, fall实现跳跃和重力"""

        self.act.y += self.y_velocity

    def image_refresh(self):
        """根据kid的运动方向刷新贴图"""

        if self.x_velocity > 0:
            self.x_image = 'right'
        elif self.x_velocity < 0:
            self.x_image = 'left'
        if self.y_velocity == 0:
            self.y_image = 'stand'
        elif self.y_velocity > 0:
            self.y_image = 'jump'
        elif self.y_velocity < 0:
            self.y_image = 'fall'

        self.act.image = self.y_image + self.x_image

    def shoot(self):
        """实现kid的射击动作"""
        pass

    def die(self, scene):
        """处理死亡事件:碰刺或者掉出界面"""
        if (self.lethal_check(scene) or self.act.y > 570)and not scene.blackcurtain:
            scene.death += 1
            sounds.diesound.play()
            self.visible = False
            scene.texts.append(Text("Press R to retry!", center=(WIDTH / 2, HEIGHT / 2 + 150),
                         fontsize=30, color='white'))
            scene.texts.append(Text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2 - 100),
                                    fontsize=100, color='white'))
            scene.blackcurtain = True
        if keyboard.r:
            if scene.blackcurtain:
                for i in range(len(scene.texts)):
                    scene.texts.pop()
                scene.blackcurtain = False
            self.visible = True
            self.goback_rebirth(scene)

    def goback_rebirth(self, scene):
        """处理复活事件"""

        self.act.x = scene.savers[self.rebirth_location - 1].act.x
        self.act.y = scene.savers[self.rebirth_location - 1].act.y

    def jump_check(self, scene):
        """更新跳跃条件"""

        for obj in scene.blocks:
            if isinstance(obj, Block) and obj.jumpable:
                delta_x = obj.act.x - self.act.x
                delta_y = obj.act.y - self.act.y
                delta_x0 = self.radius + obj.size_x / 2
                delta_y0 = self.radius + obj.size_y / 2
                if 0 < delta_y <= delta_y0 and abs(delta_x) < delta_x0:
                    return True
        return False

    def block_check(self, direction, scene):
        """为掉落、跳跃等事件服务的方块碰撞检测函数"""

        for obj in scene.blocks:
            if self.collide_check(obj, direction):
                return True
        return False

    def lethal_check(self, scene):
        """死亡物碰撞检测事件"""

        for obj in scene.lethals:
            if self.collide_check(obj, None):
                return True
        return False

    def layout_check(self, scene):
        """布局物块的碰撞检测"""

        for obj in scene.layouts:
                if self.act.colliderect(obj.act) and keyboard.j:
                    if isinstance(obj, Saver) and obj.visible == True:
                        obj.action(self, scene)
                    if isinstance(obj, Ending):
                        obj.action(scene)
                    if isinstance(obj, Trigger):
                        obj.action()

    def collide_check(self, obj, direction):
        """为方块碰撞检测，死亡物碰撞检测提供的不同形状物体的碰撞检测算法"""

        collide = False
        if obj.shape == 'rectangle' and obj.collidable:
            delta_x = obj.act.x - self.act.x
            delta_y = obj.act.y - self.act.y
            delta_x0 = self.radius + obj.size_x / 2
            delta_y0 = self.radius + obj.size_y / 2
            if direction == "right" and 0 < delta_x <= delta_x0 and abs(delta_y) < delta_y0:
                if abs(delta_x) > abs(delta_y):
                    self.act.x = obj.act.x - delta_x0
                collide = True
            if direction == 'left' and 0 < -delta_x <= delta_x0 and abs(delta_y) < delta_y0:
                if abs(delta_x) > abs(delta_y):
                    self.act.x = obj.act.x + delta_x0
                collide = True
            if direction == 'down' and 0 < delta_y <= delta_y0 and abs(delta_x) < delta_x0:
                if abs(delta_x / delta_y) < 1:
                    self.act.y = obj.act.y - delta_y0
                collide = True
            if direction == 'up' and 0 < -delta_y <= delta_y0 and abs(delta_x) < delta_x0:
                if abs(delta_x / delta_y) < 1:
                    self.act.y = obj.act.y + delta_y0
                collide = True

        if obj.shape == 'triangle':
            collide = is_circle_intersect_triangle(self.act.x, self.act.y, self.radius,
                                                obj.x1, obj.y1, obj.x2, obj.y2, obj.x3, obj.y3)
        return collide


class Bullet(Actors):
    """子弹类，尚未实现"""
    def __init__(self, image_name, init_x, init_y, direction):
        super().__init__(image_name, init_x, init_y)
        self.direction = direction

    def move(self):
        pass

    def perish(self):
        pass


class Objects(object):
    """物块、致死物、布局物的父类

    :param image_name 外部素材图片文件名
    :param init_x, init_y 初始位置的方块坐标

    """
    def __init__(self, image_name, init_x, init_y):
        self.act = Actor(image_name, (init_x, init_y))
        self.shape = ''
        self.collidable = True
        self.jumpable = True
        self.lethal = False


class Block(Objects):
    """可以踩踏 不能穿过 不致死的物块类，做父类"""

    def __init__(self, image_name, init_x, init_y):
        super().__init__(image_name, init_x, init_y)
        self.collidable = True
        self.jumpable = True
        self.lethal = False
        self.size_x = 0
        self.size_y = 0


class Brick(Block):
    """最一般的标准1×1砖块"""

    def __init__(self, image_name, init_x, init_y):
        super().__init__(image_name, init_x, init_y)
        self.shape = 'rectangle'
        self.size_x = 30
        self.size_y = 30


class Board(Block):
    """会移动的板子，尚未实现"""
    pass


class Shattered_brick:
    """踩踏后会碎裂的砖块，尚未实现"""
    pass


class Lethal(Objects):
    """致死物的父类"""
    def __init__(self, image_name, init_x, init_y):
        super().__init__(image_name, init_x, init_y)
        self.lethal = True


class Thorn(Lethal):
    """最一般的致死物尖刺

    :param x1, y1, x2, y2, x3, y3 为圆形与三角形碰撞检测留下的三个顶点坐标参数

    """

    def __init__(self, image_name, init_x, init_y, direction='up'):
        """根据刺的方向对刺的图片素材和顶点坐标做初始化"""

        super().__init__(image_name, init_x, init_y)
        self.shape = 'triangle'
        if direction == 'up':
            self.act.image = self.act.image + 'up'
            self.x1 = init_x
            self.y1 = init_y - 10 * sqrt(3)
            self.x2 = init_x - 15
            self.y2 = init_y + 5 * sqrt(3)
            self.x3 = init_x + 15
            self.y3 = init_y + 5 * sqrt(3)
        elif direction == 'down':
            self.act.image = self.act.image + 'down'
            self.x1 = init_x
            self.y1 = init_y + 10 * sqrt(3)
            self.x2 = init_x - 15
            self.y2 = init_y - 5 * sqrt(3)
            self.x3 = init_x + 15
            self.y3 = init_y - 5 * sqrt(3)
        elif direction == 'left':
            self.act.image = self.act.image + 'left'
            self.x1 = init_x - 10 * sqrt(3)
            self.y1 = init_y
            self.x2 = init_x + 5 * sqrt(3)
            self.y2 = init_y + 15
            self.x3 = init_x + 5 * sqrt(3)
            self.y3 = init_y - 15
        elif direction == 'right':
            self.act.image = self.act.image + 'right'
            self.x1 = init_x + 10 * sqrt(3)
            self.y1 = init_y
            self.x2 = init_x - 5 * sqrt(3)
            self.y2 = init_y - 15
            self.x3 = init_x - 5 * sqrt(3)
            self.y3 = init_y + 15


class Apple(Lethal):
    """致死物苹果，尚未实现"""
    pass


class Dart(Lethal):
    """致死物忍者标，尚未实现"""
    pass


class Vine(Objects):
    """可刷新跳跃的藤蔓，尚未实现"""
    pass


class Water(Objects):
    """可以在其中游泳的水，尚未实现"""
    pass


class Layout(Objects):
    """布局物：出生点、通关点、保存点，触发器的父类"""

    def __init__(self, image_name, init_x, init_y):
        super().__init__(image_name, init_x, init_y)
        self.collidable = False
        self.jumpable = False
        self.lethal = False

    def action(self, *args):
        """对于布局物需要触发的用于重写的动作函数"""
        pass

class Trigger(Layout):
    """触发器类，用于设计机关和完成一些选择任务

    :param func 在scene模块中设定的函数，传入地址，函数用于实现触发器触发后的功能

    """
    def __init__(self, image_name, init_x, init_y, func):
        super().__init__(image_name, init_x, init_y)
        self.func = func

    def action(self):
        """触发器的动作函数，调用scene中设计好的触发动作"""

        self.func()

class Saver(Layout):
    """保存点类

    :param n 保存点标号
    :param difficulty 保存点的难度 保存点难度低于场景难度则可见
    :param visible 可见性，在不同难度下保存点的可见性不同，对应影响不同难度下的保存点数量
    """
    def __init__(self, image_name, init_x, init_y, n, difficulty = 0, visible = True):
        """初始化相关参数"""

        super().__init__(image_name, init_x, init_y)
        self.num = n
        self.difficulty = difficulty
        self.visible = visible
        if self.num == 1:
            self.act.image = 'load'


    def action(self, kid, scene):
        """保存点动作函数，重置重生点为当前保存点，将以前保存点改为失效贴图，将当前保存点改为生效贴图"""
        if self.act.image == 'unload':
            sounds.loadsound.play()
        if kid.rebirth_location < self.num:
            kid.rebirth_location = self.num
            self.act.image = "load"
            for i in scene.savers:
                if i.num < self.num and i.visible:
                    i.act.image = "hasload"

class Starting(Layout):
    """出生点，尚未实现，现以第一个保存点代替"""
    pass


class Ending(Layout):
    """通关点，切换到下一个场景"""

    def __init__(self, image_name, init_x, init_y):
        super().__init__(image_name, init_x, init_y)

    def action(self, scene):
        """通关点动作函数，将当前场景的结束属性设为True"""

        sounds.passsound.play()
        scene.over = True


class Scene(object):
    """场景类

    :param objects 场景内object的汇总
    :param bricks,blocks,thorns,lethals,savers,endings,triggers,layouts 场景内object的分类及分类汇总
    :param decorations,texts 场景内需要的装饰品、文本
    :param blackcurtain 用于处理死亡黑幕
    :param kid 场景内的kid
    :param waiting_j,need_press_j 用于处理等待按j的事件
    :param over 当前场景是否结束
    :param difficulty 场景的难度
    :param brick_image, thorn_image 场景素材图片
    :param death 记录当前scene死亡次数
    :param sum_death 记录总死亡次数
    :param loadfunc Scene的初始化函数
    """
    def __init__(self, loadfunc):
        """初始化相关变量"""

        self.objects = []
        self.bricks = []
        self.blocks = []
        self.thorns = []
        self.lethals = []
        self.savers = []
        self.endings = []
        self.triggers = []
        self.layouts = []
        self.texts = []
        self.decorations = []
        self.brick_image = ''
        self.thorn_image = ''
        self.blackcurtain = False
        self.kid = None
        self.waiting_j = False
        self.need_press_j = False
        self.over = False
        self.difficulty = 0
        self.death = 0
        self.sum_death = 0
        self.loadfunc = loadfunc

    def update(self):
        """场景内需要实时更新的函数"""

        self.kid.move_x(self)
        self.kid.jump(self)
        self.kid.move_y()
        self.kid.fall(self)
        self.kid.die(self)
        self.kid.image_refresh()

    def set_style(self, color):
        """设置场景风格接口"""
        self.brick_image = color + 'brick'
        self.thorn_image = color + 'thorn'

    def set_difficulty(self, difficulty):
        """用于设定、传递场景难度，改变不同难度下的保存点可见性"""
        self.difficulty = difficulty
        for saver in self.savers:
            if saver.difficulty < self.difficulty:
                saver.visible = False
                saver.act.image = 'null'

    def set_j(self):
        """处理一些等待j事件"""

        self.waiting_j = True

    def set_decorations(self,decorations):
        """创建装饰物接口"""
        for dec in decorations:
            self.decorations.append(Decoration(dec[0], dec[1], dec[2]))

    def set_texts(self,texts):
        """创建文本接口"""
        for text in texts:
            self.texts.append(Text(text=text[0], center=text[1], align=text[2], fontsize=text[3], color=text[4]))

    def set_bricks(self,bricks):
        """创建砖块接口"""
        for brick in bricks:
            self.bricks.append(Brick(self.brick_image, get_x(brick[0]), get_y(brick[1])))

    def set_thorns(self,thorns):
        """创建尖刺接口"""
        for thorn in thorns:
            self.thorns.append(Thorn(self.thorn_image, get_x(thorn[0]), get_y(thorn[1]), thorn[2]))

    def set_savers(self,savers):
        """创建保存点接口"""
        for saver in savers:
            self.savers.append(Saver('unload', get_x(saver[0]), get_y(saver[1]), saver[2], saver[3]))

    def set_endings(self,endings):
        """创建通关点接口"""
        for ending in endings:
            self.endings.append(Ending('ending', get_x(ending[0]), get_y(ending[1])))

    def set_triggers(self,triggers):
        """创建触发器接口"""
        for trigger in triggers:
            self.triggers.append(Trigger('null', get_x(trigger[0]), get_y(trigger[1]), trigger[2]))

    def append_objects(self):
        """汇总objects接口，用于初始化场景"""
        self.blocks += self.bricks

        self.lethals += self.thorns

        self.layouts += self.savers
        self.layouts += self.endings
        self.layouts += self.triggers

        self.objects = self.blocks + self.lethals + self.layouts

    def set_kid(self):
        """创建kid接口"""
        self.kid = Kid("standright", self.savers[0].act.x, self.savers[0].act.y)

    def load(self):
        self.loadfunc(self)

class Text(object):
    """文本类，用于添加到场景中

    :param text 文本字符串
    :param center 文本中心点像素坐标
    :param align 文本对齐方式
    :param fontname 文本字体
    :param fontsize 文本字号
    :param color 文本颜色
    """
    def __init__(self, text, center=None, align=None, fontname='01', fontsize=24, color='white'):
        self.text = text
        self.center = center
        self.align = align
        self.fontname = fontname
        self.fontsize = fontsize
        self.color = color

class Decoration(object):
    """装饰类，用于添加到场景中

    :param decoration 贴图素材文件名
    :param x,y 贴图中心点的像素坐标
    """
    def __init__(self, decoration, x, y):
        self.decoration = decoration
        self.x = x
        self.y = y







