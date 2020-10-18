import numpy as np
import random


def field_generation(click_x, click_y, side):
    '''Генерация массива мин и соседей'''
    mines_num = round(0.12 * side**2) + 2
    mines_set = set(random.sample(range(0, side**2),mines_num))

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
                if (mine_x + i >= 0) and (mine_x + i < side) or (mine_y + j >= 0) and (mine_y + j < side):
                    if (i != 0) or (j != 0):
                        neighbours[mine_x + i][mine_y + j] += 1

    return mines, neighbours


class Mechanics():
    def __init__(self, click_x, click_y,  side):
        self.mines, self.neighbours = field_generation(click_x,click_y,side)
        self.clicked = np.zeros((side, side))
        self.flags = np.zeros((side, side))
        self.clicked[click_x][click_y] = 1





    def game(self, click_x, click_y):

        def clicked_arr(click_x, click_y):
            '''Проверка открытия клетки'''
            if self.clicked[click_x][click_y] == 1:
                pass
            else:
                self.clicked[click_x][click_y] += 1
            return self.clicked




        def is_mine(click_x, click_y):
            '''Проверка на вшивость'''
            if self.mines[click_x][click_y] == 1:
                cell = False
            else:
                cell = True

            return cell




        def flag_point(click_x, click_y):
            '''Установка флага'''
            self.flags[click_x][click_y] = 1
            return self.flags

        return clicked_arr(click_x, click_y), is_mine(click_x, click_y), flag_point(click_x,click_y)
