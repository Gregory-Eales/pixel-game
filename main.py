import pygame
import sys
import os


def init_screen_and_clock():
    global screen, display, clock, fonts
    pygame.init()
    WINDOW_SIZE = (1150, 640)
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    clock = pygame.time.Clock()
    fonts = create_fonts([32, 16, 14, 8])
 
 
def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts
 
 
def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)
 
 
def display_fps():
    "Data that will be rendered and blitted in _display"
    render(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))

def load_image(path='./assets/character/PNG/idle-run-jump/idle01.png'):
	img = pygame.image.load(path)#.convert_alpha()
	return img


def load_sprites():
	pass
 

def main():

	x = 100
	y = 100

	vx = 0
	vy = 0

 
	init_screen_and_clock()
	# This create different font size in one line
	
	img = load_image()

	running = True 

	while running:
	    screen.fill((0, 0, 0))
	    screen.blit(img, (x, y))
	    display_fps()

	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit(); sys.exit()
	            main = False

	        if event.type == pygame.KEYDOWN:

	            if event.key == pygame.K_LEFT or event.key == ord('a'):
	                x -= 1

	            if event.key == pygame.K_RIGHT or event.key == ord('d'):
	                x += 1

	            if event.key == pygame.K_UP or event.key == ord('w'):
	            	y-1

	            if event.key == pygame.K_DOWN or event.key == ord('s'):
	            	y+1

	        if event.type == pygame.KEYUP:
	            if event.key == pygame.K_LEFT or event.key == ord('a'):
	                print('left stop')
	            if event.key == pygame.K_RIGHT or event.key == ord('d'):
	                print('right stop')
	            if event.key == ord('q'):
	                pygame.quit()
	                sys.exit()
	                main = False 

	    clock.tick(1000)
	    pygame.display.flip()
	 
	pygame.quit()
	print("Game over")


if __name__ == '__main__':
	main()







