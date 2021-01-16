'''
death screen
main menu(1p or 2p)
score
music and sound
pvp in 2p
online 2p
'''

import pygame
import sys, os
import gameClass

def runGame(DISPLAY, playerNumber):
    players = list()
    # for i in range(playerNumber):
    #     players.append(gameClass.Tetrisapp())
    players.append(gameClass.Tetrisapp())
    players.append(gameClass.Tetrisapp())

    key_actions = { 'ESCAPE':   pygame.quit,
                    'w':        players[0].rotatePiece,
                    'a':        lambda:players[0].move(-1),
                    's':        players[0].drop,
                    'd':        lambda:players[0].move(1),
                    'UP':       players[1].rotatePiece,
                    'LEFT':     lambda:players[1].move(-1),
                    'DOWN':     players[1].drop,
                    'RIGHT':    lambda:players[1].move(1)}

    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
                break
        
            elif (event.type == pygame.KEYDOWN):
                for key in key_actions:
                    if event.key == eval("pygame.K_"+key):
                        key_actions[key]()

        players[0].update()
        players[0].show(DISPLAY, 100, 0)
        if playerNumber == 2:
            players[1].update()
            players[1].show(DISPLAY, 500, 0)

        pygame.display.update()
        
        try:
            fps = 1000 / clock.tick(60) 
        except:
            fps = 1000
        pygame.display.set_caption('TETORISU fps = ' + str(int(fps)))



if __name__ == "__main__":
    pygame.mixer.pre_init(48000, 16, 2, 4096)
    pygame.init()
    clock = pygame.time.Clock()

    display_width = 900
    display_height = 600
    DISPLAY = pygame.display.set_mode([display_width, display_height])
    pygame.display.set_caption('TETORISU')

    path = os.path.dirname(sys.argv[0])
    pygame.mixer.music.load(path + '/tetris-99-main-theme.mp3')
    pygame.mixer.music.play(-1)

    runGame(DISPLAY, 2)
