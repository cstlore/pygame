import pygame as pg
from random import randrange
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False
background_colour = (156, 229, 255)
RES = WIDTH, HEIGHT = 1000, 600
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)
#физика предметов
space = pymunk.Space()
space.gravity = 0, 8000
segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 150)
space.add(segment_shape)
segment_shape.elasticity = 0.4
segment_shape.friction = 1.0

while True:
    surface.fill(background_colour)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)
