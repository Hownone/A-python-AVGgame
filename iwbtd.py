# -*- coding:gb18030 -*-

import pgzrun
from pgzero.clock import clock
from pgzero.keyboard import keyboard

from scenes import *


def draw():
    # 绘制函数
    # 装饰物的绘制
    if scene.decorations and not scene.over:
        for dec in scene.decorations:
            screen.blit(dec.decoration, (dec.x, dec.y))
    # 实体的绘制
    for i in range(len(scene.objects)):
        scene.objects[i].act.draw()
    # kid的绘制
    if scene.kid and scene.kid.visible:
        scene.kid.act.draw()
    # 死亡黑幕
    if scene.blackcurtain:
        screen.blit('blackcurtain', (0,0))
    # 文本框的绘制
    if scene.texts:
        for text in scene.texts:
            screen.draw.text(text.text,center=text.center, align=text.align, fontname=text.fontname,
                             fontsize=text.fontsize, color=text.color)



def update():
    global scene, i
    # 重复播放bgm
    if not music.is_playing('bgm'):
        music.play('bgm')
        music.set_volume(0.7)
    # 更新场景
    scene.update()
    # 处理需要按j的等待事件
    if scene.waiting_j:
        if keyboard.j:
            scene.over = True
    # 处理切换场景事件
    if scene.over:
        if i == len(scenes) - 1:
            exit()
        else:
            i += 1
            scene = scenes[i]
            scene.sum_death = scenes[i - 1].death + scenes[i - 1].sum_death
            scene.difficulty = scenes[i - 1].difficulty
            scene.load()
            scene.set_difficulty(scene.difficulty)
            if scene.need_press_j:
                clock.schedule_unique(scene.set_j,1)

i = 0  # 场景序号
scene = scenes[i]  # 提取场景
scene.load()
pgzrun.go()  # pycharm环境下需要调用pgzrun.go()启动程序
