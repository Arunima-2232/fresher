import pygame
from sys import exit

pygame.init()

screen=pygame.display.set_mode((600,300))
pygame.display.set_caption('Gravity Falls Inspired')
clock=pygame.time.Clock()
test_font=pygame.font.Font(None,50)

sky_surface=pygame.image.load('graphics/skypt2.jpg').convert_alpha()
ground_surface=pygame.image.load('graphics/groundpt2.jpg').convert_alpha()
enemy_surface=pygame.image.load('graphics/enemyy-0.png').convert_alpha()
player_surface=pygame.image.load('graphics/player-0.png').convert_alpha()

sky_surface=pygame.transform.scale(sky_surface,(600,250))
ground_surface=pygame.transform.scale(ground_surface,(600,60))
enemy_surface=pygame.transform.scale(enemy_surface,(300,230))
player_surface=pygame.transform.scale(player_surface,(400,300))
score_surface=test_font.render('SCORE',False,'Black')
score_rect=score_surface.get_rect(topleft=(230,30))

enemy_x_pos=400
player_rect=player_surface.get_rect(topleft=(2,50))
enemy_rect=enemy_surface.get_rect(topleft=(enemy_x_pos,70))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
            
        mouse_pos=pygame.mouse.get_pos()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,250))
    enemy_rect.right-=4
    if enemy_rect.right<-120:
        enemy_rect.right=750
    screen.blit(enemy_surface,enemy_rect)

    screen.blit(player_surface,player_rect)
    pygame.draw.rect(screen,'Pink',score_rect)

    screen.blit(score_surface,score_rect)       
    pygame.display.update()

    clock.tick(60)
