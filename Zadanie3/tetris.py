import pygame
import sys
import numpy as np
from block import Block
import os
import time

pygame.init()
np.set_printoptions(threshold=sys.maxsize)

screen_dim_x = 10
screen_dim_y = 20
block_dim = 40
bonus_parameters = 300
screen = pygame.display.set_mode((screen_dim_x * block_dim + bonus_parameters, screen_dim_y * block_dim))
chosen_block_l = -1
pause = False
Point_counter = 0


def drawBlock(xl, yl, color, border=0):
    pygame.draw.rect(screen, color,
                     pygame.Rect(xl * block_dim, yl * block_dim, block_dim, block_dim), border)


def clearMaps(chosen_block_local):
    for coord in blocks_list[chosen_block_local].blocks:
        occupation_map[coord[0], coord[1]] = False
        blocks_map[coord[0], coord[1]] = -1
    for yyy, line in enumerate(single_blocks_map):
        for xxx, element in enumerate(line):
            if element == 0:
                occupation_map[xxx, yyy] = False
                blocks_map[xxx, yyy] = -1


def updateMaps(chosen_block_local):
    for coord in blocks_list[chosen_block_local].blocks:
        occupation_map[coord[0], coord[1]] = True
        blocks_map[coord[0], coord[1]] = chosen_block_local
    for yyy, line in enumerate(single_blocks_map):
        for xxx, element in enumerate(line):
            if element != 0:
                occupation_map[xxx, yyy] = True
                blocks_map[xxx, yyy] = 100
            elif element == 0:
                occupation_map[xxx, yyy] = False
                blocks_map[xxx, yyy] = -1


def rotate(direction, chosen_block_l):
    global occupation_map
    global blocks_map
    old_occupation_map = occupation_map.copy()
    old_blocks_map = blocks_map.copy()
    clearMaps(chosen_block_l)
    collision = False
    base_x, base_y = blocks_list[chosen_block_l].blocks[1]
    old_block = blocks_list[chosen_block_l].blocks.copy()
    for count, coord in enumerate(blocks_list[chosen_block_l].blocks):
        old_x, old_y = coord
        if direction == "left":
            new_x = base_x + (old_y - base_y)
            new_y = base_y - (old_x - base_x)
        elif direction == "right":
            new_x = base_x - (old_y - base_y)
            new_y = base_y + (old_x - base_x)
        else:
            pass
        blocks_list[chosen_block_l].blocks[count] = (new_x, new_y)
        if ((new_y < 0) |
                (new_y >= screen_dim_y) |
                (new_x >= screen_dim_x) |
                (new_x < 0)):
            collision = True
            break
        elif ((blocks_map[new_x, new_y] != chosen_block_l) &
              (blocks_map[new_x, new_y] != -1)):
            collision = True
            break
    if not collision:
        updateMaps(chosen_block_l)
    else:
        blocks_list[chosen_block_l].blocks = old_block
        blocks_map = old_blocks_map
        occupation_map = old_occupation_map


def move(direction, chosen_block_l):
    collision = False
    if direction == "down":
        for coord in blocks_list[chosen_block_l].blocks:
            if coord[1] + 1 >= screen_dim_y:
                collision = True
            elif ((blocks_map[coord[0], coord[1] + 1] != chosen_block_l) &
                  (blocks_map[coord[0], coord[1] + 1] != -1)):
                collision = True
        if not collision:
            clearMaps(chosen_block_l)
            blocks_list[chosen_block_l].down()
            updateMaps(chosen_block_l)
        else:
            return True
    elif direction == "right":
        for coord in blocks_list[chosen_block_l].blocks:
            if coord[0] + 1 >= screen_dim_x:
                collision = True
            else:
                if ((blocks_map[coord[0] + 1, coord[1]] != chosen_block_l) &
                        (blocks_map[coord[0] + 1, coord[1]] != -1)):
                    collision = True
        if not collision:
            clearMaps(chosen_block_l)
            blocks_list[chosen_block_l].right()
            updateMaps(chosen_block_l)
    elif direction == "left":
        for coord in blocks_list[chosen_block_l].blocks:
            if coord[0] - 1 < 0:
                collision = True
            else:
                if ((blocks_map[coord[0] - 1, coord[1]] != chosen_block_l) &
                        (blocks_map[coord[0] - 1, coord[1]] != -1)):
                    collision = True
        if not collision:
            clearMaps(chosen_block_l)
            blocks_list[chosen_block_l].left()
            updateMaps(chosen_block_l)


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def add_block(blocks):
    global occupation_map
    proper = False
    global blocks_map
    while not proper:
        nowy_klocek = Block(len(blocks),
                            int(screen_dim_x / 2) - 1, 0, np.random.randint(0, 7), skin_type)
        for spot in nowy_klocek.blocks:
            if not occupation_map[spot[0], spot[1]]:
                proper = True
            else:
                proper = False
                break
        if proper:
            for spot in nowy_klocek.blocks:
                occupation_map[spot[0], spot[1]] = True
                blocks_map[spot[0], spot[1]] = nowy_klocek.block_id
            blocks.append(nowy_klocek)
            blocks[-1].chosen = True
    return blocks


def draw_button(button_id, text, font, color=(200, 0, 0), counter=False):
    if not counter:
        button_width = screen.get_width() * 0.8
        button_height = screen.get_height() * 0.1
        button_x = (screen.get_width() - button_width) / 2
        button_y = (screen.get_height() - button_height) * button_id / 5
        button = pygame.Rect(button_x,
                             button_y,
                             button_width,
                             button_height)
        pygame.draw.rect(screen, color, button)
        screen.blit(font.render(text, True, (255, 255, 255)), (button_x * 1.1, button_y))
        return button
    else:
        button_width = screen.get_width() * 0.8
        button_height = screen.get_height() * 0.1
        button_x = (screen_dim_x * block_dim - button_width) / 2
        button_y = (screen_dim_y * block_dim - button_height) / 2
        button = pygame.Rect(button_x,
                             button_y,
                             button_width,
                             button_height)
        pygame.draw.rect(screen, color, button)
        screen.blit(font.render(text, True, (255, 255, 255)), (button_x, button_y))
        return button


def draw_window_name(text, font):
    coord_x = (screen.get_width() - screen.get_width() * 0.8) / 2
    coord_y = 0 + screen.get_height() * 0.05
    screen.blit(font.render(text, True, (255, 255, 255)), (coord_x * 1.1, coord_y))


def clearAll():
    global blocks_list
    global occupation_map
    global next_block
    global blocks_map
    global single_blocks_map
    global next_block_item
    next_block_item = 1
    single_blocks_map = [[0 for i in range(screen_dim_x)] for j in range(screen_dim_y)]
    occupation_map = np.zeros((screen_dim_x, screen_dim_y), dtype=bool)
    blocks_map = np.zeros((screen_dim_x, screen_dim_y), dtype=np.int32)
    blocks_map[:, :] = -1
    next_block = False
    blocks_list = []


def menu():
    pygame.image.save(screen, 'screen.png')
    menu_music_path = resource_path('music\\tetris_menu.mp3')
    pygame.mixer.music.load(menu_music_path)
    pygame.mixer.music.play(loops=1000)
    click = False
    pygame.display.set_caption('Menu')
    font = pygame.font.SysFont('Bauhaus 93', 60)
    while True:
        screen.fill((0, 0, 0))
        draw_window_name('TETRIS', font)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        play_button = draw_button(1, 'PLAY', font)
        settings_button = draw_button(2, 'SETTINGS', font)
        exit_button = draw_button(3, 'EXIT', font)
        if play_button.collidepoint(mouse_x, mouse_y):
            draw_button(1, 'PLAY', font, (255, 0, 0))
            if click:
                game()
        if exit_button.collidepoint(mouse_x, mouse_y):
            draw_button(3, 'EXIT', font, (255, 0, 0))
            if click:
                os.remove('screen.png')
                sys.exit(0)
        if settings_button.collidepoint(mouse_x, mouse_y):
            draw_button(2, 'SETTINGS', font, (255, 0, 0))
            if click:
                settings()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            pygame.display.update()


def settings():
    click = False
    pygame.display.set_caption('Settings')
    font = pygame.font.SysFont('Bauhaus 93', 60)
    while True:
        screen.fill((0, 0, 0))
        draw_window_name('SETTINGS', font)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        controls_button = draw_button(1, 'CONTROLS', font)
        difficulty_button = draw_button(2, 'DIFFICULTY', font)
        skin_button = draw_button(3, 'SKIN', font)
        back_button = draw_button(4, 'BACK', font)
        if controls_button.collidepoint(mouse_x, mouse_y):
            draw_button(1, 'CONTROLS', font, (255, 0, 0))
            if click:
                controls()
        if difficulty_button.collidepoint(mouse_x, mouse_y):
            draw_button(2, 'DIFFICULTY', font, (255, 0, 0))
            if click:
                difficulty()
        if skin_button.collidepoint(mouse_x, mouse_y):
            draw_button(3, 'SKIN', font, (255, 0, 0))
            if click:
                skin()
        if back_button.collidepoint(mouse_x, mouse_y):
            draw_button(4, 'BACK', font, (255, 0, 0))
            if click:
                menu()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                    menu()
            pygame.display.update()


def controls():
    click = False
    pygame.display.set_caption('Controls')
    font = pygame.font.SysFont('Bauhaus 93', 60)
    font_steering = pygame.font.SysFont('Bauhaus 93', 40)
    while True:
        screen.fill((0, 0, 0))
        draw_window_name('CONTROLS', font)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_button(1, 'arrow up - rotate', font_steering)
        draw_button(2, 'arrows - left, right', font_steering)
        draw_button(3, 'SPACE - faster drop', font_steering)
        back_button = draw_button(4, 'BACK', font)
        if back_button.collidepoint(mouse_x, mouse_y):
            draw_button(4, 'BACK', font, (255, 0, 0))
            if click:
                settings()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                    settings()
            pygame.display.update()


def difficulty():
    global interval
    click = False
    pygame.display.set_caption('Controls')
    font = pygame.font.SysFont('Bauhaus 93', 60)
    while True:
        screen.fill((0, 0, 0))
        draw_window_name('DIFFICULTY', font)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        easy_button = draw_button(1, 'EASY', font)
        medium_button = draw_button(2, 'MEDIUM', font)
        hard_button = draw_button(3, 'INSANE', font)
        cancel_button = draw_button(4, 'CANCEL', font)
        if easy_button.collidepoint(mouse_x, mouse_y):
            draw_button(1, 'EASY', font, (255, 0, 0))
            if click:
                interval = 400
                settings()
                pass
        if medium_button.collidepoint(mouse_x, mouse_y):
            draw_button(2, 'MEDIUM', font, (255, 0, 0))
            if click:
                interval = 200
                settings()
                pass
        if hard_button.collidepoint(mouse_x, mouse_y):
            draw_button(3, 'INSANE', font, (255, 0, 0))
            cancel_button = draw_button(4, 'CANCEL', font)
            if click:
                interval = 70
                settings()
                pass
        if cancel_button.collidepoint(mouse_x, mouse_y):
            draw_button(4, 'CANCEL', font, (255, 0, 0))
            if click:
                settings()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                    settings()
            pygame.display.update()


def skin():
    click = False
    global skin_type
    pygame.display.set_caption('Controls')
    font = pygame.font.SysFont('Bauhaus 93', 60)
    while True:
        screen.fill((0, 0, 0))
        draw_window_name('SKIN', font)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        skin1_button = draw_button(1, 'SPRING', font)
        skin2_button = draw_button(2, 'SAD', font)
        skin3_button = draw_button(3, 'HAPPY', font)
        cancel_button = draw_button(4, 'BACK', font)
        if skin1_button.collidepoint(mouse_x, mouse_y):
            draw_button(1, 'SPRING', font, (255, 0, 0))
            if click:
                skin_type = 2
                settings()
                pass
        if skin2_button.collidepoint(mouse_x, mouse_y):
            draw_button(2, 'SAD', font, (255, 0, 0))
            if click:
                skin_type = 1
                settings()
                pass
        if skin3_button.collidepoint(mouse_x, mouse_y):
            draw_button(3, 'HAPPY', font, (255, 0, 0))
            if click:
                skin_type = 3
                settings()
                pass
        if cancel_button.collidepoint(mouse_x, mouse_y):
            draw_button(4, 'BACK', font, (255, 0, 0))
            if click:
                settings()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                    settings()
            pygame.display.update()


def lost():
    pygame.image.save(screen, 'screen.png')
    screen.fill((0, 0, 0))
    background = pygame.image.load('screen.png')
    screen.blit(background, (0, 0))
    text1 = "GAME"
    text2 = "OVER"
    text1_bg = "GAME"
    text2_bg = "OVER"
    font = pygame.font.SysFont('Bauhaus 93', 150)
    font_bg = pygame.font.SysFont('Bauhaus 93', 160)
    screen.blit(font_bg.render(text1_bg, True, (0, 0, 0)), (screen.get_width() * 0.05,
                                                            screen.get_width() * 0.3))
    screen.blit(font_bg.render(text2_bg, True, (0, 0, 0)), (screen.get_width() * 0.1,
                                                            screen.get_width() * 0.6))
    screen.blit(font.render(text1, True, (255, 255, 255)), (screen.get_width() * 0.05,
                                                            screen.get_width() * 0.3))
    screen.blit(font.render(text2, True, (255, 255, 255)), (screen.get_width() * 0.1,
                                                            screen.get_width() * 0.6))
    pygame.display.update()
    pygame.mixer.music.fadeout(300)
    while pygame.mixer.music.get_busy():
        pass
    lost_music_path = resource_path('music\\tetris_lost.mp3')
    pygame.mixer.music.load(lost_music_path)
    pygame.mixer.music.play(loops=1000)
    pygame.display.set_caption('GAME OVER')
    pygame.display.update()
    while True:
        screen.fill((0, 0, 0))
        background = pygame.image.load('screen.png')
        screen.blit(background, (0, 0))
        screen.blit(font_bg.render(text1_bg, True, (0, 0, 0)), (screen.get_width() * 0.05,
                                                                screen.get_width() * 0.3))
        screen.blit(font_bg.render(text2_bg, True, (0, 0, 0)), (screen.get_width() * 0.1,
                                                                screen.get_width() * 0.6))
        screen.blit(font.render(text1, True, (255, 255, 255)), (screen.get_width() * 0.05,
                                                                screen.get_width() * 0.3))
        screen.blit(font.render(text2, True, (255, 255, 255)), (screen.get_width() * 0.1,
                                                                screen.get_width() * 0.6))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                clearAll()
                pygame.mixer.music.fadeout(1000)
                while pygame.mixer.music.get_busy():
                    pass
                menu()

        pygame.display.update()


def game():
    global next_block_item
    global from_pause
    global blocks_list
    if not from_pause:
        blocks_list = add_block(blocks_list)
        next_block_item = Block(1, int(screen_dim_x / 2) - 1, 0, np.random.randint(0, 7), skin_type)
        from_pause = False
    pygame.time.set_timer(1, interval)
    pygame.display.set_caption('Tetris')
    pygame.mixer.music.fadeout(1000)
    while pygame.mixer.music.get_busy():
        pass
    game_music_path = resource_path('music\\tetris_game.mp3')
    pygame.mixer.music.load(game_music_path)
    pygame.mixer.music.play(loops=1000)
    global next_block
    possible_move = True

    score_font = pygame.font.SysFont('Bauhaus 93', 60)
    score = 0
    score_text = 'SCORE'
    nb_text1 = 'NEXT'
    nb_text2 = 'BLOCK'

    if skin_type == 1:
        nb_background_color = (27, 0, 66)
    elif skin_type == 2:
        nb_background_color = (0, 10, 73)
    elif skin_type == 3:
        nb_background_color = (0, 34, 27)

    while True:

        if not possible_move:
            from_pause = False
            lost()
        chosen_block_l = len(blocks_list) - 1
        for i in range(screen_dim_y):
            if np.all(occupation_map[:, i]):
                pass
        if next_block:
            for block in blocks_list[-1].blocks:
                single_blocks_map[block[1]][block[0]] = blocks_list[-1].colour
                blocks_map[np.asarray(block)[0], np.asarray(block)[1]] = 100
                time.sleep(0.1)
            blocks_list.pop(-1)
            next_block_item.block_id = 0
            blocks_list.append(next_block_item)
            next_block_item = Block(1, int(screen_dim_x / 2) - 1, 0, np.random.randint(0, 7), skin_type)
            next_block = False
            possible_move = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('screen.png')
                sys.exit(0)

            screen.fill((0, 0, 0))
            screen.blit(score_font.render(score_text, True, (255, 255, 255)), (screen.get_width() * 0.65,
                                                                                            screen.get_height() * 0.06))

            screen.blit(score_font.render(str(score), True, (255, 255, 255)), (screen.get_width() * 0.65,
                                                                                            screen.get_height() * 0.14))

            screen.blit(score_font.render(nb_text1, True, (255, 255, 255)), (screen.get_width() * 0.62,
                                                                                            screen.get_height() * 0.28))

            screen.blit(score_font.render(nb_text2, True, (255, 255, 255)), (screen.get_width() * 0.67,
                                                                                            screen.get_height() * 0.35))

            pygame.draw.rect(screen,
                             nb_background_color,
                             pygame.Rect(11 * block_dim, 9.5 * block_dim, block_dim * 6, block_dim * 4))

            pygame.draw.rect(screen, next_block_item.colour,
                             pygame.Rect(11 * block_dim, 9.5 * block_dim, block_dim * 6, block_dim * 4), 10)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                move("left", chosen_block_l)
            if pressed[pygame.K_RIGHT]:
                move("right", chosen_block_l)
            if pressed[pygame.K_DOWN]:
                next_block = move("down", chosen_block_l)
                if next_block is None:
                    next_block = False
                    possible_move = True

            if event.type == pygame.KEYDOWN and blocks_list[-1].block_type != 5:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]:
                    rotate("right", chosen_block_l)
            if pressed[pygame.K_SPACE]:
                for _ in range(screen_dim_y):
                    next_block = move("down", chosen_block_l)
                    if next_block is None:
                        next_block = False
                        possible_move = True
            if event.type == 1:
                next_block = move("down", chosen_block_l)
                if next_block is None:
                    possible_move = True
                    next_block = False
            for x_dim in range(screen_dim_x):
                for y_dim in range(screen_dim_y):
                    drawBlock(x_dim, y_dim, (100, 100, 100), border=1)

            for id in blocks_list:
                for kloc in id.blocks:
                    drawBlock(kloc[0], kloc[1], id.colour)

            for kloc in next_block_item.blocks:
                if next_block_item.block_type == 5:
                    kloc = (kloc[0] + 9, kloc[1] + 10.5)
                    drawBlock(kloc[0], kloc[1], next_block_item.colour)
                elif next_block_item.block_type == 3:
                    kloc = (kloc[0] + 8, kloc[1] + 11)
                    drawBlock(kloc[0], kloc[1], next_block_item.colour)
                else:
                    kloc = (kloc[0] + 8.5, kloc[1] + 10.5)
                    drawBlock(kloc[0], kloc[1], next_block_item.colour)

            for xxx_id, xxx in enumerate(single_blocks_map):
                sum_in_row = 0
                for element in xxx:
                    if element != 0:
                        sum_in_row += 1
                if sum_in_row == screen_dim_x:
                    single_blocks_map[1:(xxx_id + 1)] = single_blocks_map[:xxx_id]
                    single_blocks_map[0] = [0 for i in range(len(single_blocks_map[0]))]
                    score += 1

            for yyy, line in enumerate(single_blocks_map):
                for xxx, element in enumerate(line):
                    if element != 0:
                        drawBlock(xxx, yyy, element)

            pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_m] or pressed[pygame.K_ESCAPE]:
                    clearAll()
                    pygame.mixer.music.fadeout(1000)
                    while pygame.mixer.music.get_busy():
                        pass
                    menu()
                if pressed[pygame.K_p]:
                    pygame.mixer.music.fadeout(1000)
                    while pygame.mixer.music.get_busy():
                        pass
                    from_pause = True
                    menu()




occupation_map = np.zeros((screen_dim_x, screen_dim_y), dtype=bool)
blocks_map = np.zeros((screen_dim_x, screen_dim_y), dtype=np.int32)
blocks_map[:, :] = -1

blocks_list = []
skin_type = 3

single_blocks_map = [[0 for i in range(screen_dim_x)] for j in range(screen_dim_y)]
next_block_item = 1

next_block = False
from_pause = False

interval = 400  # 700 - very easy, 500- easy, 400 -normal, 250 - hard, 50 - insane
clock = pygame.time.Clock()
menu()
