# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/19 18:25

import sys
import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))  # 初始化一个准备显示的窗口或屏幕
pygame.display.set_caption("Drawing Rectangles")  # 设置当前窗口标题

pos_x = 300
pos_y = 250
vel_x = 0.15
vel_y = 0.075

while True:
    for event in pygame.event.get():
        if event in (QUIT, KEYDOWN):
            sys.exit()

    # 移动矩形
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 550 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 450 or pos_y < 0:
        vel_y = -vel_y

    screen.fill((0, 0, 200))
    color = 255, 255, 0
    width = 0
    pos = pos_x, pos_y, 50, 50  # (初始x位置， 初始y位置， 矩形长，矩形宽)

    start_angle = math.radians(90)
    end_angle = math.radians(180)
    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()

