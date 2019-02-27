import pygame
pygame.init()
display_width = 500
display_height = 500

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("spectrum")
clock = pygame.time.Clock()

def spectrum():
	
	red = []
	green = []
	blue = []
	
	resolution = 40
	for r in range(0, 255, resolution):
		red.append(r)
	for g in range(0, 255, resolution):
		green.append(g)
	for b in range(0, 255, resolution):
		blue.append(b)
		
	
	
	w = 20
	xpos = 0
	ypos = 0
	
	for x in range(0, len(red)):
		for y in range(0, len(green)):
			for z in range(0, len(blue)):
				print((red[x],green[y],blue[z]))
				pygame.draw.rect(gameDisplay, (red[x],green[y],blue[z]), (xpos, ypos, w, w))
				pygame.display.update()
				if xpos < ((250/resolution)+1)**3:
					xpos += w
				else:
					xpos = 0
					ypos += w

loop = True					
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if loop:					
			spectrum()		
			loop = False
		else:
			print("Hi")

		
