import pygame
import pygame.freetype
import mechanic


def img_load(cfg):
    """ Подгрузка объектов всех изображений """

    digit_images_list = [None, ]  # Список изображений цифр, начиная с 1

    mine_image = pygame.image.load("/Users/donatello/DDproject/sourse/img/mine.png").convert_alpha()
    mine_image = pygame.transform.scale(
        mine_image,
        (cfg.cell_size, cfg.cell_size))

    cell_image = pygame.image.load("/Users/donatello/DDproject/sourse/img/botton.png").convert_alpha()
    cell_image = pygame.transform.scale(
        cell_image,
        (cfg.cell_size, cfg.cell_size))

    flag_image = pygame.image.load("/Users/donatello/DDproject/sourse/img/flag.png").convert_alpha()
    flag_image = pygame.transform.scale(flag_image, (int(cfg.cell_size * 0.7),int(cfg.cell_size * 0.7)))

    # Цикл для каждой цифры
    for digit_image in range(1, 9):
        digit_images_list.append(pygame.image.load(
            ('/Users/donatello/DDproject/sourse/img/{}.png'.format(str(digit_image)))).convert_alpha())
        digit_images_list[digit_image] = pygame.transform.scale(
            digit_images_list[digit_image],
            (cfg.cell_size, cfg.cell_size))

    return (mine_image,
            cell_image,
            flag_image,
            digit_images_list)


def screen_init(cfg):
    """ Инициализация окна """
    pygame.init()
    pygame.mixer.init()  # Voice

    screen = pygame.display.set_mode(
        (cfg.cell_size * cfg.cell_quantity + 1,
         cfg.cell_size * cfg.cell_quantity + cfg.head_hight + 1))

    pygame.display.set_caption(cfg.title)

    return screen


class WinConfig():
    """docstring for WinConfig"""

    def __init__(self):
        self.title = "Miner"
        self.cell_quantity = 16
        self.cell_size = 30
        self.head_hight = 75
        self.fps = 60
        self.screen = screen_init(self)
        self.last_screen = screen_init(self)
        self.game_start = True
        self.verdict_time = 0

        self.timer_font = pygame.freetype.SysFont(None, 34)
        self.timer_font.origin = True
        self.txt_font = pygame.freetype.SysFont(None, 26)
        self.txt_font.origin = True

        self.state_time = pygame.time.get_ticks()

        self.verdict = None

    def round_restart(self):
        self.verdict = None
        self.game_start = True
        self.state_time = pygame.time.get_ticks()


class Image():
    def __init__(self, cfg):
        self.mine_image, self.cell_image, self.flag_image, self.digit_images_list = img_load(cfg)