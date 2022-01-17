import sys
import pygame
from pygame.locals import *

bar_heigh=150
bar_width=30
border_color =  [255, 0, 0]

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()


pygame.init();
pygame.display.set_caption("Joystick to PPM")

screen = pygame.display.set_mode([200, 600], 0, 32)


# Draw some black (Transparent) polygons to create mountain peaks
# The screen is 600 wide so I've drawn 10 polygons at 60 pixels wide each
trottle_now=0
trottle_max=2000
trottle_ltx=10
trottle_lty=30
trottle_color =  [0, 0, 255]

pitch_now=0
pitch_max=2000
pitch_ltx=50
pitch_lty=30
pitch_color =  [0, 0, 255]

roll_now=0
roll_max=2000
roll_ltx=100
roll_lty=30
roll_color =  [0, 0, 255]

yaw_now=0
yaw_max=2000
yaw_ltx=150
yaw_lty=30
yaw_color =  [0, 0, 255]

Velocity=50

while True:
    screen.fill((100, 100, 100))

    trottle_now = trottle_now + Velocity
    if trottle_now >= 2000: Velocity *= -1
    if trottle_now <= 0: Velocity *= -1
    current_trottle_pix = bar_heigh * trottle_now / trottle_max




    font = pygame.font.SysFont("Arial", 13)
    text = font.render("THR", True, trottle_color)
    screen.blit(text, (trottle_ltx, trottle_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (trottle_ltx, trottle_lty), (trottle_ltx + bar_width, trottle_lty), 2)
    pygame.draw.line(screen, border_color, (trottle_ltx + bar_width, trottle_lty),(trottle_ltx + bar_width, trottle_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (trottle_ltx + bar_width, trottle_lty + bar_heigh),(trottle_ltx, trottle_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (trottle_ltx, trottle_lty + bar_heigh), (trottle_ltx, trottle_lty), 2)
    pygame.draw.polygon(screen, trottle_color, [(int(trottle_ltx+2),int(trottle_lty+bar_heigh-2)), (int(trottle_ltx+bar_width-1),int(trottle_lty+bar_heigh-2)), (int(trottle_ltx+bar_width-1),int(trottle_lty+bar_heigh-current_trottle_pix)), (int(trottle_ltx+2),int(trottle_lty+bar_heigh-current_trottle_pix))])

    font = pygame.font.SysFont("Arial", 13)
    text = font.render("PTH", True, pitch_color)
    screen.blit(text, (pitch_ltx, pitch_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (pitch_ltx, pitch_lty), (pitch_ltx + bar_width, pitch_lty), 2)
    pygame.draw.line(screen, border_color, (pitch_ltx + bar_width, pitch_lty),
                     (pitch_ltx + bar_width, pitch_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (pitch_ltx + bar_width, pitch_lty + bar_heigh),
                     (pitch_ltx, pitch_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (pitch_ltx, pitch_lty + bar_heigh), (pitch_ltx, pitch_lty), 2)
    pygame.draw.polygon(screen, pitch_color, [(int(pitch_ltx + 2), int(pitch_lty + bar_heigh - 2)),
                                                (int(pitch_ltx + bar_width - 1), int(pitch_lty + bar_heigh - 2)), (
                                                int(pitch_ltx + bar_width - 1),
                                                int(pitch_lty + bar_heigh - current_trottle_pix)),
                                                (int(pitch_ltx + 2), int(pitch_lty + bar_heigh - current_trottle_pix))])

    font = pygame.font.SysFont("Arial", 13)
    text = font.render("YAW", True, yaw_color)
    screen.blit(text, (yaw_ltx, yaw_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (yaw_ltx, yaw_lty), (yaw_ltx + bar_width, yaw_lty), 2)
    pygame.draw.line(screen, border_color, (yaw_ltx + bar_width, yaw_lty),
                     (yaw_ltx + bar_width, yaw_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (yaw_ltx + bar_width, yaw_lty + bar_heigh),
                     (yaw_ltx, yaw_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (yaw_ltx, yaw_lty + bar_heigh), (yaw_ltx, yaw_lty), 2)
    pygame.draw.polygon(screen, yaw_color, [(int(yaw_ltx + 2), int(yaw_lty + bar_heigh - 2)),
                                              (int(yaw_ltx + bar_width - 1), int(yaw_lty + bar_heigh - 2)), (
                                                  int(yaw_ltx + bar_width - 1),
                                                  int(yaw_lty + bar_heigh - current_trottle_pix)),
                                              (int(yaw_ltx + 2), int(yaw_lty + bar_heigh - current_trottle_pix))])

    font = pygame.font.SysFont("Arial", 13)
    text = font.render("ROL", True, roll_color)
    screen.blit(text, (roll_ltx, roll_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (roll_ltx, roll_lty), (roll_ltx + bar_width, roll_lty), 2)
    pygame.draw.line(screen, border_color, (roll_ltx + bar_width, roll_lty),
                     (roll_ltx + bar_width, roll_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (roll_ltx + bar_width, roll_lty + bar_heigh),
                     (roll_ltx, roll_lty + bar_heigh), 2)
    pygame.draw.line(screen, border_color, (roll_ltx, roll_lty + bar_heigh), (roll_ltx, roll_lty), 2)
    pygame.draw.polygon(screen, roll_color, [(int(roll_ltx + 2), int(roll_lty + bar_heigh - 2)),
                                            (int(roll_ltx + bar_width - 1), int(roll_lty + bar_heigh - 2)), (
                                                int(roll_ltx + bar_width - 1),
                                                int(roll_lty + bar_heigh - current_trottle_pix)),
                                            (int(roll_ltx + 2), int(roll_lty + bar_heigh - current_trottle_pix))])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)



