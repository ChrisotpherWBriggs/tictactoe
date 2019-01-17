import pygame
import os
import math
import sys
sys.path.insert(0,"C:\\Users\\CBriggs\\Desktop\\pygame")
from colors import *
from boxes import *

pygame.init()
os.chdir("C:\\Users\\CBriggs\\Desktop\\pygame")
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Shapes")

clock = pygame.time.Clock()

running = True
x_img = pygame.image.load('x.png')

o_img = pygame.image.load('o.png')
#white = (255,255,255)

x = int((display_width - 450) * 0.5)
y = int((display_height - 450) * 0.5)

board = [0,0,0,0,0,0,0,0,0,0]

pygame.font.init()
myfont = pygame.font.SysFont('Gorgia', 36)
textsurface = myfont.render("X's Win", False,(0,0,0))
textsurface2 = myfont.render("O's Win", False,(0,0,0))

def checkWin():
    if board[1] % 2 != 0 and board[2]  % 2 != 0 and board[3] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 150), (625, 150), 3)
    elif board[1] != 0 and board[1] % 2 == 0 and board[2] != 0 and board[2]  % 2 == 0 and  board[3] != 0 and board[3] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 150), (625, 150), 3)
    elif board[4] % 2 != 0 and board[5]  % 2 != 0 and board[6] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 300), (625, 300), 3)
    elif board[4] != 0 and board[4] % 2 == 0 and board[5] != 0 and board[5]  % 2 == 0 and  board[6] != 0 and board[6] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 300), (625, 300), 3)
    elif board[7] % 2 != 0 and board[8]  % 2 != 0 and board[9] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 450), (625, 450), 3)
    elif board[7] != 0 and board[7] % 2 == 0 and board[8] != 0 and board[8]  % 2 == 0 and  board[9] != 0 and board[9] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 450), (625, 450), 3)
    elif board[1] % 2 != 0 and board[4]  % 2 != 0 and board[7] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (250, 75), (250, 525), 3)
    elif board[1] != 0 and board[1] % 2 == 0 and board[4] != 0 and board[4]  % 2 == 0 and  board[7] != 0 and board[7] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (250, 75), (250, 525), 3)
    elif board[2] % 2 != 0 and board[5]  % 2 != 0 and board[8] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (400, 75), (400, 525), 3)
    elif board[2] != 0 and board[2] % 2 == 0 and board[5] != 0 and board[5]  % 2 == 0 and  board[8] != 0 and board[8] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (400, 75), (400, 525), 3)
    elif board[3] % 2 != 0 and board[6]  % 2 != 0 and board[9] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (550, 75), (550, 525), 3)
    elif board[3] != 0 and board[3] % 2 == 0 and board[6] != 0 and board[6]  % 2 == 0 and  board[9] != 0 and board[9] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (550, 75), (550, 525), 3)
    elif board[1] % 2 != 0 and board[5]  % 2 != 0 and board[9] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 75), (625, 525), 3)
    elif board[1] != 0 and board[1] % 2 == 0 and board[5] != 0 and board[5]  % 2 == 0 and  board[9] != 0 and board[9] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (175, 75), (625, 525), 3)
    elif board[3] % 2 != 0 and board[5]  % 2 != 0 and board[7] % 2 != 0:
        gameDisplay.blit(textsurface, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (625, 75), (175, 525), 3)
    elif board[3] != 0 and board[3] % 2 == 0 and board[5] != 0 and board[5]  % 2 == 0 and  board[7] != 0 and board[7] % 2 == 0:
        gameDisplay.blit(textsurface2, (175,10))
        pygame.draw.line(gameDisplay, colors['black'], (625, 75), (175, 525), 3)
#board[1] = pygame.draw.rect(gameDisplay, (colors['aqua']), pygame.Rect(x, y), (150, 150),3)
#board[2] = pygame.draw.rect(gameDisplay, (colors['blueviolet']), pygame.Rect(x + 150, y, 150, 150),3)
#board[3] = pygame.draw.rect(gameDisplay, (colors['darkslategray']), pygame.Rect(x + 300, y, 150, 150),3)
#board[4] = pygame.draw.rect(gameDisplay, (colors['darkslategray']), pygame.Rect(x, y + 150, 150, 150),3)
#board[5] = pygame.draw.rect(gameDisplay, (colors['aqua']), pygame.Rect(x + 150, y + 150, 150, 150),3)
#board[6] = pygame.draw.rect(gameDisplay, (colors['blueviolet']), pygame.Rect(x + 300, y +150, 150, 150),3)
#board[7] = pygame.draw.rect(gameDisplay, (colors['blueviolet']), pygame.Rect(x, y + 300, 150, 150),3)
#board[8] = pygame.draw.rect(gameDisplay, (colors['darkslategray']), pygame.Rect(x + 150, y + 300, 150, 150),3)
#board[9] = pygame.draw.rect(gameDisplay, (colors['aqua']), pygame.Rect(x + 300, y + 300, 150, 150),3)
turn = 0
while running:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    gameDisplay.fill(colors['white'])
    pygame.draw.line(gameDisplay, colors['black'], (x +150, y), (x + 150, y + 450))
    pygame.draw.line(gameDisplay, colors['black'], (x +300, y), (x + 300, y + 450))
    pygame.draw.line(gameDisplay, colors['black'], (x, y + 150), (x + 450, y + 150))
    pygame.draw.line(gameDisplay, colors['black'], (x, y + 300), (x + 450, y + 300))

    if board[1] != 0 and board[1] % 2 != 0:
        gameDisplay.blit(x_img, (200,100) )
    elif board[1] != 0 and board[1] % 2 == 0:
       gameDisplay.blit(o_img, (200,100) )

    if board[2] != 0 and board[2] % 2 !=0:
        gameDisplay.blit(x_img, (350,100) )
    elif board[2] != 0 and board[2] % 2 ==0:
        gameDisplay.blit(o_img, (350,100) )

    if board[3] != 0 and board[3] % 2 !=0:
        gameDisplay.blit(x_img, (500,100) )
    elif board[3] != 0 and board[3] % 2 ==0:
        gameDisplay.blit(o_img, (500,100) )

    if board[4] != 0 and board[4] % 2 !=0:
        gameDisplay.blit(x_img, (200,250) )
    elif board[4] != 0 and board[4] % 2 == 0:
        gameDisplay.blit(o_img, (200,250) )

    if board[5] != 0 and board[5] % 2 !=0:
        gameDisplay.blit(x_img, (350,250) )
    elif board[5] != 0 and board[5] % 2 ==0:
        gameDisplay.blit(o_img, (350,250) )

    if board[6] != 0 and board[6] % 2 !=0:
        gameDisplay.blit(x_img, (500,250) )
    elif board[6] != 0 and board[6] % 2 ==0:
        gameDisplay.blit(o_img, (500,250) )

    if board[7] != 0 and board[7] % 2 !=0:
        gameDisplay.blit(x_img, (200,400) )
    elif board[7] != 0 and board[7] % 2 ==0:
        gameDisplay.blit(o_img, (200,400) )

    if board[8] != 0 and board[8] % 2 !=0:
        gameDisplay.blit(x_img, (350,400) )
    elif board[8] != 0 and board[8] % 2 ==0:
        gameDisplay.blit(o_img, (350,400) )

    if board[9] != 0 and board[9] % 2 !=0:
        gameDisplay.blit(x_img, (500,400) )
    elif board[9] != 0 and board[9] % 2 ==0:
        gameDisplay.blit(o_img, (500,400) )


    if event.type == pygame.MOUSEBUTTONDOWN:
        pos_x, pos_y  = pygame.mouse.get_pos()
        print("X Position is " + str(pos_x) + "and Position Y is " + str(pos_y))

        if board[1] == 0 and pos_x > box1 and pos_x < box1b and pos_y > box1c and pos_y < box1d and turn % 2 !=0:
            board[1] = turn
            turn += 1
        elif board[1] == 0 and  pos_x > box1 and pos_x < box1b and pos_y > box1c and pos_y < box1d and turn % 2 == 0:
            board[1] = turn
            turn += 1
        if board[2] == 0 and  pos_x > box2 and pos_x < box2b and pos_y > box2c and pos_y < box2d and turn % 2 != 0:
            board[2] = turn
            turn += 1
        elif board[2] == 0 and  pos_x > box2 and pos_x < box2b and pos_y > box2c and pos_y < box2d and turn % 2 == 0:
            board[2] = turn
            turn += 1
        if board[3] == 0 and  pos_x > box3 and pos_x < box3b and pos_y > box3c and pos_y < box3d and turn % 2 != 0:
            board[3] = turn
            turn += 1
        elif board[3] == 0 and  pos_x > box3 and pos_x < box3b and pos_y > box3c and pos_y < box3d and turn % 2 == 0:
            board[3] = turn
            turn += 1
        if board[4] == 0 and  pos_x > box4 and pos_x < box4b and pos_y > box4c and pos_y < box4d and turn %2 != 0:
            board[4] = turn
            turn += 1
        elif board[4] == 0 and  pos_x > box4 and pos_x < box4b and pos_y > box4c and pos_y < box4d and turn %2 == 0:
            board[4] = turn
            turn += 1
        if board[5] == 0 and  pos_x > box5 and pos_x < box5b and pos_y > box5c and pos_y < box5d and turn % 2 != 0:
            board[5] = turn
            turn += 1
        elif board[5] == 0 and  pos_x > box5 and pos_x < box5b and pos_y > box5c and pos_y < box5d and turn %2 == 0:
            board[5] = turn
            turn += 1
        if board[6] == 0 and  pos_x > box6 and pos_x < box6b and pos_y > box6c and pos_y < box6d and turn % 2 != 0:
            board[6] = turn
            turn +=1
        elif board[6] == 0 and  pos_x > box6 and pos_x < box6b and pos_y > box6c and pos_y < box6d and turn % 2 == 0:
            board[6] = turn
            turn += 1
        if board[7] == 0 and  pos_x > box7 and pos_x < box7b and pos_y > box7c and pos_y < box7d and turn % 2 !=0:
            board[7] = turn
            turn += 1
        elif board[7] == 0 and  pos_x > box7 and pos_x < box7b and pos_y > box7c and pos_y < box7d and turn % 2 == 0:
            board[7] = turn
            turn +=1
        if board[8] == 0 and  pos_x > box8 and pos_x < box8b and pos_y > box8c and pos_y < box8d and turn % 2 !=0:
            board[8] = turn
            turn +=1
        elif board[8] == 0 and  pos_x > box8 and pos_x < box8b and pos_y > box8c and pos_y < box8d and turn % 2 ==0:
            board[8] = turn
            turn +=1
        if board[9] == 0 and  pos_x > box9 and pos_x < box9b and pos_y > box9c and pos_y < box9d and turn % 2 !=0:
            board[9] = turn
            turn += 1
        elif board[9] == 0 and  pos_x > box9 and pos_x < box9b and pos_y > box9c and pos_y < box9d and turn % 2 == 0:
            board[9] = turn
            turn +=1


    print("turn is " + str(turn))
    print("board 1 is " + str(board[1]))
    print("board 2 is " + str(board[2]))
    print("board 3 is " + str(board[3]))
    print("board 4 is " + str(board[4]))
    print("board 5 is " + str(board[5]))
    print("board 6 is " + str(board[6]))
    print("board 7 is " + str(board[7]))
    print("board 8 is " + str(board[8]))
    print("board 9 is " + str(board[9]))




    checkWin()
    pygame.display.flip()
    clock.tick(18)

pygame.quit()