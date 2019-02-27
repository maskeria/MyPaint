import pygame
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
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
	
	textSurf, textRect = textObjects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)

#def spectrum():
#loop to make the buttons and return the chosen color
#choice = True
#while choice:
	
	
def chooseColor(mouse, click, color):
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
			
	return color		
		
def drawLine():
	one = False
	two = False
	order = False
	clickOne = (0,0)
	clickTwo = (0,0)
	r = 250
	g = 250
	b = 250
	color = (r,g,b)
	
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
	r = 250
	g = 250
	b = 250
	color = (r,g,b)
	
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
				
			print(color)
			#####DRAWING WITH MOUSE 
			if click[0] == 1:
				pygame.draw.rect(gameDisplay, color, (mouse[0], mouse[1], 3, 3))
			elif click[2] == 1:
				pygame.draw.rect(gameDisplay, black, (mouse[0]-25, mouse[1]-25, 50, 50))
			
			button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)
			button("Erase All", 10, 550, 100, 30, red, bright_red, eraseAll)
			button("line", 240, 10, 100, 30, blue, bright_blue, drawLine)
			pygame.display.update()
			clock.tick(500)
				
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

	
	
	
	
