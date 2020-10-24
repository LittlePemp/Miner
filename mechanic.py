import numpy as np
import random


def field_generation(click_x, click_y, side):
    '''Генерация массива мин и соседей'''
    mines_num = round(0.12 * side ** 2) + 2
    mines_set = set(random.sample(range(0, side ** 2), mines_num))

    if side * click_x + click_y in mines_set:
        mines_set.remove(side * click_x + click_y)

    mines = np.zeros((side, side))
    neighbours = np.zeros((side, side))

    for mine in mines_set:
        mine_x = mine // side
        mine_y = mine % side
        mines[mine_x][mine_y] += 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (mine_x + i >= 0) and (mine_x + i < side) and (mine_y + j >= 0) and (mine_y + j < side):
                    if mines[mine_x + i][mine_y + j] != 1:
                        neighbours[mine_x + i][mine_y + j] += 1

    return mines, neighbours, len(mines_set)


class Mechanics():

    def __init__(self, click_x, click_y,  side):
        self.mines, self.neighbours, self.mines_num = field_generation(click_x,click_y,side)
        self.clicked = np.zeros((side, side))
        self.flags = np.zeros((side, side))
        self.clicked[click_x][click_y] = 1
        self.side = side
        self.counter = 0
        #self.button = button





    def game(self, click_x, click_y, button):

        def clicked_arr(click_x, click_y):
            '''Проверка открытия клетки'''
            if button == "l":
                if self.clicked[click_x][click_y] == 1:
                    pass
                else:
                    self.clicked[click_x][click_y] += 1
                    self.counter += 1
            return self.clicked




        def is_mine(click_x, click_y):
            '''Проверка на вшивость'''
            cell = True
            if button == "l":
                if self.mines[click_x][click_y] == 1:
                    cell = False
                else:
                    pass

            return cell, self.neighbours[click_x][click_y]

        cell, neigh = is_mine(click_x,click_y)


        def flag_point(click_x, click_y):
            '''Установка и снятие флага'''
            if button == "r":
                if self.clicked[click_x][click_y] == 0:
                    self.flags[click_x][click_y] = 1

                else:
                    self.flags[click_x][click_y] = 1


        if self.side**2 - self.counter == self.mines_num:
            end_of_game = True
        else: 
            end_of_game = False

        return end_of_game, clicked_arr(click_x, click_y), cell, neigh, flag_point(click_x,click_y)