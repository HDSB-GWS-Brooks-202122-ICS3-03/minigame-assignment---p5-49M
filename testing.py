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
    pygame.font.init()  # font display
    surfaceSize = 900  # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  # Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize - 100))

    # -----------------------------Program Variable Initialization-----------------------#
    rocketBaseColor = (171, 186, 185)  # rocket color
    rocketWingColor = (156, 5, 5)
    rocketPos = [435, 250]  # rocket position
    rocketSpeed = [0, 0]
    #  movement
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    #  asteroids
    asteroidColor = (153, 153, 153)
    asteroidPos = []
    asteroidSize = [30]
    astMovementX = []
    astMovementY = []
    rocketAsteroidCollision = []
    numAsteroids = 3
    for count in range(numAsteroids):
        asteroidPos.append([900, randint(0, 800)])
        astMovementX.append(0)
        astMovementY.append(0)

    #  life count
    lives = 3
    livesFont = pygame.font.SysFont('Comic Sans MS', 40)

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
        for count in range(numAsteroids):
            if asteroidPos[count][0] <= 25:
                astMovementX[count] = randint(0, 5)
                astMovementY[count] = randint(-5, 5)
            elif asteroidPos[count][0] >= 875:
                astMovementX[count] = randint(-5, 0)
                astMovementY[count] = randint(-5, 5)
            elif asteroidPos[count][1] <= 25:
                astMovementX[count] = randint(-5, 5)
                astMovementY[count] = randint(0, 5)
            elif asteroidPos[count][1] >= 775:
                astMovementX[count] = randint(-5, 5)
                astMovementY[count] = randint(-5, 0)

            if astMovementX[count] == 0 and astMovementY[count] == 0:
                if asteroidPos[count][0] <= 25:
                    astMovementX[count] = randint(1, 5)
                else:
                    astMovementX[count] = randint(-5, -1)

            asteroidPos[count][0] += astMovementX[count]
            asteroidPos[count][1] += astMovementY[count]

        #  Rocket key points for collision detection
        rocketTopRight = (rocketPos[0] + 30, rocketPos[1])
        rocketBtmLeft = (rocketPos[0] - 8, rocketPos[1] + 105)
        rocketBtmRight = (rocketPos[0] + 38, rocketPos[1] + 105)
        leftWing = (rocketPos[0] - 12, rocketPos[1] + 60)
        rightWing = (rocketPos[0] + 42, rocketPos[1] + 60)

        #  asteroid to rocket collision detection with key points
        for count in range(numAsteroids):
            if distFromPoints(asteroidPos[count], rocketPos) < asteroidSize[0] or \
                    distFromPoints(asteroidPos[count], rocketTopRight) < asteroidSize[0] or \
                    distFromPoints(asteroidPos[count], rocketBtmLeft) < asteroidSize[0] or \
                    distFromPoints(asteroidPos[count], rocketBtmRight) < asteroidSize[0] or \
                    distFromPoints(asteroidPos[count], leftWing) < asteroidSize[0] or \
                    distFromPoints(asteroidPos[count], rightWing) < asteroidSize[0]:
                rocketAsteroidCollision.append(count)

        if len(rocketAsteroidCollision) > 0:
            for count in rocketAsteroidCollision:
                #  rocketBaseColor = (255, 0, 0)
                asteroidPos[count][0] = randint(0, 900)
                asteroidPos[count][1] = randint(0, 800)
                astMovementX[count] = randint(-5, 5)
                astMovementY[count] = randint(-5, 5)
                if astMovementX[count] == 0 and astMovementY[count] == 0:
                    astMovementX[count] = randint(-5, -1)
                lives -= 1

            rocketAsteroidCollision = []

        # -----------------------------Drawing Everything--------------------------------#

        mainSurface.fill((39, 1, 59))
        #  Lives counter
        lifeCount = str(lives)
        textSurface = livesFont.render(f"lives: {lifeCount}", False, (255, 0, 0))
        mainSurface.blit(textSurface, (0, 0))

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
        for count in range(numAsteroids):
            pygame.draw.circle(mainSurface, asteroidColor, asteroidPos[count], asteroidSize[0])

        # Surface display
        pygame.display.flip()

        clock.tick(60)  # Forces frame rate to be slower

    pygame.quit()  # Once loop is left, closes the window.


main()
