import pygame as pg
pg.init()

pg.display.set_mode((1200,500))
pg.display.set_caption("PYGAME TUTORIAL")

exit_game=False
game_over=False

# create a game loop
while not exit_game:
    for event in pg.event.get():
        print(event)

#infinite loop 
pg.quit()
quit()