# A-python-AVG-game-
基于pgzero的一款用python编写开发的AVG小游戏

# Introduction of game

  游戏为 2D 平面单人单机游戏，采用复古像素风，玩家可以通过移动和跳跃躲避尖刺达到终点。
  游戏由初始的欢迎界面，难度选择界面，关卡，结束总结界面组成。
  其中除关卡以外的界面为固定的，而关卡为可拓展的。
  
 # Design style
 
 将人物物体和场景都作为独立对象处理，在 math_funcs 中实现一些用于碰撞检测的数学算法使 resource 中的代码更加专注于实现游戏功能。
 在 resources 中封装人物，物体，场景对象，留出接口给 scenes 使用。在 scenes 中进行关卡设计，整合resource 中的资源留给主程序使用。
 而 iwbtd 做主程序，链接了制作好的地图和pgzero接口。
 
 # Last
 
 游戏大部分玩法已实现，但依然可以添加一些小功能和想法，带pass的模块是有想法但还没有完全实现的，有兴趣的玩家可以自己DIY，在已有的父类基础上，完善子类模块，创造更丰富的游戏世界。
 
 # Display in game
 ![image](https://github.com/Hownone/A-python-AVGgame/blob/main/Display/3.png)
 
 
 
