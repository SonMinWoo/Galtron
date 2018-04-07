import pygame as pg
<<<<<<< HEAD
=======

>>>>>>> 680715a2841b571424a13107d9077d9d96c2738e
from settings import Settings

setting = Settings()
screen = pg.display.set_mode((setting.screenWidth, setting.screenHeight))

<<<<<<< HEAD
 # load and change images
def introimages():
    while (pg.time.get_ticks() < 3000):

=======

# load and change images
def introimages():
    while (pg.time.get_ticks() < 3000):
>>>>>>> 680715a2841b571424a13107d9077d9d96c2738e
        image = pg.image.load("gfx/intro1.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(400)

        image = pg.image.load("gfx/intro2.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(400)

        image = pg.image.load("gfx/intro3.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(400)

        image = pg.image.load("gfx/intro4.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(400)

        image = pg.image.load("gfx/intro5.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(400)

        image = pg.image.load("gfx/intro6.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(400)

        image = pg.image.load("gfx/intro7.png")
        image = pg.transform.scale(image, (setting.screenWidth, setting.screenHeight))
        rect = image.get_rect()
        screen.fill(setting.bgColor)
        screen.blit(image, rect)
        pg.display.update()
        pg.time.wait(600)
