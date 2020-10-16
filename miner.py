import numpy as np
import pygame
from winconfig import *
from PIL import ImageTk, Image


mas = np.array(
	[[0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 1, 0, 0], 
	[0, 0, 0, 1, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 1, 0], 
	[0, 0, 1, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 1, 0, 0, 0], 
	[0, 1, 0, 0, 0, 1, 0, 0]])




def screen_init(cfg):
	""" Инициализация окна """
	pygame.init()
	pygame.mixer.init()  # Voice

	screen = pygame.display.set_mode(
		(cfg.cell_size * cfg.cell_quantity + 1,
		cfg.cell_size * cfg.cell_quantity + cfg.head_hight + 1))

	
	pygame.display.set_caption(cfg.title)

	return screen



def img_load(cfg):
	mine_image = pygame.image.load("sourse/img/mine.png").convert_alpha()
	mine_image = pygame.transform.scale(
		mine_image, 
		(cfg.cell_size, cfg.cell_size))

	return mine_image



def game_field_drawing(cfg, screen):
	""" Заливка окна + наложение сетки/
	Добавление head_high для хэд бара """

	mine_image = img_load(cfg)

	screen.fill((50, 50, 50))

	for i in range(cfg.cell_quantity + 1):

		# Columns drawing
		pygame.draw.line(
			screen,
			(255, 255, 255),
			[0, cfg.cell_size*i + cfg.head_hight], 
			[cfg.cell_size * cfg.cell_quantity, 
				cfg.cell_size*i + cfg.head_hight], 
			1)

		# Rows drwing
		pygame.draw.line(
			screen, 
			(255, 255, 255),

			[cfg.cell_size*i, 
				cfg.head_hight],

			[cfg.cell_size*i, 
				cfg.cell_size * cfg.cell_quantity + cfg.head_hight], 
			1)

	for i in range(cfg.cell_quantity):
		for j in range(cfg.cell_quantity):
			if mas[i][j]:
				screen.blit(
					mine_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))



def screen_interaction(cfg, screen):
	""" Обработка событий + вызов заливки """

	clock = pygame.time.Clock()
	game_running = True
	while game_running:
		clock.tick(cfg.fps)
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT):
				game_running = False
			
		game_field_drawing(cfg, screen)
		pygame.display.flip()



def main():
	cfg = WinConfig()
	screen = screen_init(cfg)
	screen_interaction(cfg, screen)



if __name__ == '__main__':
	main()


