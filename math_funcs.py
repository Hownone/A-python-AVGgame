from math import *
"""
进行三角形与圆形碰撞检测数学算法
方块坐标转换像素坐标匿名函数
"""

# 方块坐标 转换 像素坐标 匿名函数
get_x = lambda x0:30 * x0 - 15
get_y = lambda y0:30 * y0 - 15

def evaluate_point_to_line(x, y, x1, y1, x2, y2):
    """计算点到线距离"""

    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    return a * x + b * y + c


def is_point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
    """判断点是否在三角形内"""
    d1 = evaluate_point_to_line(x, y, x1, y1, x2, y2)
    d2 = evaluate_point_to_line(x, y, x2, y2, x3, y3)
    if d1 * d2 < 0:
        return False
    d3 = evaluate_point_to_line(x, y, x3, y3, x1, y1)
    if d2 * d3 < 0:
        return False
    return True


def is_circle_intersect_line_seg(x, y, r, x1, y1, x2, y2):
    """判断圆是否与直线相交"""
    vx1 = x - x1
    vy1 = y - y1
    vx2 = x2 - x1
    vy2 = y2 - y1
    len = sqrt(vx2 ** 2 + vy2 ** 2)
    vx2 /= len
    vy2 /= len
    u = vx1 * vx2 + vy1 * vy2
    if u <= 0:
        x0 = x1
        y0 = y1
    elif u >= len:
        x0 = x2
        y0 = y2
    else:
        x0 = x1 + vx2 * u
        y0 = y1 + vx2 * u
    if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
        return True


def is_circle_intersect_triangle(x, y, r, x1, y1, x2, y2, x3, y3):
    """判断圆是否与三角形相交"""
    if is_point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
        return True
    if is_circle_intersect_line_seg(x, y, r, x1, y1, x2, y2):
        return True
    if is_circle_intersect_line_seg(x, y, r, x2, y2, x3, y3):
        return True
    if is_circle_intersect_line_seg(x, y, r, x3, y3, x1, y1):
        return True
    return False
