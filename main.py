import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((1920, 1080))


player = pygame.Rect(65, 70, 15, 15)
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
# lanes
bottomlane = pygame.Rect(0, 930, 1980, 150)
leftlane = pygame.Rect(0, 0, 150, 1980)
rightlane = pygame.Rect(1770, 0, 150, 1080)
toplane = pygame.Rect(0, 0, 1920, 150)
second_level_toplane = pygame.Rect(0, 150, 1770, 150)
second_level_rightlane = pygame.Rect(1620,150, 150, 780)
second_level_bottomlane = pygame.Rect(150, 780, 1620, 150)
second_level_leftlane = pygame.Rect(150, 300, 150, 500)
third_level_toplane = pygame.Rect(150, 300, 1470, 150)
movement_speed = float(2)
run = True

while run:
    # background color
    screen.fill('black')
    
    pygame.draw.rect(screen, ('white'), toplane)
    pygame.draw.rect(screen, ('white'), rightlane)
    pygame.draw.rect(screen, ('white'), bottomlane)
    pygame.draw.rect(screen, ('white'), leftlane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_toplane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_rightlane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_bottomlane)
    pygame.draw.rect(screen, ('whitesmoke'), second_level_leftlane)
    pygame.draw.rect(screen, ('gray86'), third_level_toplane)
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
    pygame.draw.rect(screen, ('red'), player)


    # Diagonal Movement Keybinds
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and key[pygame.K_s]:
        player.move_ip(-(0.5 * movement_speed), 0.5 * movement_speed)
    elif key[pygame.K_w] and key[pygame.K_a]:
        player.move_ip(-(0.5 * movement_speed), -(0.5 * movement_speed))
    elif key[pygame.K_w] and key[pygame.K_d]:
        player.move_ip(0.5 * movement_speed, -(0.5 * movement_speed))
    elif key[pygame.K_d] and key[pygame.K_s]:
        player.move_ip(0.5 * movement_speed, (0.5 * movement_speed))
    elif key[pygame.K_a] and key[pygame.K_d]:
        player.move_ip(0, 0)
    elif key[pygame.K_w] and key[pygame.K_s]:
        player.move_ip(0, 0)
    
    # Movement Keybinds
    if key[pygame.K_a] == True:
        player.move_ip(-(movement_speed), 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, movement_speed)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -(movement_speed))
    elif key[pygame.K_d] == True:
        player.move_ip(movement_speed, 0)
   

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()