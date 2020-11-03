import numpy as np
import random


def field_generation(click_x, click_y, side):
    '''Генерация массива мин и соседей'''
    mines_num = round(0.12 * side ** 2) + 2
    mines_set = set(random.sample(range(0, side ** 2), mines_num))

    if side * click_y + click_x in mines_set:
        mines_set.remove(side * click_y + click_x)

    mines = np.zeros((side, side))
    neighbours = np.zeros((side, side))

    for mine in mines_set:
        mine_y = mine // side
        mine_x = mine % side
        mines[mine_x][mine_y] += 1
        for j in range(-1, 2):
            for i in range(-1, 2):
                if (mine_x + i >= 0) and (mine_x + i < side) and (mine_y + j >= 0) and (mine_y + j < side):
                    if mines[mine_x + i][mine_y + j] != 1:
                        neighbours[mine_x + i][mine_y + j] += 1

    return mines, neighbours, mines_set


class Mechanics():

    def __init__(self, click_x, click_y,  side):
        self.mines, self.neighbours, self.mines_set = field_generation(click_x,click_y,side)
        self.clicked = np.zeros((side, side))
        self.flags = np.ones((side, side))
        #self.clicked[click_x][click_y] = 1
        self.counter = side ** 2
        self.flag_count = len(self.mines_set)
        self.side = side
        self.lose_game = False
        self.open(click_x,click_y)




    def open(self, click_x, click_y):
        """Открытие ячеек"""
        if (self.clicked[click_x][click_y] == 0) and (self.mines[click_x][click_y] == 0):
            self.clicked[click_x][click_y] += 1
            self.counter -= 1
            if self.neighbours[click_x][click_y] == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (click_x + i >= 0) and (click_x + i < self.side) and (click_y + j >= 0) and (
                                click_y + j < self.side):
                            self.open(click_x + i, click_y + j)




    def mine_flag_set(self, click_x, click_y, button):
        """Проверка на вшивость"""
        if button == "l":
            if self.mines[click_x][click_y] == 1:
                self.lose_game = True
                for j in range(self.side):
                    for i in range(self.side):
                        if self.mines[i][j]:
                            self.clicked[i][j] = 1

        """Установка и снятие флага"""
        if button == "r":
            if self.clicked[click_x][click_y] == 0:
                if (self.flag_count > 0) or (self.flags[click_x][click_y] == -1):
                    self.flags[click_x][click_y] *= -1

                    self.flag_count += int(self.flags[click_x][click_y])




    def end(self):
        if self.lose_game == True:
            return "Lose"
        elif self.counter == len(self.mines_set):
            for j in range(self.side):
                for i in range(self.side):
                    if self.mines[i][j]:
                        self.flags[i][j] = -1
            return "Win"


    def game(self, click_x, click_y, button):
        """Игровой ход"""
        self.mine_flag_set(click_x,click_y,button)
        if button == "l":
            self.open(click_x,click_y)
        return self.end()
