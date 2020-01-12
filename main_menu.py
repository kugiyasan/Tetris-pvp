import pygame
import pygameMenu
import sys, os
import tetris

def bgFill():
    global DISPLAY
    DISPLAY.fill((20, 20, 20))

def startGame(playerNumber):
    main_menu.disable()
    main_menu.reset(1)
    path = os.path.dirname(sys.argv[0])
    pygame.mixer.music.load(path + '/tetris-99-main-theme.mp3')
    pygame.mixer.music.play(-1)

    tetris.runGame(DISPLAY, playerNumber)

def change_volume(value, volume): # selected='1', index=1, volume='LOW'
    selected, index = value
    pygame.mixer.music.set_volume(index / 10)

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
clock = pygame.time.Clock()

display_width = 900
display_height = 600
DISPLAY = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('TETORISU')

main_menu = pygameMenu.Menu(DISPLAY, display_width, display_height, 'fonts/Roboto-Regular.ttf', 'TETRIS', bgfun=bgFill)
play_menu = pygameMenu.Menu(DISPLAY, display_width, display_height, 'fonts/Roboto-Regular.ttf', 'PLAY', bgfun=bgFill)
options_menu = pygameMenu.Menu(DISPLAY, display_width, display_height, 'fonts/Roboto-Regular.ttf', 'OPTIONS', bgfun=bgFill)
# about_menu = pygameMenu.TextMenu(DISPLAY, display_width, display_height, 'fonts/Roboto-Regular.ttf', 'TETRIS', bgfun=bgFill)

main_menu.add_option('Play', play_menu)
main_menu.add_option('Options', options_menu)
# main_menu.add_option('About', lambda:print('About the game!'))
main_menu.add_option('Quit', pygameMenu.events.EXIT)

play_menu.add_option('Single Player', lambda:startGame(1))
play_menu.add_option('Two Players', lambda:startGame(2))
play_menu.add_option('Online Game', lambda:print('Feature not implemented yet'))
play_menu.add_option('Back', pygameMenu.events.BACK)

options_menu.add_selector('Master Volume',
                           [('0', 'MUTE'), ('1', 'LOW'), ('2', 'LOW'), ('3', 'LOW'),
                            ('4', 'MED'), ('5', 'MED'), ('6', 'MED'),
                            ('7', 'HIGH'), ('8', 'HIGH'), ('9', 'HIGH'), ('10', 'MAX'),],
                           onchange=change_volume, default=5)
options_menu.add_option('Back', pygameMenu.events.BACK)

running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
            break
    
        elif (event.type == pygame.KEYDOWN):
            pass
    
        main_menu.mainloop(event)
        pygame.display.update()

    try:
        fps = 1000 / clock.tick_busy_loop(60) 
    except:
        fps = 1000
    pygame.display.set_caption('TETORISU fps = ' + str(int(fps)))