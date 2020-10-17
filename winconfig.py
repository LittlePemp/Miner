import pygame



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


	# Цикл для каждой цифры
	for digit_image in range(1,9):

		digit_images_list.append(pygame.image.load(('sourse/img/{}.png'.format(str(digit_image)))).convert_alpha())
		digit_images_list[digit_image] = pygame.transform.scale(
			digit_images_list[digit_image], 
			(cfg.cell_size, cfg.cell_size))

	return (mine_image, 
		cell_image, 
		digit_images_list)



class WinConfig():
	"""docstring for WinConfig"""
	def __init__(self):
		self.title = "Miner"
		self.cell_quantity = 8
		self.cell_size = 50
		self.head_hight = 75
		self.fps = 60



class Image():
	def __init__(self, cfg):
		self.mine_image, self.cell_image, self.digit_images_list = img_load(cfg)