import pygame as pg
pg.init()
pg.display.set_mode((1200,500))
pg.display.set_caption("PYGAME TUTORIAL")
exit_game=False
game_over=False

while not exit_game:
    for event in pg.event.get():
        #key handling
        if event.type==pg.QUIT:
            exit_game=True

        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                print("Successfully Right Key")

pg.quit()
quit()