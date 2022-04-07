# -----------------------------------------------------------------------------
# Name: Michal Buczek       Assignment Template (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Your Name Here
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
# ---------------------------------------------------------------------------------------#
# I think this project deserves a level XXXXXX because ...
#
# Features Added:
#   Movement with boolean functions to make transitions from keys smoother. When two keys are pressed by accident at
#   the same time, movement does not stop and goes in the most recently clicked key direction.
#   ...
#   ...
# ---------------------------------------------------------------------------------------#
from random import randint

import pygame
import math

def distFromPoints(point1, point2):

    distance = math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2))

    return distance

def main():
    # -----------------------------Setup-------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use
    surfaceSize = 900  # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  # Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize - 100))

    # -----------------------------Program Variable Initialization-----------------------#
    rocketBaseColor = (171, 186, 185)  # rocket color
    rocketWingColor = (156, 5, 5)
    rocketPos = [435, 250]  # rocket position
    rocketSpeed = [0, 0]
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    asteroidColor = (153, 153, 153)
    asteroidPos = [900, 0]
    asteroidSize = [50]
    astMovementX = 0
    astMovementY = 0

    rocketAsteroidCollision = False

    # -----------------------------Main Game Loop----------------------------------------#
    while True:

        # -----------------------------Event Handling------------------------------------#
        ev = pygame.event.poll()  # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # ... leave game loop
        #  Enabling movement with arrow keys when pressed down
        elif ev.type == pygame.KEYDOWN:  # KEYDOWN has the attributes: key, mod, unicode, scancode
            print('A Key was pressed down.  ', end='')
            print(f'key: {ev.key}, mod: {ev.mod}, unicode: {ev.unicode}, scancode: {ev.scancode}')
            #  movement in desired direction
            if ev.key == pygame.K_LEFT:
                print('Move Left')
                moveLeft = True
                if moveLeft:
                    rocketSpeed[0] = -10

            elif ev.key == pygame.K_RIGHT:
                print('Move Right')
                moveRight = True
                if moveRight:
                    rocketSpeed[0] = 10

            elif ev.key == pygame.K_UP:
                print('Move Up')
                moveUp = True
                if moveUp:
                    rocketSpeed[1] = -10

            elif ev.key == pygame.K_DOWN:
                print('Move Down')
                moveDown = True
                if moveDown:
                    rocketSpeed[1] = 10

        #  Stops movement when arrow key is released
        #  Boolean usage to make transitions from keys more smooth and not stopping rocket when two clicked at the same
        #  time.
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_LEFT:
                moveLeft = False
                if not moveLeft and not moveRight:
                    rocketSpeed[0] = 0

            elif ev.key == pygame.K_RIGHT:
                moveRight = False
                if not moveRight and not moveLeft:
                    rocketSpeed[0] = 0

            elif ev.key == pygame.K_UP:
                moveUp = False
                if not moveUp and not moveDown:
                    rocketSpeed[1] = 0

            elif ev.key == pygame.K_DOWN:
                moveDown = False
                if not moveDown and not moveUp:
                    rocketSpeed[1] = 0

        # -----------------------------Game Logic----------------------------------------#
        # Rocket movement based on the rocket speed
        rocketPos[0] += rocketSpeed[0]
        rocketPos[1] += rocketSpeed[1]

        #  Horizontal boundary's for rocket ship
        if rocketPos[0] <= 5:
            rocketSpeed[0] = 0
            rocketPos[0] += abs(rocketPos[0] - 5)  # Makes it impossible to cross 5 because the difference is added back

        if rocketPos[0] >= 865:
            rocketSpeed[0] = 0
            rocketPos[0] -= rocketPos[0] - 865  # Makes it impossible to cross 865 because difference is subtracted back

        #  Vertical boundary's for rocket ship
        if rocketPos[1] <= 0:
            rocketSpeed[1] = 0
            rocketPos[1] -= rocketPos[1]  # If rocketPos < 0 then; (-) * (-) = +, impossible to pass 0

        if rocketPos[1] >= 695:
            rocketSpeed[1] = 0
            rocketPos[1] -= rocketPos[1] - 695  # Difference is subtracted back making it impossible to cross 695

        #  Getting asteroid to bounce off walls/boundaries
        if asteroidPos[0] <= 25:
            astMovementX = randint(0, 5)
            astMovementY = randint(-5, 5)
        elif asteroidPos[0] >= 875:
            astMovementX = randint(-5, 0)
            astMovementY = randint(-5, 5)
        elif asteroidPos[1] <= 25:
            astMovementX = randint(-5, 5)
            astMovementY = randint(0, 5)
        elif asteroidPos[1] >= 775:
            astMovementX = randint(-5, 5)
            astMovementY = randint(-5, 0)

        asteroidPos[0] += astMovementX
        asteroidPos[1] += astMovementY

        #  Rocket key points for collision detection
        rocketTopRight = (rocketPos[0] + 30, rocketPos[1])
        rocketBtmLeft = (rocketPos[0] - 8, rocketPos[1] + 105)
        rocketBtmRight = (rocketPos[0] + 38, rocketPos[1] + 105)
        leftWing = (rocketPos[0] - 12, rocketPos[1] + 60)
        rightWing = (rocketPos[0] + 42, rocketPos[1] + 60)

        #  asteroid to rocket collision detection
        if distFromPoints(asteroidPos, rocketPos) < asteroidSize[0] or \
                distFromPoints(asteroidPos, rocketTopRight) < asteroidSize[0] or \
                distFromPoints(asteroidPos, rocketBtmLeft) < asteroidSize[0] or \
                distFromPoints(asteroidPos, rocketBtmRight) < asteroidSize[0] or \
                distFromPoints(asteroidPos, leftWing) < asteroidSize[0] or \
                distFromPoints(asteroidPos, rightWing) < asteroidSize[0]:
            rocketAsteroidCollision = not rocketAsteroidCollision

        if rocketAsteroidCollision:
            rocketBaseColor = (255, 0, 0)
            astMovementX = randint(-5, 5)
            astMovementY = randint(-5, 5)
            rocketSpeed[0] -= astMovementX
            rocketSpeed[1] -= astMovementY
            rocketAsteroidCollision = False

        # -----------------------------Drawing Everything--------------------------------#

        mainSurface.fill((39, 1, 59))

        #  Rocket design (All parts are connected throughout movement)
        pygame.draw.ellipse(mainSurface, rocketBaseColor, (rocketPos[0], rocketPos[1], 30, 90))  # rockets main body
        pygame.draw.polygon(mainSurface, (104, 115, 114), [(rocketPos[0] + 3, rocketPos[1] + 70), (rocketPos[0] + 27,
                                                                                                   rocketPos[1] + 70),
                                                           (rocketPos[0] - 8, rocketPos[1] + 105), (rocketPos[0] + 38,
                                                                                                    rocketPos[1] + 105)
                                                           ])  # Bottom of Rocket
        pygame.draw.polygon(mainSurface, rocketWingColor, [(rocketPos[0] + 2, rocketPos[1] + 20), (rocketPos[0] + 2,
                                                                                                   rocketPos[1] + 69),
                                                           (rocketPos[0] - 12, rocketPos[1] + 60)])  # Left wing
        pygame.draw.polygon(mainSurface, rocketWingColor, [(rocketPos[0] + 28, rocketPos[1] + 20), (rocketPos[0] + 28,
                                                                                                    rocketPos[1] + 69),
                                                           (rocketPos[0] + 42, rocketPos[1] + 60)])  # Right wing
        #  Space rocks (meteors, asteroids, comet's)
        pygame.draw.circle(mainSurface, asteroidColor, (asteroidPos[0], asteroidPos[1]), asteroidSize[0])

        # Surface display
        pygame.display.flip()

        clock.tick(60)  # Forces frame rate to be slower

    pygame.quit()  # Once loop is left, closes the window.


main()
