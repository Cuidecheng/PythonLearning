# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/24 15:41

import pygame
import random
import sys
import os

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)
    pass

W = 600
H = 400
ROW = 40  # 10
COL = 60  # 10
size = (W, H)
pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

execute_flag_dict = {
    'prepare_flag': 1,
    'mode_selection_flag': 0,
    'running_flag': 0,
    'dead_flag': 0,
    'quit_flag': 0
}

get_foods = 0
clock_tick = 15

def prepare():

    global execute_flag_dict
    text_start_flag = False
    text_quit_flag = False
    background = pygame.image.load("pictures/bkg.png").convert_alpha()
    while True:
        if text_start_flag:
            font_start = pygame.font.Font(None, 32)
        else:
            font_start = pygame.font.Font(None, 30)
        if text_quit_flag:
            font_quit = pygame.font.Font(None, 29)
        else:
            font_quit = pygame.font.Font(None, 27)
        start_text = font_start.render("GO", True, (0, 0, 0))
        quit_text = font_quit.render("QUIT", True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if 530 <= event.pos[0] <= 570 and 340 <= event.pos[1] <= 357:
                    text_start_flag = True
                elif 25 <= event.pos[0] <= 85 and 340 <= event.pos[1] <= 357:
                    text_quit_flag = True
                else:
                    text_start_flag = False
                    text_quit_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if text_start_flag:
                    for keys in execute_flag_dict:
                        execute_flag_dict[keys] = 0
                    execute_flag_dict['mode_selection_flag'] = 1

                if text_quit_flag:
                    for keys in execute_flag_dict:
                        execute_flag_dict[keys] = 0
                    execute_flag_dict['quit_flag'] = 1

        if execute_flag_dict['mode_selection_flag'] or execute_flag_dict['quit_flag']:
            break
        window.blit(background, (0, 0))
        window.blit(start_text, (530, 340))
        window.blit(quit_text, (25, 340))
        clock.tick(60)
        pygame.display.update()
    pass

def mode_selection():

    text_easy_flag = False
    text_normal_flag = False
    text_difficult_flag = False
    global clock_tick
    global execute_flag_dict
    global get_foods
    get_foods = 0
    font_degree_title = pygame.font.Font(None, 37)
    background = pygame.image.load("pictures/mode_selection.png").convert_alpha()

    while True:

        if text_easy_flag:
            font_easy_mode = pygame.font.Font(None, 34)
        else:
            font_easy_mode = pygame.font.Font(None, 32)
        if text_normal_flag:
            font_normal_mode = pygame.font.Font(None, 34)
        else:
            font_normal_mode = pygame.font.Font(None, 32)
        if text_difficult_flag:
            font_difficult_mode = pygame.font.Font(None, 34)
        else:
            font_difficult_mode = pygame.font.Font(None, 32)
        degree_text = font_degree_title.render("Degree Selection:", True, (0, 0, 0))
        easy_text = font_easy_mode.render("easy", True, (0, 0, 0))  # 255, 165, 0
        normal_text = font_normal_mode.render("normal", True, (0, 0, 0))  # 255, 99, 71
        difficult_text = font_difficult_mode.render("difficult", True, (0, 0, 0))  # 255, 69, 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if 355 <= event.pos[0] <= 405 and 198 <= event.pos[1] <= 223:
                    text_easy_flag = True
                elif 345 <= event.pos[0] <= 423 and 260 <= event.pos[1] <= 280:
                    text_normal_flag = True
                elif 340 <= event.pos[0] <= 430 and 320 <= event.pos[1] <= 339:
                    text_difficult_flag = True
                else:
                    text_easy_flag = False
                    text_normal_flag = False
                    text_difficult_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for keys in execute_flag_dict:
                    execute_flag_dict[keys] = 0
                execute_flag_dict['running_flag'] = 1

                if text_easy_flag:
                    clock_tick = 15
                if text_normal_flag:
                    clock_tick = 22
                if text_difficult_flag:
                    clock_tick = 35

        if execute_flag_dict['running_flag']:
            break

        window.blit(background, (0, 0))
        window.blit(degree_text, (82, 83))
        window.blit(easy_text, (355, 198))
        window.blit(normal_text, (345, 260))
        window.blit(difficult_text, (340, 320))

        clock.tick(120)
        pygame.display.update()

    pass

def running():

    global get_foods

    def rect(point, color):
        cell_width = W / COL
        cell_height = H / ROW
        left = point.col * cell_width
        top = point.row * cell_height
        pygame.draw.rect(window, color, (left, top, cell_width, cell_height))

    head = Point(row=int(ROW / 2), col=int(COL / 2))
    snakes = [
        Point(row=head.row, col=head.col + 1),
        Point(row=head.row, col=head.col + 2),
        Point(row=head.row, col=head.col + 3),
    ]

    def generate_food():
        while True:
            is_crash = False
            pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
            if head.row == pos.row and head.col == pos.col:
                is_crash = True
            for body in snakes:
                if body.row == pos.row and body.col == pos.col:
                    is_crash = True
                    break
            if not is_crash:
                break
        return pos
    food = generate_food()
    bkg_color = (255, 255, 255)
    head_color = (0, 128, 128)
    food_color = (255, 128, 0)
    snake_color = (200, 200, 200)
    direct = 'left'

    while True:

        font_scores = pygame.font.Font(None, 35)
        font_number = pygame.font.Font(None, 35)
        scores_text = font_scores.render("scores:", True, (238, 106, 167))
        number_text = font_number.render(str(get_foods), True, (238, 106, 167))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:  # 键盘按下
                if event.key == 1073741906 or event.key == 119:
                    if direct == 'left' or direct == 'right':
                        direct = 'up'
                if event.key == 1073741905 or event.key == 115:
                    if direct == 'left' or direct == 'right':
                        direct = 'down'
                if event.key == 1073741904 or event.key == 97:
                    if direct == 'up' or direct == 'down':
                        direct = 'left'
                if event.key == 1073741903 or event.key == 100:
                    if direct == 'up' or direct == 'down':
                        direct = 'right'
        snakes.insert(0, head.copy())
        eat = (head.row == food.row and head.col == food.col)
        if not eat:
            snakes.pop()
        else:
            get_foods += 1
            food = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
        if direct == 'left':
            head.col -= 1
        elif direct == 'right':
            head.col += 1
        elif direct == 'up':
            head.row -= 1
        elif direct == 'down':
            head.row += 1
        if head.col < 0 or head.row < 0 or head.col >= COL or head.row >= ROW:
            for keys in execute_flag_dict:
                execute_flag_dict[keys] = 0
            execute_flag_dict['dead_flag'] = 1
        for snake in snakes:
            if head.col == snake.col and head.row == snake.row:
                for keys in execute_flag_dict:
                    execute_flag_dict[keys] = 0
                execute_flag_dict['dead_flag'] = 1
        if execute_flag_dict['dead_flag']:
            break
        window.fill(bkg_color)
        window.blit(scores_text, (20, 370))
        window.blit(number_text, (120, 370))
        rect(head, head_color)
        rect(food, food_color)
        for snake in snakes:
            rect(snake, snake_color)
        pygame.display.update()
        clock.tick(clock_tick)
        pass
    pass

def statistics():

    global get_foods
    text_over_quit_flag = False
    text_restart_flag = False
    font_first = pygame.font.Font(None, 35)
    font_second = pygame.font.Font(None, 35)
    font_third = pygame.font.Font(None, 35)
    font_over_quit = pygame.font.Font(None, 35)
    font_restart = pygame.font.Font(None, 35)
    over_quit_text = font_over_quit.render("QUIT", True, (139, 134, 130))
    restart_text = font_restart.render("RESTART", True, (34, 139, 34))
    rank_list = pygame.image.load("pictures/rank.png").convert_alpha()
    game_over = pygame.image.load("pictures/game_over.png").convert_alpha()

    def rank_sort(cur_scores):
        filename = 'ranking_list.txt'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as rfile:

                rank_info = rfile.readlines()
                rank_info_list = eval(rank_info[0])
                rank_info_list.append(cur_scores)
                rank_info_list.sort()
                rank_info_list = rank_info_list[::-1]
            with open(filename, 'w', encoding='UTF-8') as wfile:
                wfile.write(str(rank_info_list[:3]))
        else:
            rank_info_list = [0, 0, 0]
            with open(filename, 'a+') as file:
                rank_info_list.append(cur_scores)
                rank_info_list.sort()
                rank_info_list = rank_info_list[::-1]
            with open(filename, 'w', encoding='UTF-8') as wfile:
                wfile.write(str(rank_info_list[:3]))
        return rank_info_list[:3]
    scores_statistics = rank_sort(get_foods)
    first_text = font_first.render(str(scores_statistics[0]), True, (238, 106, 167))
    second_text = font_second.render(str(scores_statistics[1]), True, (238, 106, 167))
    third_text = font_third.render(str(scores_statistics[2]), True, (238, 106, 167))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if 150 <= event.pos[0] <= 260 and 200 <= event.pos[1] <= 220:
                    text_restart_flag = True
                elif 165 <= event.pos[0] <= 225 and 275 <= event.pos[1] <= 295:
                    text_over_quit_flag = True
                else:
                    text_over_quit_flag = False
                    text_restart_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if text_restart_flag:
                    for keys in execute_flag_dict:
                        execute_flag_dict[keys] = 0
                    execute_flag_dict['mode_selection_flag'] = 1
                if text_over_quit_flag:
                    for keys in execute_flag_dict:
                        execute_flag_dict[keys] = 0
                    execute_flag_dict['quit_flag'] = 1
        if execute_flag_dict['mode_selection_flag'] or execute_flag_dict['quit_flag']:
            break
        window.blit(restart_text, (150, 200))
        window.blit(over_quit_text, (165, 275))
        window.blit(rank_list, (370, 0))
        window.blit(game_over, (50, 80))
        window.blit(first_text, (490, 165))
        window.blit(second_text, (450, 237))
        window.blit(third_text, (530, 318))
        clock.tick(30)
        pygame.display.update()
    pass

if __name__ == '__main__':

    while True:
        if execute_flag_dict['prepare_flag']:
            prepare()
        if execute_flag_dict['mode_selection_flag']:
            mode_selection()
        if execute_flag_dict['running_flag']:
            running()
        if execute_flag_dict['dead_flag']:
            statistics()
        if execute_flag_dict['quit_flag']:
            break
            exit()




