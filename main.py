import sys

import pygame

from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
#for joystick in joysticks:
    #print(joystick.get_name())

while True:

    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            if event.button != 24: print(event)
        if event.type == JOYBUTTONUP:
            if event.button != 24: print(event)
        if event.type == JOYAXISMOTION:
            if event.axis == 0:
                print('ROLL:', event.value)
            if event.axis == 1:
                print('PITCH:', event.value)
            if event.axis == 2:
                if event.value+1 == 0 or event.value+1 < 0:
                    event.value=0
                else:
                    event.value=(event.value+1)/2
                print('TROTTLE:', event.value)
        if event.type == JOYHATMOTION:
            print(event)
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    clock.tick(60)