import pygame
import math
import time
pygame.init()

display_width = 800
display_height = 600

#  COLOURS 
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

r = 250
g = 250
b = 250
color = (r,g,b)


# FONT SIZES
largeText = pygame.font.Font("freesansbold.ttf", 100)
medText = pygame.font.Font("freesansbold.ttf", 50)
smallText = pygame.font.Font("freesansbold.ttf", 20)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's see if we can paint eh")
clock = pygame.time.Clock()

def textObjects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()
	
def button(msg, x, y, w, h, ic, ac, action = None):	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x < mouse[0] < x+w and y < mouse[1] < y+h:
		pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
		pygame.draw.rect(gameDisplay, ic, (x+5, y+5, w-10, h-10))
		if click[0] == 1 and action != None:
			pygame.display.update()
			time.sleep(0.5)
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
	
	textSurf, textRect = textObjects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)


	
def spectrum():
	
	red = []
	green = []
	blue = []
	global color
	
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
	xpos = 100
	ypos = 100
	
	#for x in range(0, len(red)):
	#	for y in range(0, len(green)):
	#		for z in range(0, len(blue)):
	#			 colors.append((red[x],green[y],blue[z]))
	for x in range(0, 541):
		if x < 180:
			colors.append((red[int(math.cos(x)*5)] ,(green[1-int(math.cos(x)*5)]),0))
			 
		if 180 < x < 360:
			colors.append((0,(green[1-int(math.cos(x)*5)]),blue[int(math.cos(x)*5)]))
		
		if 360 < x < 540:
			colors.append(((red[1-int(math.cos(x)*5)]),0,blue[int(math.cos(x)*5)]))	

	print(len(colors))	
	for i in range(0, len(colors)):
		
		pygame.draw.rect(gameDisplay, colors[i], (xpos, ypos, w, w))
		pygame.display.update()
		colorPosx.append(xpos)
		colorPosy.append(ypos)
		
		if xpos < ((250/resolution)+1)**3 + 538:
			xpos += w
		else:
			xpos = 100
			ypos += w
	
	
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
				gameDisplay.fill(black)
				print(colors[i])
				color = colors[i]
				choice = False
		
		if i < len(colors)-1:
			i += 1
		else:
			i = 0
		
				
def chooseColor(mouse, click, choose):
	###### COLOR BUTTONS
	
	pygame.draw.rect(gameDisplay, red, (10, 50, 20, 20))
	if 10 < mouse[0] < 10+20 and 50 < mouse[1] < 50+20:
		pygame.draw.rect(gameDisplay, bright_red, (10, 50, 20, 20))
		if click[0] == 1:
			return red
			
	pygame.draw.rect(gameDisplay, blue, (10, 75, 20, 20))
	if 10 < mouse[0] < 10+20 and 75 < mouse[1] < 75+20:
		pygame.draw.rect(gameDisplay, bright_blue, (10, 75, 20, 20))
		if click[0] == 1:
			return blue
	
	pygame.draw.rect(gameDisplay, green, (10, 100, 20, 20))
	if 10 < mouse[0] < 10+20 and 100 < mouse[1] < 100+20:
		pygame.draw.rect(gameDisplay, bright_green, (10, 100, 20, 20))
		if click[0] == 1:
			return green
			
	pygame.draw.rect(gameDisplay, white, (10, 125, 20, 20))
	if 10 < mouse[0] < 10+20 and 125 < mouse[1] < 125+20:
		pygame.draw.rect(gameDisplay, (205,205,205), (10, 125, 20, 20))
		if click[0] == 1:
			return white
			
	return choose		
		
def drawLine():
	one = False
	two = False
	order = False
	clickOne = (0,0)
	clickTwo = (0,0)
	
	global color
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			###### COLOR BUTTONs
			color = chooseColor(mouse, click, color)
			######	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					if r < 250:
						r += 50
					elif r == 250 and g < 250:
						r = 0;
						g += 50
					elif r == 250 and g == 250 and b < 250:
						r = 0
						g = 0
						b += 50	
				if event.key == pygame.K_LEFT:
					if b > 0:
						b -= 50
					elif b == 0 and g > 0:
						b = 250
						g -= 50
					elif b == 0 and g == 0 and r > 0:
						b = 250
						g = 250
						r -= 50
				color = (r,g,b)
			######	
			button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)
			button("Erase All", 10, 550, 100, 30, red, bright_red, eraseAll)
			button("DRAW", 10, 10, 100, 30, green, bright_green, freeDraw)
			button("Spectrum", 360, 10, 100, 30, red, bright_red, spectrum)
			
			###### LINE DRAWING
			if event.type == pygame.MOUSEBUTTONDOWN and one == False:
				clickOne = (mouse[0], mouse[1])
				one = True
				order = True
					
			elif event.type == pygame.MOUSEBUTTONUP and order == True:
				clickTwo = (mouse[0],  mouse[1])
				two = True
			
			elif one and two:	
				pygame.draw.line(gameDisplay, color, clickOne, clickTwo, 3)
				pygame.display.update()
				one = False
				two = False
				order = False
			if click[2] == 1:
				pygame.draw.rect(gameDisplay, black, (mouse[0]-25, mouse[1]-25, 50, 50))
				
			pygame.display.update()
			clock.tick(500)	

def freeDraw():
	#add more functionality to colour
	loop = True
	
	global color
	
	while loop:	
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			
			##### COLOR BUTTONS
			color = chooseColor(mouse, click, color)
			######
			###### COLOR SLIDING USING ARROW KEYS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					if r < 250:
						r += 50
					elif r == 250 and g < 250:
						r = 0;
						g += 50
					elif r == 250 and g == 250 and b < 250:
						r = 0
						g = 0
						b += 50	
				if event.key == pygame.K_LEFT:
					if b > 0:
						b -= 50
					elif b == 0 and g > 0:
						b = 250
						g -= 50
					elif b == 0 and g == 0 and r > 0:
						b = 250
						g = 250
						r -= 50
				color = (r,g,b)		
				
			
			#####DRAWING WITH MOUSE 
			if click[0] == 1:
				pygame.draw.rect(gameDisplay, color, (mouse[0], mouse[1], 3, 3))
			elif click[2] == 1:
				pygame.draw.rect(gameDisplay, black, (mouse[0]-25, mouse[1]-25, 50, 50))
			
			button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)
			button("Erase All", 10, 550, 100, 30, red, bright_red, eraseAll)
			button("line", 240, 10, 100, 30, blue, bright_blue, drawLine)
			button("Spectrum", 360, 10, 100, 30, red, bright_red, spectrum)
			pygame.display.update()
			clock.tick(50000)
				
def eraseAll():
	gameDisplay.fill(black)

def quit_paint():
	pygame.quit()
	quit()
	
def game_loop():
	
	game = True
	while game: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		button("DRAW", 10, 10, 100, 30, green, bright_green, freeDraw)
		button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)

		
		pygame.display.update()
		clock.tick(10)
	

game_loop()
pygame.quit()
quit()

#make rotating dots and create patterns

	
	
	
	
