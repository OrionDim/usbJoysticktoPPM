# https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Header-with-Photo-702x336.png

import sys
import pygame
from pygame.locals import *

bar_height = 150
bar_width = 30
border_color = [255, 0, 0]

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Joystick to PPM")
screen = pygame.display.set_mode([200, 600], 0, 32)
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    print(joystick.get_name())

throttle_now = 0
throttle_max = 2000
throttle_ltx = 10
throttle_lty = 30
throttle_color = [0, 0, 255]

pitch_now = 0
pitch_max = 2000
pitch_ltx = 50
pitch_lty = 30
pitch_color = [0, 0, 255]

roll_now = 0
roll_max = 2000
roll_ltx = 100
roll_lty = 30
roll_color = [0, 0, 255]

yaw_now = 0
yaw_max = 2000
yaw_ltx = 150
yaw_lty = 30
yaw_color = [0, 0, 255]

throttle_value = 0
yaw_value = 0
pitch_value = 0
roll_value = 0

# TODO make config file JSON

while True:

    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button != 24:
                print(event)
        if event.type == pygame.JOYBUTTONUP:
            if event.button != 24:
                print(event)
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                roll_value = int(event.value * 1000)
                # print('ROLL:', event.value*2000)
            if event.axis == 1:
                # print('PITCH:', event.value*2000)
                pitch_value = int(event.value * 1000)
            if event.axis == 2:
                if event.value + 1 == 0 or event.value + 1 < 0:
                    event.value = 0
                else:
                    event.value = (event.value + 1) / 2 * 2000
                # print('THROTTLE:', event.value)
                throttle_value = int(event.value)
        if event.type == pygame.JOYHATMOTION:
            print(event)
        if event.type == pygame.JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == pygame.JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    current_pitch_pix = bar_height * pitch_value / throttle_max
    current_roll_pix = bar_height * roll_value / throttle_max
    current_yaw_pix = bar_height * yaw_value / throttle_max
    current_throttle_pix = bar_height * throttle_value / throttle_max
    font = pygame.font.SysFont("Arial", 13)
    text = font.render("THR", True, throttle_color)
    screen.blit(text, (throttle_ltx, throttle_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (throttle_ltx, throttle_lty), (throttle_ltx + bar_width, throttle_lty), 2)
    pygame.draw.line(screen, border_color, (throttle_ltx + bar_width, throttle_lty),
                     (throttle_ltx + bar_width, throttle_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (throttle_ltx + bar_width, throttle_lty + bar_height),
                     (throttle_ltx, throttle_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (throttle_ltx, throttle_lty + bar_height), (throttle_ltx, throttle_lty), 2)
    pygame.draw.polygon(screen, throttle_color, [(int(throttle_ltx + 2), int(throttle_lty + bar_height - 2)),
                                                 (
                                                 int(throttle_ltx + bar_width - 1), int(throttle_lty + bar_height - 2)),
                                                 (int(throttle_ltx + bar_width - 1),
                                                  int(throttle_lty + bar_height - current_throttle_pix)), (
                                                     int(throttle_ltx + 2),
                                                     int(throttle_lty + bar_height - current_throttle_pix))])

    font = pygame.font.SysFont("Arial", 13)
    text = font.render("PTH", True, pitch_color)
    screen.blit(text, (pitch_ltx, pitch_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (pitch_ltx, pitch_lty), (pitch_ltx + bar_width, pitch_lty), 2)
    pygame.draw.line(screen, border_color, (pitch_ltx + bar_width, pitch_lty),
                     (pitch_ltx + bar_width, pitch_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (pitch_ltx + bar_width, pitch_lty + bar_height),
                     (pitch_ltx, pitch_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (pitch_ltx, pitch_lty + bar_height), (pitch_ltx, pitch_lty), 2)
    pygame.draw.polygon(screen, pitch_color, [(int(pitch_ltx + 2), int(pitch_lty + bar_height / 2 - 2)),
                                              (int(pitch_ltx + bar_width - 1), int(pitch_lty + bar_height / 2 - 2)), (
                                                  int(pitch_ltx + bar_width - 1),
                                                  int(pitch_lty + bar_height / 2 - current_pitch_pix)),
                                              (
                                              int(pitch_ltx + 2), int(pitch_lty + bar_height / 2 - current_pitch_pix))])

    font = pygame.font.SysFont("Arial", 13)
    text = font.render("YAW", True, yaw_color)
    screen.blit(text, (yaw_ltx, yaw_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (yaw_ltx, yaw_lty), (yaw_ltx + bar_width, yaw_lty), 2)
    pygame.draw.line(screen, border_color, (yaw_ltx + bar_width, yaw_lty),
                     (yaw_ltx + bar_width, yaw_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (yaw_ltx + bar_width, yaw_lty + bar_height),
                     (yaw_ltx, yaw_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (yaw_ltx, yaw_lty + bar_height), (yaw_ltx, yaw_lty), 2)
    pygame.draw.polygon(screen, yaw_color, [(int(yaw_ltx + 2), int(yaw_lty + bar_height / 2 - 2)),
                                            (int(yaw_ltx + bar_width - 1), int(yaw_lty + bar_height / 2 - 2)), (
                                                int(yaw_ltx + bar_width - 1),
                                                int(yaw_lty + bar_height / 2 - current_yaw_pix)),
                                            (int(yaw_ltx + 2), int(yaw_lty + bar_height / 2 - current_yaw_pix))])

    font = pygame.font.SysFont("Arial", 13)
    text = font.render("ROL", True, roll_color)
    screen.blit(text, (roll_ltx, roll_lty - text.get_height()))
    pygame.draw.line(screen, border_color, (roll_ltx, roll_lty), (roll_ltx + bar_width, roll_lty), 2)
    pygame.draw.line(screen, border_color, (roll_ltx + bar_width, roll_lty),
                     (roll_ltx + bar_width, roll_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (roll_ltx + bar_width, roll_lty + bar_height),
                     (roll_ltx, roll_lty + bar_height), 2)
    pygame.draw.line(screen, border_color, (roll_ltx, roll_lty + bar_height), (roll_ltx, roll_lty), 2)

    pygame.draw.polygon(screen, roll_color, [(int(roll_ltx + 2), int(roll_lty + bar_height / 2 - 2)),
                                             (int(roll_ltx + bar_width - 1), int(roll_lty + bar_height / 2 - 2)), (
                                                 int(roll_ltx + bar_width - 1),
                                                 int(roll_lty + bar_height / 2 - current_roll_pix)),
                                             (int(roll_ltx + 2), int(roll_lty + bar_height / 2 - current_roll_pix))])
    # TODO Make PPM output 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
