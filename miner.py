import numpy as np
import pygame
import winconfig
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
	[[1, 0, 1, 0, 0, 1, 0, 0], 
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





def game_field_drawing(cfg, screen, pics):
	""" Заливка окна + наложение сетки """


	screen.fill((150, 150, 150)) # Цвет бэкграунда


	for j in range(cfg.cell_quantity):
		for i in range(cfg.cell_quantity):

			if (open_cell_matrix[i][j]) == 0:
				screen.blit(
					pics.cell_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif mas[i][j]:
				screen.blit(
					pics.mine_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif ((dig_matrix[i][j] > 0) and (dig_matrix[i][j] < 9)):
				screen.blit(
					pics.digit_images_list[dig_matrix[i][j]], 
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

		# Rows drawing
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

	# Подгрузка изображений
	pics = winconfig.Image(cfg)

	clock = pygame.time.Clock()
	game_running = True
	while game_running:
		clock.tick(cfg.fps)

		for event in pygame.event.get():

			# Нажатие на ячейку
			if (event.type == pygame.MOUSEBUTTONDOWN):
				x, y = (pygame.mouse.get_pos())
				x //= cfg.cell_size
				y = (y - cfg.head_hight) // cfg.cell_size

				# Координата + left right button
				print(x, y, "l" if event.button == 1 else "r") 

			# Выход из игры
			if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT):
				game_running = False
			
		# Зарисовка экрана
		game_field_drawing(cfg, screen, pics)
		pygame.display.flip()




def main():
	cfg = winconfig.WinConfig()
	screen = screen_init(cfg)
	screen_interaction(cfg, screen)




if __name__ == '__main__':
	main()


