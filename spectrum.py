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
	
	resolution = 50
	for r in range(0, 255, resolution):
		red.append(r)
	for g in range(0, 255, resolution):
		green.append(g)
	for b in range(0, 255, resolution):
		blue.append(b)
		
	colors = []
	colorPosx = []
	colorPosy = []
	
	w = 20
	xpos = 0
	ypos = 0
	
	for x in range(0, len(red)):
		for y in range(0, len(green)):
			for z in range(0, len(blue)):
				 colors.append((red[x],green[y],blue[z]))
				 
	for i in range(0, len(colors)):
		pygame.draw.rect(gameDisplay, colors[i], (xpos, ypos, w, w))
		pygame.display.update()
		colorPosx.append(xpos)
		colorPosy.append(ypos)
		
		if xpos < ((250/resolution)+1)**3:
			xpos += w
		else:
			xpos = 0
			ypos += w
				
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		
		choice = True
		
		
		
		i = 0
		while choice:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			#print(colors[i], colorPosx[i], colorPosy[i], i)
			
			if colorPosx[i] < mouse[0] < colorPosx[i] + w and colorPosy[i] < mouse[1] < colorPosy[i] + w: 
				
				if click[0] == 1:
					return colors[i]
					
					choice = False
			
			if i < len(colors)-1:
				i += 1
			else:
				i = 0
					
print(spectrum())

		
