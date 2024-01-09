import pygame

pygame.init()
pygame.display.set_caption('Puck Dodge')

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((1920, 1080))

#import and play music
file = "assets\James Bond-ScoutingForGirls.mp3"
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.01)
pygame.event.wait()

# create player character and border
player = pygame.Rect(65, 70, 15, 15)
game_border = pygame.Rect(0, 0, 1920, 1080)

# safe zones
outside_UL_safezone = pygame.Rect(0, 0, 150, 150)
outside_UR_safezone = pygame.Rect(1770, 0, 150, 150)
outside_LR_safezone = pygame.Rect(1770, 930, 150, 150)
outside_LL_safezone = pygame.Rect(0, 930, 150, 150)
ul_second_level_safezone = pygame.Rect(0, 150, 150, 150)
ur_second_level_safezone = pygame.Rect(1620, 150, 150, 150)
lr_second_level_safezone = pygame.Rect(1620, 780, 150, 150)
ll_second_level_safezone = pygame.Rect(150, 780, 150, 150)
ul_third_level_safezone = pygame.Rect(150, 300, 150, 150)
ur_third_level_safezone = pygame.Rect(1470, 300, 150, 150)

# goal zone
goal = pygame.Rect(1320, 450, 150, 180)

# lanes
bottomlane = pygame.Rect(0, 930, 1980, 150)
leftlane = pygame.Rect(0, 0, 150, 1980)
rightlane = pygame.Rect(1770, 0, 150, 1080)
toplane = pygame.Rect(0, 0, 1920, 150)
second_level_toplane = pygame.Rect(0, 150, 1770, 150)
second_level_rightlane = pygame.Rect(1620, 150, 150, 780)
second_level_bottomlane = pygame.Rect(150, 780, 1620, 150)
second_level_leftlane = pygame.Rect(150, 300, 150, 500)
third_level_toplane = pygame.Rect(150, 300, 1470, 150)
third_level_finallane = pygame.Rect(300, 450, 1320, 330)


movement_speed = float(2)
run = True


while run:
    # background color
    screen.fill('black')
    
    # draw lanes, safe zones, and goal
    pygame.draw.rect(screen, ('white'), toplane)
    pygame.draw.rect(screen, ('white'), rightlane)
    pygame.draw.rect(screen, ('white'), bottomlane)
    pygame.draw.rect(screen, ('white'), leftlane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_toplane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_rightlane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_bottomlane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_leftlane)
    pygame.draw.rect(screen, ('gray86'), third_level_toplane)
    pygame.draw.rect(screen, ('gray75'), third_level_finallane)
    pygame.draw.rect(screen, ('gray'), outside_LL_safezone)    
    pygame.draw.rect(screen, ('gray'), outside_UL_safezone)    
    pygame.draw.rect(screen, ('gray'), outside_UR_safezone)    
    pygame.draw.rect(screen, ('gray'), outside_LR_safezone)
    pygame.draw.rect(screen, ('gray46'), ul_second_level_safezone)
    pygame.draw.rect(screen, ('gray46'), ur_second_level_safezone)
    pygame.draw.rect(screen, ('gray46'), lr_second_level_safezone)
    pygame.draw.rect(screen, ('gray46'), ll_second_level_safezone)    
    pygame.draw.rect(screen, ('gray23'), ul_third_level_safezone)
    pygame.draw.rect(screen, ('gray23'), ur_third_level_safezone)
    pygame.draw.rect(screen, 'red', goal)
    pygame.draw.rect(screen, ('black'), (game_border), 1)
    
    # Wall Lines
    pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)
    pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)
    pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)
    pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)
    pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)
    pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)
    pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)
    pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)
    pygame.draw.line(screen, 'black', (300, 450), (1470, 450), 3)
    pygame.draw.line(screen, 'black', (1470, 450), (1470, 630), 3)
    pygame.draw.line(screen, 'black', (1470, 630), (450, 630), 3)



    pygame.draw.rect(screen, ('green4'), player)

        
    # Diagonal Movement Keybinds
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and key[pygame.K_s] and player.bottom <= 1080 and player.left >= 0:
        player.move_ip(-(0.5 * movement_speed), 0.5 * movement_speed)
    elif key[pygame.K_w] and key[pygame.K_a] and player.top > 0 and player.left >= 0:
        player.move_ip((-0.5 * movement_speed), (-0.5 * movement_speed))
    elif key[pygame.K_w] and key[pygame.K_d] and player.top > 0 and player.right < 1920:
        player.move_ip(0.5 * movement_speed, (-0.5 * movement_speed))
    elif key[pygame.K_d] and key[pygame.K_s] and player.bottom <= 1080 and player.right < 1920:
        player.move_ip(0.5 * movement_speed, (0.5 * movement_speed))
    elif key[pygame.K_a] and key[pygame.K_d]:
        player.move_ip(0, 0)
    elif key[pygame.K_w] and key[pygame.K_s]:
        player.move_ip(0, 0)
    
    
    # Movement Keybinds
    if key[pygame.K_a] == True and player.left >= 0:
        player.move_ip(-(movement_speed), 0)
    elif key[pygame.K_s] == True and player.bottom <= 1080:
        player.move_ip(0, movement_speed)
    elif key[pygame.K_w] == True and player.top > 0:
        player.move_ip(0, -(movement_speed))
    elif key[pygame.K_d] == True and player.right < 1920:
        player.move_ip(movement_speed, 0)
   
   # Top Wall Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)):
        if key[pygame.K_s] == True:
            player.move_ip(0, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)):
        if key[pygame.K_d] and key[pygame.K_s] == True:
            player.move_ip((0.6 * movement_speed), -(movement_speed))
    if player.colliderect(pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)):
        if key[pygame.K_a] and key[pygame.K_s] and player.bottom:
            player.move_ip((0.6 * movement_speed), -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)):
        if key[pygame.K_w] == True:
            player.move_ip(0, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)):
        if key[pygame.K_w] and key[pygame.K_d] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (0, 150), (1770, 150), 3)):
        if key[pygame.K_w] and key[pygame.K_a] == True:
            player.move_ip(movement_speed, movement_speed)

    # Outside Right Wall Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)):
        if key[pygame.K_a] == True:
            player.move_ip(movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)):
        if key[pygame.K_a] and key[pygame.K_s]== True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)):
        if key[pygame.K_a] and key[pygame.K_w]== True:
            player.move_ip(movement_speed, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)):
        if key[pygame.K_d] == True:
            player.move_ip(-movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)):
        if key[pygame.K_d] and key[pygame.K_s]== True:
            player.move_ip(-movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 150), (1770, 930), 3)):
        if key[pygame.K_d] and key[pygame.K_w]== True:
            player.move_ip(-movement_speed, movement_speed)
            
    # Outside Bottom Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)):
        if key[pygame.K_s] == True:
            player.move_ip(0, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)):
        if key[pygame.K_d] and key[pygame.K_s] == True:
            player.move_ip((0.6 * movement_speed), -(movement_speed))
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)):
        if key[pygame.K_a] and key[pygame.K_s] and player.bottom:
            player.move_ip((0.6 * movement_speed), -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)):
        if key[pygame.K_w] == True:
            player.move_ip(0, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)):
        if key[pygame.K_w] and key[pygame.K_d] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1770, 930), (150, 930), 3)):
        if key[pygame.K_w] and key[pygame.K_a] == True:
            player.move_ip(movement_speed, movement_speed)

    # Outside Left Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)):
        if key[pygame.K_a] == True:
            player.move_ip(movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)):
        if key[pygame.K_a] and key[pygame.K_s]== True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)):
        if key[pygame.K_a] and key[pygame.K_w]== True:
            player.move_ip(movement_speed, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)):
        if key[pygame.K_d] == True:
            player.move_ip(-movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)):
        if key[pygame.K_d] and key[pygame.K_s]== True:
            player.move_ip(-movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 930), (150, 300), 3)):
        if key[pygame.K_d] and key[pygame.K_w]== True:
            player.move_ip(-movement_speed, movement_speed)
    
    # Second Layer Top Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)):
        if key[pygame.K_s] == True:
            player.move_ip(0, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)):
        if key[pygame.K_d] and key[pygame.K_s] == True:
            player.move_ip((0.6 * movement_speed), -(movement_speed))
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)):
        if key[pygame.K_a] and key[pygame.K_s] and player.bottom:
            player.move_ip((0.6 * movement_speed), -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)):
        if key[pygame.K_w] == True:
            player.move_ip(0, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)):
        if key[pygame.K_w] and key[pygame.K_d] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (150, 300), (1620, 300), 3)):
        if key[pygame.K_w] and key[pygame.K_a] == True:
            player.move_ip(movement_speed, movement_speed)
    
    # Second Layer Right Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)):
        if key[pygame.K_a] == True:
            player.move_ip(movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)):
        if key[pygame.K_a] and key[pygame.K_s]== True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)):
        if key[pygame.K_a] and key[pygame.K_w]== True:
            player.move_ip(movement_speed, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)):
        if key[pygame.K_d] == True:
            player.move_ip(-movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)):
        if key[pygame.K_d] and key[pygame.K_s]== True:
            player.move_ip(-movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 300), (1620, 780), 3)):
        if key[pygame.K_d] and key[pygame.K_w]== True:
            player.move_ip(-movement_speed, movement_speed)
    
    # Second Layer Bottom
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)):
        if key[pygame.K_s] == True:
            player.move_ip(0, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)):
        if key[pygame.K_d] and key[pygame.K_s] == True:
            player.move_ip((0.6 * movement_speed), -(movement_speed))
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)):
        if key[pygame.K_a] and key[pygame.K_s] and player.bottom:
            player.move_ip((0.6 * movement_speed), -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)):
        if key[pygame.K_w] == True:
            player.move_ip(0, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)):
        if key[pygame.K_w] and key[pygame.K_d] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1620, 780), (300, 780), 3)):
        if key[pygame.K_w] and key[pygame.K_a] == True:
            player.move_ip(movement_speed, movement_speed)
    
    # Outside Left Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)):
        if key[pygame.K_a] == True:
            player.move_ip(movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)):
        if key[pygame.K_a] and key[pygame.K_s] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)):
        if key[pygame.K_a] and key[pygame.K_w] == True:
            player.move_ip(movement_speed, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)):
        if key[pygame.K_d] == True:
            player.move_ip(-movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)):
        if key[pygame.K_d] and key[pygame.K_s]== True:
            player.move_ip(-movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 780), (300, 450), 3)):
        if key[pygame.K_d] and key[pygame.K_w]== True:
            player.move_ip(-movement_speed, movement_speed)
    
    # Third Level Top Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 450), (1470, 450) , 3)):
        if key[pygame.K_s] == True:
            player.move_ip(0, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 450), (1470, 450) , 3)):
        if key[pygame.K_d] and key[pygame.K_s] == True:
            player.move_ip((0.6 * movement_speed), -(movement_speed))
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 450), (1470, 450) , 3)):
        if key[pygame.K_a] and key[pygame.K_s] and player.bottom:
            player.move_ip((0.6 * movement_speed), -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 450), (1470, 450) , 3)):
        if key[pygame.K_w] == True:
            player.move_ip(0, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 450), (1470, 450) , 3)):
        if key[pygame.K_w] and key[pygame.K_d] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (300, 450), (1470, 450) , 3)):
        if key[pygame.K_w] and key[pygame.K_a] == True:
            player.move_ip(movement_speed, movement_speed)
    
    # Third Layer Right Collisions
    if player.colliderect(pygame.draw.line(screen, 'black', (1470, 450), (1470,630), 3)):
        if key[pygame.K_a] == True:
            player.move_ip(movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470, 450), (1470,630), 3)):
        if key[pygame.K_a] and key[pygame.K_s]== True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470, 450), (1470,630), 3)):
        if key[pygame.K_a] and key[pygame.K_w]== True:
            player.move_ip(movement_speed, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470, 450), (1470,630), 3)):
        if key[pygame.K_d] == True:
            player.move_ip(-movement_speed, 0)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470, 450), (1470,630), 3)):
        if key[pygame.K_d] and key[pygame.K_s]== True:
            player.move_ip(-movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470, 450), (1470,630), 3)):
        if key[pygame.K_d] and key[pygame.K_w]== True:
            player.move_ip(-movement_speed, movement_speed)
    
    # Final Layer Bottom
    if player.colliderect(pygame.draw.line(screen, 'black', (1470,630), (450, 630), 3)):
        if key[pygame.K_s] == True:
            player.move_ip(0, -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470,630), (450, 630), 3)):
        if key[pygame.K_d] and key[pygame.K_s] == True:
            player.move_ip((0.6 * movement_speed), -(movement_speed))
    if player.colliderect(pygame.draw.line(screen, 'black', (1470,630), (450, 630), 3)):
        if key[pygame.K_a] and key[pygame.K_s] and player.bottom:
            player.move_ip((0.6 * movement_speed), -movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470,630), (450, 630), 3)):
        if key[pygame.K_w] == True:
            player.move_ip(0, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470,630), (450, 630), 3)):
        if key[pygame.K_w] and key[pygame.K_d] == True:
            player.move_ip(movement_speed, movement_speed)
    if player.colliderect(pygame.draw.line(screen, 'black', (1470,630), (450, 630), 3)):
        if key[pygame.K_w] and key[pygame.K_a] == True:
            player.move_ip(movement_speed, movement_speed)
    

    # Reach end of level
    if player.colliderect(goal) is True:
        pygame.Rect.update(player, 65, 65, 15, 15)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Force Close Game
    if key[pygame.K_ESCAPE] == True:
        run = False
    pygame.display.update()

pygame.quit()