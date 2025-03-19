import pygame 
import time
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Mouse clock")

leftarm = pygame.image.load("labs/lab7/images/leftarm.png")
rightarm = pygame.image.load("labs/lab7/images/rightarm.png")
mainclock = pygame.transform.scale(pygame.image.load("labs/lab7/images/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    
    screen.blit(mainclock, (0,0))
    
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()









# import pygame 
# import time

# pygame.init()
# clock = pygame.time.Clock()

# width, height = 1400, 1050
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Mickey Mouse Clock')

# background = pygame.image.load('labs/lab7/images/clock.png') 
# left_arm = pygame.image.load('labs/lab7/images/leftarm.png')
# right_arm = pygame.image.load('labs/lab7/images/rightarm.png')

# done = False

# while not done:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
    
#     current_time = time.localtime()
#     minute = current_time.tm_min 
#     second = current_time.tm_sec 

#     minute_angle = -(minute * 6 + (second / 60) * 6)
#     second_angle = -(second * 6)

#     screen.blit(background, (0, 0))

#     rotated_rightarm = pygame.transform.rotate(right_arm, minute_angle)
#     rightarm_rect = rotated_rightarm.get_rect(center=(width // 2, height // 2))
#     screen.blit(rotated_rightarm, rightarm_rect)

#     rotated_leftarm = pygame.transform.rotate(left_arm, second_angle)
#     leftarm_rect = rotated_leftarm.get_rect(center=(width // 2, height // 2))
#     screen.blit(rotated_leftarm, leftarm_rect)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()











# import pygame 
# import time

# pygame.init()
# clock = pygame.time.Clock()
# width,height = 800,600
# screen = pygame.display.set_mode((width,height))
# pygame.display.set_caption('Mickey Mouse Clock')

# background = pygame.image.load('labs/lab7/images/clock.png'),(width,height)
# left_arm = pygame.image.load('labs/lab7/images/leftarm.png')
# right_arm = pygame.image.load('labs/lab7/images/rightarm.png')

# done = False

# while not done:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
    
#     current_time = time.localtime()
#     minute = current_time.tm_min 
#     second = current_time.tm_sec 

#     screen.blit(background, (0,0))

#      # Бұрылыстарды есептеу
#     minute_angle = -(minute * 6 + (second / 60) * 6)
#     second_angle = -(second * 6)

#     # Фонды салу
#     screen.blit(background, (0, 0))

#     # Оң қол (минут стрелкасы)
#     rotated_rightarm = pygame.transform.rotate(right_arm, minute_angle)
#     rightarm_rect = rotated_rightarm.get_rect(center=(width // 2, height // 2))
#     screen.blit(rotated_rightarm, rightarm_rect)

#     # Сол қол (секунд стрелкасы)
#     rotated_leftarm = pygame.transform.rotate(left_arm, second_angle)
#     leftarm_rect = rotated_leftarm.get_rect(center=(width // 2, height // 2))
#     screen.blit(rotated_leftarm, leftarm_rect)

#     # Экранды жаңарту
#     pygame.display.flip()
#     clock.tick(60)  # 60 FPS
# pygame.quit()
