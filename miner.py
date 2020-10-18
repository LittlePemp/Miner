import numpy as np
import pygame
import winconfig
from PIL import ImageTk, Image


mas = np.zeros((25, 25))

dig_matrix = np.zeros((25, 25))

open_cell_matrix = np.zeros((25, 25))


def timer(cfg):
	""" Счет секунд """
	ticks = pygame.time.get_ticks()
	seconds = int(ticks / 1000)
	timer_time = 's: {seconds:03d}'.format(seconds=seconds)
	
	return timer_time 
	



def game_field_drawing(cfg, pics):
	""" Заливка окна + наложение сетки """


	cfg.screen.fill((150, 150, 150)) # Цвет бэкграунда


	for j in range(cfg.cell_quantity):
		for i in range(cfg.cell_quantity):

			if (open_cell_matrix[i][j]) == 0:
				cfg.screen.blit(
					pics.cell_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif mas[i][j]:
				cfg.screen.blit(
					pics.mine_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif ((dig_matrix[i][j] > 0) and (dig_matrix[i][j] < 9)):
				cfg.screen.blit(
					pics.digit_images_list[dig_matrix[i][j]], 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))


	for i in range(cfg.cell_quantity + 1):
		
		# Columns drawing
		pygame.draw.line(
			cfg.screen,
			(0, 0, 0),
			[0, cfg.cell_size*i + cfg.head_hight], 
			[cfg.cell_size * cfg.cell_quantity, 
				cfg.cell_size*i + cfg.head_hight], 
			1)

		# Rows drawing
		pygame.draw.line(
			cfg.screen, 
			(0, 0, 0),

			[cfg.cell_size*i, 
				cfg.head_hight],

			[cfg.cell_size*i, 
				cfg.cell_size*cfg.cell_quantity + cfg.head_hight], 
			1)

	#Вставка таймера
	timer_time = timer(cfg)

	cfg.font.render_to(cfg.screen, 
		(cfg.cell_size * cfg.cell_quantity - 120, cfg.head_hight / 2 + 10), 
		timer_time, 
		(138, 43, 226))





def screen_interaction(cfg):
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
		game_field_drawing(cfg, pics)
		pygame.display.flip()




def main():
	cfg = winconfig.WinConfig()
	screen_interaction(cfg)




if __name__ == '__main__':
	main()


