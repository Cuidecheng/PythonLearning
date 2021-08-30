# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/19 20:47

import sys
import math
import pygame
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("make Pie game")
font = pygame.font.Font(None, 30)

color = 200, 80, 60
x = 300
y = 250
radius = 200
pos = x-radius, y-radius, radius*2, radius*2
color_draw = 255, 255, 0
change_flag = False

press_1 = False
press_2 = False
press_3 = False
press_4 = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                press_1 = True
            elif event.key == pygame.K_2:
                press_2 = True
            elif event.key == pygame.K_3:
                press_3 = True
            elif event.key == pygame.K_4:
                press_4 = True

    screen.fill((255, 255, 255))
    textImage1 = font.render('1', True, color)
    screen.blit(textImage1, (x+radius/2, y-radius/2))
    textImage2 = font.render('2', True, color)
    screen.blit(textImage2, (x-radius/2, y-radius/2))
    textImage3 = font.render('3', True, color)
    screen.blit(textImage3, (x-radius/2, y+radius/2))
    textImage4 = font.render('4', True, color)
    screen.blit(textImage4, (x+radius/2, y+radius/2))


    width = 4

    if press_1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color_draw, pos, start_angle, end_angle, width)
        pygame.draw.line(screen, color_draw, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color_draw, (x, y), (x+radius, y), width)
    if press_2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color_draw, pos, start_angle, end_angle, width)
        pygame.draw.line(screen, color_draw, (x, y), (x-radius, y), width)
        pygame.draw.line(screen, color_draw, (x, y), (x, y-radius), width)
    if press_3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color_draw, pos, start_angle, end_angle, width)
        pygame.draw.line(screen, color_draw, (x, y), (x-radius, y), width)
        pygame.draw.line(screen, color_draw, (x, y), (x, y+radius), width)
    if press_4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color_draw, pos, start_angle, end_angle, width)
        pygame.draw.line(screen, color_draw, (x, y), (x+radius, y), width)
        pygame.draw.line(screen, color_draw, (x, y), (x, y+radius), width)

    if press_1 and press_2 and press_3 and press_4:
        change_flag = not change_flag
        if change_flag:
            color_draw = 255, 255, 0
            time.sleep(0.2)
        else:
            color_draw = 200, 80, 60
            time.sleep(0.2)

    pygame.display.update()

    pass




