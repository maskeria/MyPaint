import pygame

pygame.init()

display_width = 500
display_height = 500

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
		if click[0] == 1 and action != None:
			action()
	
	else:
		pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
		
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)
	
	
loop = True 
while loop:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	pixAr = pygame.PixelArray(gameDisplay)
	
	
	print(click + mouse)
	if click[0] == 1:
		pixAr[mouse[0]][mouse[1]] = green ## this works but the pixels are too small. better to make a rectangle instead
		
	
	
	pygame.display.update()
	clock.tick(100)
	
	
	
	
	
	
	
	
	
	