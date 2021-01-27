import pygame
import os
import math
import random
#setup display
pygame.init()
WIDTH,HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pname  = input("ENTER PLAYER NAME:")
#button variables
RADIUS = 20
GAP = 15
A = 65
letters = []
startx = round((WIDTH-(RADIUS*2+GAP)*12-2*RADIUS)/2)
starty = 400
for i in range(26):
    x = startx + RADIUS + ((RADIUS*2+GAP)*(i%13))
    y = starty + ((i//13))*(GAP+RADIUS*2)
    letters.append([x,y,chr(A+i),True])
#fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
#loading images
images = []
for i in range(7):
    image =pygame.image.load("hangman"+str(i)+".png")
    images.append(image)
#print(images)
#colors
WHITE = (250,250,250)
BLACK = (0,0,0)
#game variables
hangman_status = 0
words = ["IRON","MAN","BLUES","REDDYS"]
word = random.choice(words)
guessed = []
#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE) #to fill the background
    # draw title
    text = TITLE_FONT.render("PLAYER : "+ pname , 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))
    #draw buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
          pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)#for drawing the circle with centre x,y thickness 3 and radius with black color
          text = LETTER_FONT.render(ltr,1,BLACK)#to draw the text
          win.blit(text,(x - text.get_width()/2,y - text.get_height()/2))#for aligning the text within the circle
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

while run:
    clock.tick(FPS) #making the game to have the same FPS
    draw() #to draw all icons to the screen
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):#to end the game when we close it
            run = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                  dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)#checking if my click is within the circle itself or not
                  if dis < RADIUS: #collision condition
                    letter[3] = False#we want to change the original variable value and not the copy of it
                    guessed.append(ltr)
                    if ltr not in word:
                        hangman_status+=1
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("CONGRATS YOU WON!!")
            break
        if hangman_status == 6:
            display_message("SORRY YOU LOST!!")
            break

pygame.quit()