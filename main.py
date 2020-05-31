import pygame
# from colours import *
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (150,20,20)
br_red = (255,0,0)
green = (78,164,40)
br_green = (0,255,0)
blue = (46,46,158)
br_blue = (0,0,255)
gray = (200,200,200)
yellow = (255,255,0)
orange = (255, 168, 64)
brown = (128, 64, 0)

display_width = 512
display_height = 512

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Exotic Recipes from East India!')

clock = pygame.time.Clock()
FPS = 10


def fix(a):
	if(a==3):
		return 2
	else:
		return a

smallfont = pygame.font.SysFont('timesnewroman', 20)
medfont = pygame.font.SysFont('blackadderitc', 45)
larfont = pygame.font.SysFont('comicsansms', 80)

def text_objects(text, colour,size):
    if size == 'small':
        textSurface=smallfont.render(text,True, colour)
    if size == 'medium':
        textSurface=medfont.render(text,True, colour)
    if size == 'large':
        textSurface=larfont.render(text,True, colour)

    return textSurface, textSurface.get_rect()
    

def message_to_screen(msg,colour, x_displace=0, y_displace = 0, size ='small'):
    textSurf, textRect = text_objects(msg,colour, size)
##    screen_text = font.render(msg, True, colour)
##    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width/2)+x_displace, (display_height / 2)+y_displace
    gameDisplay.blit(textSurf,textRect)


class Sprite:
	def __init__(self, sheet, size):
		self.sheet = pygame.transform.scale(pygame.image.load("Sprites/" + sheet + ".png"), [100, 130])
		self.size = size
		self.sprite = pygame.image.load("Sprites/trans.png")
		self.sprite = pygame.transform.scale(self.sprite, size)
		self.move = 0
		self.frameCounter = 0
		self.frame = 0


	def display(self, j, flip = False, move = False):
		self.sprite.fill((0, 0, 0, 0))
		if not move:
			self.sprite.blit(self.sheet, (0, 0), (0, (self.size[1]+1)*j, self.size[0], self.size[1]))
			self.move = 0
			self.frameCounter = 0
		else:
			if self.frameCounter == 0:
				self.frameCounter = time.clock()
			if time.clock() >= self.frameCounter:
				self.frameCounter += 0.2
				self.frame += 1
				self.frame %= 2
			self.sprite.blit(self.sheet, (0, 0), ((self.size[0]+2)*(self.frame+1), (self.size[1]+2)*j, self.size[0], self.size[1]))



		if flip:
			self.sprite = pygame.transform.flip(self.sprite, True, False)

		return self.sprite


player = Sprite("Red", (32, 42))
f1 = pygame.transform.scale(pygame.image.load("Sprites/F1.png"), (int(display_width), int(display_height/7)))
f2 = pygame.transform.scale(pygame.image.load("Sprites/F2.png"), (int(display_width), int(display_height*3/7)))


def gameLoop():
	gameExit = False
	gameOver = False
	direction = 0
	movem = False
	allowed = ((5, 1), (5, 2), (6, 1), (6, 2), (7, 2), (8, 1), (8, 2), (9, 0), (9, 1), (10, 0), (10, 1), (11, 0), (11, 1), (11, 2), (12, 1), (12, 2))

	bmap = pygame.transform.scale(pygame.image.load("Sprites/FMap.png"), [1154, 642])
	e1 = pygame.transform.scale(pygame.image.load("Sprites/E1.png"), [32, 42])
	bmap.blit(e1, (20*32, 6*42+15))
	e2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/E2.png"), [32, 42]), True, False)
	bmap.blit(e2, (12*32, 8*42))
	e3 = pygame.transform.scale(pygame.image.load("Sprites/E3.png"), [32, 42])
	bmap.blit(e3, (17*32, 6*42-15))
	e4 = pygame.transform.scale(pygame.image.load("Sprites/E4.png"), [32, 42])
	bmap.blit(e4, (21*32, 8*42+8))
	e5 = pygame.transform.scale(pygame.image.load("Sprites/E5.png"), [32, 42])
	bmap.blit(e5, (14*32, 6*42+20))

	# bmap = pygame.transform.scale(bmap, (display_width*3, display_height*3))
	# x, y = int(display_width*3/2), int(display_height*3/2)
	x, y = 6*32, 2*42

	while not gameExit:
		talk = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					direction = 2
					movem = True
					# x-=32
				elif event.key == pygame.K_RIGHT:
					direction = 3
					movem = True
					# x+=32
					 
				elif event.key == pygame.K_UP:
					direction = 1
					movem = True
					# y-=42
				elif event.key == pygame.K_DOWN:
					direction = 0
					movem = True
				elif event.key == pygame.K_z:
					talk = True
					# y+=42
			# if event.type == pygame.KEYUP:
			#     if event.key == pygame.K_LEFT:
			#         direction = 2
			#         movem = False
			#     elif event.key == pygame.K_RIGHT:
			#         direction = 3
			#         movem = False
					 
			#     elif event.key == pygame.K_UP:
			#         direction = 1
			#         movem = False
			#     elif event.key == pygame.K_DOWN:
			#         direction = 0
			#         movem = False
		key = pygame.key.get_pressed()
		if not (key[pygame.K_LEFT]+key[pygame.K_DOWN]+key[pygame.K_UP]+key[pygame.K_RIGHT]):
			movem = False

		if movem:
			if(direction==0 or direction==1):
				if(x/32, y/42+(-2*direction+1)) in allowed:
					y+=(-2*direction+1)*42
			else:
				if(x/32+(2*direction-5), y/42) in allowed:
					x+=(2*direction-5)*32

		gameDisplay.blit(bmap, (0, 0), (x, y, x+display_width, y+display_height))
		gameDisplay.blit(player.display(fix(direction), flip = (direction==3), move = movem), (int(display_height/2), int(display_width/2)))

		pause = True
		msg = 0

		if talk:
			if(x, y) == (11*32, 0*42) and direction == 3:
				while pause:
					if msg == 0:
						gameDisplay.blit(f1, (0, display_height*6/7))
						message_to_screen("Do you want to learn the recipe of 'Tetor Daal'? (Y/N)", black, y_displace = int(display_height*3/7))
					elif msg == 1:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Moong Dal", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("2.Bottle Gourd", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("3.Bitter Gourd", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("4.Mustard, Methi, Turmeric", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("5.Salt", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("6.Mustard Oil, Red Chili, Green Chili", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 2:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1. Chop up the bottle gourd and ", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("the bitter gourd into small pieces.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("2. Boil the moong dal and the bottle gourd.", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("3. Heat some mustard oil on a pan ", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("and add some mustard, methi and red chili.", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 3:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("4. Add the chopped bitter gourd in the boiling oil", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("and fry for a couple of minutes.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("5. Add some ginger paste ", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("and turmeric with the fried bitter gourd.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("6. Add the boiled dal and bottle gourd mixture.", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("7. Serve with rice.", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					else:
						pause = False
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								msg+=1
							elif event.key == pygame.K_n:
								pause = False

					pygame.display.update()
					clock.tick(FPS)
			if(x, y) == (12*32, 1*42) and direction == 1:
				while pause:
					if msg == 0:
						gameDisplay.blit(f1, (0, display_height*6/7))
						message_to_screen("Do you want to learn the recipe of 'Tetor Daal?' (Y/N)", black, y_displace = int(display_height*3/7))
					elif msg == 1:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Moong Dal", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("2.Bottle Gourd", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("3.Bitter Gourd", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("4.Mustard, Methi, Turmeric", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("5.Salt", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("6.Mustard Oil, Red Chili, Green Chili", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 2:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1. Chop up the bottle gourd and ", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("the bitter gourd into small pieces.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("2. Boil the moong dal and the bottle gourd.", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("3. Heat some mustard oil on a pan ", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("and add some mustard, methi and red chili.", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 3:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("4. Add the chopped bitter gourd in the boiling oil", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("and fry for a couple of minutes.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("5. Add some ginger paste ", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("and turmeric with the fried bitter gourd.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("6. Add the boiled dal and bottle gourd mixture.", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("7. Serve with rice.", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					else:
						pause = False
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								msg+=1
							elif event.key == pygame.K_n:
								pause = False

					pygame.display.update()
					clock.tick(FPS)
			if(x, y) == (5*32, 2*42) and direction == 2:
				while pause:
					if msg == 0:
						gameDisplay.blit(f1, (0, display_height*6/7))
						message_to_screen("Do you want to learn the recipe of 'Chanar Dalna'? (Y/N)", black, y_displace = int(display_height*3/7))
					elif msg == 1:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Milk", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("2.Lemon", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("3.Maida", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("4.Sunflower Oil", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("5.Jeera, Cinnamon, Cardamom and Clove", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("6.Bayleaf, Ginger paste, Jeera powder, Coriander Powder", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 2:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Add a few drops of lemon juice in the milk", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("and keep it aside and wait for it to curdle.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("Remove the extra water and dry it.", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("2. Add a pinch of Maida and mix it. Make small balls out of it.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("3. Heat some sunflower oil and then fry the balls lightly", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen(" and then keep them aside.", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 3:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("4. In the same oil, add Jeera, Bayleaf, Cinnamon,", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen(" Cardamom and Clove and fry it slightly.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("5. Add some ginger paste ", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("and turmeric with the fried bitter gourd.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("5. Add some ginger paste, jeera powder,", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen(" coriander Powder, turmeric and fry it for a while.", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 4:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("6. Add some curd to it.", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("7. After a couple of minutes, add some water.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("8. Once the water starts boiling, add the balls ", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("made in step 2 and cover it with a lid.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("9. After it cooks for a few minutes,", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen(" Chanar Dalna is ready to be served!", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					else:
						pause = False
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								msg+=1
							elif event.key == pygame.K_n:
								pause = False

					pygame.display.update()
					clock.tick(FPS)
			if(x, y) == (9*32, 0*42) and direction == 1:
				while pause:
					if msg == 0:
						gameDisplay.blit(f1, (0, display_height*6/7))
						message_to_screen("Do you want to learn the recipe of 'Gota Shedho'?(Y/N)", black, y_displace = int(display_height*3/7))
					elif msg == 1:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Black Urad Dal (Whole)", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("2.Peas", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("3.Flat Beans", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("4.White Brinjal (Small)", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("5.Mustard Oil", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("6.Green Chili and Salt", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 2:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1. Soak the black urad dal in water for a couple of hours.", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("the bitter gourd into small pieces.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("2. Boil the vegetables (whole) and the dal ", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("until it develops a soft texture (approx 1 hour) on a low flame.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("3. Serve the boiled mixture ", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("with rice, mustard oil and green chili", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					else:
						pause = False
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								msg+=1
							elif event.key == pygame.K_n:
								pause = False

					pygame.display.update()
					clock.tick(FPS)
			if(x, y) == (12*32, 2*42) and direction == 3:
				while pause:
					if msg == 0:
						gameDisplay.blit(f1, (0, display_height*6/7))
						message_to_screen("Do you want to learn the recipe of 'Palang Ghonto'? (Y/N)", black, y_displace = int(display_height*3/7))
					elif msg == 1:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Spinach", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("2.Flat Beans", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("3.Potato", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("4.Brinjal", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("5.Raddish", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("6.Mustard Oil, Jeera Powder, Ginger Paste", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 2:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("7. Salt, Green Chili", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("8. Sugar", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("9. Fried Bori", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 3:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1. Boil the Spinach and crush it.", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("and fry for a couple of minutes.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("2. Cut the Fried Beans, Potato, Brinjal", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("and Raddish into small pieces and fry them in mustard oil.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("3. Add some Jeera powder and Ginger paste.", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("4. After a couple of minutes, add the crushed spinach.", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 4:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("5. Add some green chili, salt and sugar to taste.", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("6. Add some fried bori.", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("7. Serve with rice.", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					else:
						pause = False
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								msg+=1
							elif event.key == pygame.K_n:
								pause = False

					pygame.display.update()
					clock.tick(FPS)			
			if(x, y) == (6*32, 1*42) and direction == 1:
				while pause:
					if msg == 0:
						gameDisplay.blit(f1, (0, display_height*6/7))
						message_to_screen("Do you want to learn the recipe of 'Aam Pora Shorbot'?(Y/N)", black, y_displace = int(display_height*3/7))
					elif msg == 1:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("INGREDIENTS : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1.Mango", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("2.Mustard Oil", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("3.Sugar", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("4.Black Salt", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					elif msg == 2:
						gameDisplay.blit(f2, (0, display_height*4/7))
						message_to_screen("RECIPE : ", black, y_displace = int(display_height)*1/9)
						message_to_screen("1. Wash the mango, dry it and apply mustard oil on it.", black, y_displace = int(display_height*(1/9+1/20)))
						message_to_screen("Note - Do not peel the skin", black, y_displace = int(display_height*(1/9+2/20)))
						message_to_screen("2. Put the mango on a flame and wait for it to burn.", black, y_displace = int(display_height*(1/9+3/20)))
						message_to_screen("3. After that side is sufficiently burnt, turn it over.", black, y_displace = int(display_height*(1/9+4/20)))
						message_to_screen("4. Remove the skin from the burnt mango.", black, y_displace = int(display_height*(1/9+5/20)))
						message_to_screen("5. Mix the mango in water, add sugar, salt and mix throughly.", black, y_displace = int(display_height*(1/9+6/20)))
						message_to_screen("Press 'Y' to continue", black, y_displace = int(display_height*(1/9+7/20)))
					else:
						pause = False
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								msg+=1
							elif event.key == pygame.K_n:
								pause = False

					pygame.display.update()
					clock.tick(FPS)

		
		# sp.fill((0, 0, 0, 0))
		# sp.blit(img, (0, 0), (0, (21+1)*fix(direction), 16, 21))

		# if(direction != 3):
		# 	gameDisplay.blit(sp, (50, 50))
		# else:
		# 	gameDisplay.blit(pygame.transform.flip(sp, True, False), (50, 50))
				 

		pygame.display.update()
		clock.tick(FPS)


gameLoop()
pygame.quit()
quit()