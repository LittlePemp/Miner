import numpy as np
import pygame
import winconfig
from PIL import ImageTk, Image
import mechanic



def timer(cfg):
	""" Счет секунд """
	ticks = pygame.time.get_ticks()
	seconds = int(ticks / 1000)
	timer_time = 's: {seconds:03d}'.format(seconds=seconds)
	
	return timer_time 
	



def game_field_drawing(cfg, pics, game_matrixes=None):
	""" Заливка окна + наложение сетки """




	for j in range(cfg.cell_quantity):
		for i in range(cfg.cell_quantity):

			if cfg.game_start:
				cfg.screen.blit(
					pics.cell_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))
			
			elif (game_matrixes.clicked[i][j]) == 0:
				cfg.screen.blit(
					pics.cell_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))
			
			elif game_matrixes.mines[i][j]:
				cfg.screen.blit(
					pics.mine_image, 
					(i*cfg.cell_size, j*cfg.cell_size + cfg.head_hight))

			elif ((game_matrixes.neighbours[i][j] > 0)):
				cfg.screen.blit(
					pics.digit_images_list[int(game_matrixes.neighbours[i][j])], 
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
def get_timer(cfg):
	timer_time = timer(cfg)
	cfg.screen.fill((150, 150, 150)) # Цвет бэкграунда
	cfg.font.render_to(cfg.screen, 
		(cfg.cell_size * cfg.cell_quantity - 120, cfg.head_hight / 2 + 10), 
		timer_time, 
		(18, 83, 255))





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

				# Первый клик
				if cfg.game_start:
					cfg.game_start = False
					try:
						game_matrixes = mechanic.Mechanics(x, y, cfg.cell_quantity)
					except:
						cfg.game_start = True
				# Вызов фунции для обновления массива по кликам. Координата + left right button
				else:
					game_running = game_matrixes.game(x, y, "l" if event.button == 1 else "r")



			# Выход из игры
			if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT):
				game_running = False
			
		# Зарисовка экрана с таймерм, если нет нажатий
		get_timer(cfg)

		if cfg.game_start:
			game_field_drawing(cfg, pics)
		if cfg.game_start == False:	
			game_field_drawing(cfg, pics, game_matrixes)

		pygame.display.flip()



def main():
	cfg = winconfig.WinConfig()
	screen_interaction(cfg)




if __name__ == '__main__':
	main()


