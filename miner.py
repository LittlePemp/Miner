import numpy as np
import pygame
from winconfig import *
from PIL import ImageTk, Image


mas = np.array(
	[[0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 1, 0, 0], 
	[0, 0, 0, 1, 0, 0, 0, 1], 
	[0, 0, 0, 0, 0, 0, 1, 0], 
	[0, 0, 1, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 1, 0, 0, 0], 
	[0, 1, 0, 0, 0, 1, 0, 1]])

dig_matrix = np.array(
   [[4, 1, 0, 1, 1, 1, 1, 0], 
	[5, 1, 2, 2, 1, 0, 2, 1], 
	[6, 0, 0, 0, 1, 2, 3, 1], 
	[7, 1, 2, 2, 0, 2, 0, 3], 
	[8, 1, 0, 1, 0, 3, 0, 3], 
	[0, 1, 1, 2, 1, 3, 0, 2], 
	[1, 1, 1, 1, 0, 3, 3, 2], 
	[1, 1, 1, 1, 2, 0, 2, 0]])

open_cell_matrix = np.array(
	[[1, 0, 1, 0, 0, 0, 0, 0], 
	[1, 0, 0, 0, 0, 0, 0, 0], 
	[1, 0, 0, 0, 0, 1, 0, 0], 
	[1, 0, 0, 0, 1, 1, 0, 0], 
	[1, 0, 0, 0, 1, 1, 0, 0], 
	[0, 0, 0, 0, 0, 1, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0]])



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

	cell_image = pygame.image.load("sourse/img/botton.png").convert_alpha()
	cell_image = pygame.transform.scale(
		cell_image, 
		(cfg.cell_size, cfg.cell_size))

	first_image = pygame.image.load("sourse/img/1.png").convert_alpha()
	first_image = pygame.transform.scale(
		first_image, 
		(cfg.cell_size, cfg.cell_size))

	second_image = pygame.image.load("sourse/img/2.png").convert_alpha()
	second_image = pygame.transform.scale(
		second_image, 
		(cfg.cell_size, cfg.cell_size))

	third_image = pygame.image.load("sourse/img/3.png").convert_alpha()
	third_image = pygame.transform.scale(
		third_image, 
		(cfg.cell_size, cfg.cell_size))

	fourth_image = pygame.image.load("sourse/img/4.png").convert_alpha()
	fourth_image = pygame.transform.scale(
		fourth_image, 
		(cfg.cell_size, cfg.cell_size))

	fifth_image = pygame.image.load("sourse/img/5.png").convert_alpha()
	fifth_image = pygame.transform.scale(
		fifth_image, 
		(cfg.cell_size, cfg.cell_size))

	sixth_image = pygame.image.load("sourse/img/6.png").convert_alpha()
	fifth_image = pygame.transform.scale(
		fifth_image, 
		(cfg.cell_size, cfg.cell_size))

	seventh_image = pygame.image.load("sourse/img/7.png").convert_alpha()
	seventh_image = pygame.transform.scale(
		seventh_image, 
		(cfg.cell_size, cfg.cell_size))

	eighth_image = pygame.image.load("sourse/img/8.png").convert_alpha()
	eighth_image = pygame.transform.scale(
		eighth_image, 
		(cfg.cell_size, cfg.cell_size))

	return (mine_image, 
		cell_image, 
		first_image,
		second_image,
		third_image,
		fourth_image,
		fifth_image,
		sixth_image,
		seventh_image,
		eighth_image)




def game_field_drawing(cfg, screen):
	""" Заливка окна + наложение сетки/
	Добавление head_high для хэд бара """

	(mine_image, 
	cell_image, 
	first_image,
	second_image,
	third_image,
	fourth_image,
	fifth_image,
	sixth_image,
	seventh_image,
	eighth_image) = img_load(cfg)

	screen.fill((150, 150, 150))

	for j in range(cfg.cell_quantity):
		for i in range(cfg.cell_quantity):

			if (open_cell_matrix[i][j]) == 0:
				screen.blit(
					cell_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif mas[i][j]:
				screen.blit(
					mine_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif dig_matrix[i][j] != 0:
				if dig_matrix[i][j] == 1:
					screen.blit(
					first_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 2:
					screen.blit(
					second_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 3:
					screen.blit(
					third_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 4:
					screen.blit(
					fourth_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 5:
					screen.blit(
					fifth_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 6:
					screen.blit(
					sixth_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 7:
					screen.blit(
					seventh_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

				if dig_matrix[i][j] == 8:
					screen.blit(
					eighth_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))


	for i in range(cfg.cell_quantity + 1):

		
		# Columns drawing
		pygame.draw.line(
			screen,
			(0, 0, 0),
			[0, cfg.cell_size*i + cfg.head_hight], 
			[cfg.cell_size * cfg.cell_quantity, 
				cfg.cell_size*i + cfg.head_hight], 
			1)

		# Rows drwing
		pygame.draw.line(
			screen, 
			(0, 0, 0),

			[cfg.cell_size*i, 
				cfg.head_hight],

			[cfg.cell_size*i, 
				cfg.cell_size*cfg.cell_quantity + cfg.head_hight], 
			1)





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


