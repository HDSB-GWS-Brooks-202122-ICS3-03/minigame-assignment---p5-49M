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

import pygame


def main():
    # -----------------------------Setup-------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use
    surfaceSize = 900  # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  # Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize - 100))

    # -----------------------------Program Variable Initialization-----------------------#
    rocketBaseColor = (171, 186, 185)  # A color is a mix of (Red, Green, Blue)
    rocketWingColor = (156, 5, 5)
    rocketPos = [435, 250]
    rocketSpeed = [0, 0]
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

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

        #  Horizontal boundary for rocket ship
        if rocketPos[0] <= 5 or rocketPos[0] >= 865:
            rocketSpeed[0] = 0

        #  Vertical boundary for rocket ship
        if rocketPos[1] <= 0 or rocketPos[1] >= 695:
            rocketSpeed[1] = 0

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

        # Surface display
        pygame.display.flip()

        clock.tick(60)  # Forces frame rate to be slower

    pygame.quit()  # Once loop is left, closes the window.


main()
