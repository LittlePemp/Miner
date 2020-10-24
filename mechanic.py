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

        # Открыте вокруг пустого при перво нажатии
        self.open_around(click_x, click_y)



    # Координаты не выходят за рамки
    def in_field(self, x, y):
        if ((x >= 0) and (x < self.side) and
                (y >= 0) and (y < self.side)):
            return True
        else:
            return False

    def open_around(self, click_x, click_y):
            # Проверка на пустую действующую клутку
            if ((self.neighbours[click_x][click_y] == 0) and 
                    (self.mines[click_x][click_y] == 0)):

                # Все выше и ниже данной пустой
                for i in range(-1, 2):
                    for j in range(-1, 2, 2):
                        x = click_x + i
                        y = click_y + j
                        if (self.in_field(x, y) and (self.clicked[x][y]) == 0):
                            self.clicked_arr(x, y)

                # Слева и справа данной пустой
                for i in range(-1, 2, 2):
                    x = click_x + i
                    y = click_y
                    if (self.in_field(x, y) and (self.clicked[x][y]) == 0):
                        self.clicked_arr(x, y)

    def clicked_arr(self, click_x, click_y, button="l"):
        '''Проверка открытия клетки'''
        if ((button == "l") and (self.clicked[click_x][click_y]) == 0):
            self.clicked[click_x][click_y] = 1
            self.counter += 1

        # Вскрытие соседей пустых
        self.open_around(click_x, click_y)




    def mine_or_flag(self, click_x, click_y, button):
        '''Проверка на вшивость'''
        cell = True
        if button == "l":
            if self.mines[click_x][click_y] == 1:
                self.cell = False
            '''Установка и снятие флага'''
        if (button == "r") and (self.clicked[click_x][click_y] == 0):
            if self.flags[click_x][click_y] == 1:
                self.flags[click_x][click_y] = 0

            else:
                self.flags[click_x][click_y] = 1


    def game(self, click_x, click_y, button="l"):
        self.clicked_arr(click_x,click_y, button)
        self.mine_or_flag(click_x, click_y, button)