import pygame as pg
import random

# INICIALIZING PYGAME
pg.init()

# ___________VARIABLES___________

clock = pg.time.Clock()
velocity = 15

# Colors
white = (255, 255, 255) # QUADRADO
black = (0, 0, 0) # FUNDO
red = (255,0,0) # PONTO

# Display
window = pg.display.set_mode((1280, 720))

# Player Position
player_pos = pg.Vector2(window.get_width() / 2, window.get_height() / 2)

# ___________FUNCTIONS___________

# Position x and y of point
def pos_point():
     x = random.randrange(1, 1280 - 10)
     y = random.randrange(1, 720 - 10)
     return x, y

# Draw a point
def create_point(p_x, p_y):
    return pg.draw.rect(window, red, pg.Rect(p_x, p_y, 10, 10))

def play_game():
    running = True
    
    #Count
    count = 0
    
    # Position of point
    p_x, p_y = pos_point()
    
    while running:
        window.fill(black)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        square = pg.draw.rect(window, white, pg.Rect(player_pos.x - 70, player_pos.y - 70, 70, 70))

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player_pos.y -= 15
        if keys[pg.K_s]:
            player_pos.y += 15
        if keys[pg.K_a]:
            player_pos.x -= 15
        if keys[pg.K_d]:
            player_pos.x += 15
        
        point = create_point(p_x, p_y)

        pg.display.flip()
        
        if square.colliderect(point):
            p_x, p_y = pos_point()
            count += 1
            
        if count == 5:
            running = False
        
        clock.tick(velocity)
    pg.quit()

play_game()