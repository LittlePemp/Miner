import pygame
import pygame.freetype


def img_load(cfg):
	""" Подгрузка объектов всех изображений """

	digit_images_list = [None, ] # Список изображений цифр, начиная с 1


	mine_image = pygame.image.load("sourse/img/mine.png").convert_alpha()
	mine_image = pygame.transform.scale(
		mine_image, 
		(cfg.cell_size, cfg.cell_size))

	cell_image = pygame.image.load("sourse/img/botton.png").convert_alpha()
	cell_image = pygame.transform.scale(
		cell_image, 
		(cfg.cell_size, cfg.cell_size))

	flag_image = pygame.image.load("sourse/img/flag.png").convert_alpha()
	flag_image = pygame.transform.scale(
		flag_image, 
		(int(cfg.cell_size*0.7), int(cfg.cell_size*0.7)))


	# Цикл для каждой цифры
	for digit_image in range(1,9):

		digit_images_list.append(
			pygame.image.load(
				('sourse/img/{}.png'.format(str(digit_image)))).convert_alpha())
		
		digit_images_list[digit_image] = pygame.transform.scale(
			digit_images_list[digit_image], 
			(cfg.cell_size, cfg.cell_size))


	return (mine_image, 
		cell_image, 
		digit_images_list,
		flag_image)



def screen_init(cfg):
	""" Иницилизация окна """
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
		self.cell_quantity = 8
		self.cell_size = 50
		self.head_hight = 75
		self.fps = 60
		self.screen = screen_init(self)
		self.game_start = True

		self.timer_font = pygame.freetype.SysFont(None, 34)
		self.timer_font.origin = True
		self.txt_font = pygame.freetype.SysFont(None, 26)
		self.txt_font.origin = True
		self.end_font = pygame.freetype.SysFont(None, 72)
		self.end_font.origin = True

		self.state_time = pygame.time.get_ticks()
		self.game_verdict = None
		self.verdict_time = 0

	def round_restart(self):
		self.game_start = True
		self.state_time = pygame.time.get_ticks()
		self.game_verdict = None




class Image():
	def __init__(self, cfg):
		(self.mine_image,
		self.cell_image, 
		self.digit_images_list,
		self.flag_image) = img_load(cfg)
