'''
death screen
main menu(1p or 2p)
score
music and sound
pvp in 2p
online 2p
'''

import pygame
import gameClass

pygame.mixer.pre_init(48000, 16, 2, 4096)
pygame.init()
clock = pygame.time.Clock()

display_width = 900
display_height = 600
DISPLAY = pygame.display.set_mode([display_width, display_height]) 

# score = 0
P1timeSinceLastUpdate = 0
P2timeSinceLastUpdate = 0
lastFrameMillis = 0
fps = 60

pygame.display.set_caption('TETORISU')

player1 = gameClass.Tetrisapp() 
player2 = gameClass.Tetrisapp()


playing = False
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
            break
    
        elif (event.type == pygame.KEYDOWN):
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pygame.quit()
            elif key[pygame.K_a]:
                player1.thisPieceX -= 1
                if player1.thisPieceX < 0 or player1.colliding():
                    player1.thisPieceX += 1
            elif key[pygame.K_d]:
                player1.thisPieceX += 1
                if player1.thisPieceX + len(player1.thisPieceShape) > 10 or player1.colliding():
                    player1.thisPieceX -= 1
            elif key[pygame.K_s]:
                player1.update()
                P1timeSinceLastUpdate = pygame.time.get_ticks()
            elif key[pygame.K_w]:
                player1.rotatePiece()
                if player1.colliding():
                    for i in range(3):
                        player1.rotatePiece()
            elif key[pygame.K_LEFT]:
                player2.thisPieceX -= 1
                if player2.thisPieceX < 0 or player2.colliding():
                    player2.thisPieceX += 1
            elif key[pygame.K_RIGHT]:
                player2.thisPieceX += 1
                if player2.thisPieceX + len(player2.thisPieceShape) > 10 or player2.colliding():
                    player2.thisPieceX -= 1
            elif key[pygame.K_DOWN]:
                player2.update()
                P2timeSinceLastUpdate = pygame.time.get_ticks()
            elif key[pygame.K_UP]:
                player2.rotatePiece()
                if player2.colliding():
                    for i in range(3):
                        player2.rotatePiece()
    
    
    player1.update()
    player2.update()
    player1.show(DISPLAY, 100, 0)
    player2.show(DISPLAY, 500, 0)

    pygame.display.update()
    clock.tick_busy_loop(60) 

    try:
        fps = 1000 / (pygame.time.get_ticks() - lastFrameMillis)
    except:
        fps = 1000
    pygame.display.set_caption('TETORISU fps = ' + str(int(fps)))
    lastFrameMillis = pygame.time.get_ticks()