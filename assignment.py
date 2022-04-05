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
#   ...
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
    # Set up some data to describe a small circle and its color
    rocketBaseColor = (171, 186, 185)  # A color is a mix of (Red, Green, Blue)
    rocketWingColor = (156, 5, 5)
    rocketX = 435
    rocketY = 250

    # -----------------------------Main Game Loop----------------------------------------#
    while True:

        # -----------------------------Event Handling------------------------------------#
        ev = pygame.event.poll()  # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # ... leave game loop
        elif ev.type == pygame.KEYDOWN:  # KEYDOWN has the attributes: key, mod, unicode, scancode
            print('A Key was pressed down.  ', end='')
            print(f'key: {ev.key}, mod: {ev.mod}, unicode: {ev.unicode}, scancode: {ev.scancode}')

            if ev.key == pygame.K_LEFT:
                print('Move Left')
                rocketX -= 10
            elif ev.key == pygame.K_RIGHT:
                print('Move Right')
                rocketX += 10

        # -----------------------------Game Logic----------------------------------------#
        # Update your game objects and data structures here...

        # -----------------------------Drawing Everything--------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((39, 1, 59))

        # Draw a circle on the surface
        pygame.draw.ellipse(mainSurface, rocketBaseColor, (rocketX, rocketY, 30, 90))
        pygame.draw.polygon(mainSurface, (104, 115, 114), [(rocketX + 3, rocketY + 70), (rocketX + 27, rocketY + 70),
                                                           (rocketX - 8, rocketY + 105), (rocketX + 38, rocketY + 105)
                                                           ])
        pygame.draw.polygon(mainSurface, rocketWingColor, [(rocketX + 2, rocketY + 20), (rocketX + 2, rocketY + 69),
                                                           (rocketX - 12, rocketY + 60)])
        pygame.draw.polygon(mainSurface, rocketWingColor, [(rocketX + 28, rocketY + 20), (rocketX + 28, rocketY + 69),
                                                           (rocketX + 42, rocketY + 60)])

    # -----------------------------Main Game Loop----------------------------------------#
    while True:

        # -----------------------------Event Handling---------------

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

        clock.tick(60)  # Force frame rate to be slower

    pygame.quit()  # Once we leave the loop, close the window.


main()
