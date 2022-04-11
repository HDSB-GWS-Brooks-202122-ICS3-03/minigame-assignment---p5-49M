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
#   1. Movement with boolean functions to make transitions from keys smoother. When two keys are pressed by accident at
#   the same time, movement does not stop and goes in the most recently clicked key direction.
#   2. Multiple asteroids made using a list for convenience and saving space/code. The collision detection has been made
#   to check if an asteroid has been hit and if so, it finds which one hit and puts it through
#   rocketAsteroidCollision variable steps.
#   Menu screen background uploaded from files
#   3. Added score going up by seconds and being displayed. Score freezes after 3 lives have been lost and is then
#   displayed in the game over screen.
# ---------------------------------------------------------------------------------------#
from random import randint

import pygame
import math
import time


def distFromPoints(point1, point2):
    distance = math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2))

    return distance


def timeNow():
    return int(time.time())


def duration(start, end):
    return end - start


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
    gameState = 'start screen'

    #  start screen game state
    menuBackground = pygame.image.load('spacebg.jpg')
    menuBackground = pygame.transform.scale(menuBackground, (surfaceSize, surfaceSize - 100))
    startButtonPos = [325, 375, 250, 100]
    playText = pygame.font.SysFont('impact', 100)
    gameTitle = pygame.font.SysFont('impact', 100)
    howToPlayButton = [300, 500, 300, 50]
    howToPlayText = pygame.font.SysFont('impact', 60)

    #  how to play game state
    htpBackground = pygame.image.load('spacerules.jpg')
    htpBackground = pygame.transform.scale(htpBackground, (surfaceSize, surfaceSize - 100))
    instructions = pygame.font.SysFont('lucidaconsole', 20)
    #  return to menu button
    returnMenuButtonPos = [375, 600, 150, 60]
    returnText = pygame.font.SysFont('impact', 40)

    #  end screen game state
    endBackground = pygame.image.load('stars.jpg')
    endBackground = pygame.transform.scale(endBackground, (surfaceSize, surfaceSize - 100))
    gameOverText = pygame.font.SysFont('lucidaconsole', 100)
    replayButtonPos = [275, 350, 350, 100]
    replayText = pygame.font.SysFont('lucidaconsole', 55)
    star1Colour = (255, 255, 255)
    star2Colour = (255, 255, 255)
    star3Colour = (255, 255, 255)
    starPos = [400, 550]

    #  main game, game state
    mainBackground = pygame.image.load('mainspace.jpg')
    mainBackground = pygame.transform.scale(mainBackground, (surfaceSize, surfaceSize - 100))

    #  timer/score counting variables
    startTime = 0
    levelDuration = 10
    nextLevelTime = levelDuration

    #  rocket
    rocketBaseColor = (171, 186, 185)  # rocket color
    rocketWingColor = (156, 5, 5)
    rocketPos = [435, 250]  # rocket position
    rocketSpeed = [0, 0]
    #  movement
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    #  asteroids position is made through a list and each is unique with a random spawn and random movement
    asteroidColor = (153, 153, 153)
    asteroidSize = [35]
    asteroidPos = []
    astMovementX = []
    astMovementY = []
    rocketAsteroidCollision = []

    score = 0
    highestScore = 0
    newHighScore = False
    startNumAsteroids = 1
    numAsteroids = startNumAsteroids
    for count in range(numAsteroids):
        asteroidPos.append([900, randint(0, 800)])
        astMovementX.append(0)
        astMovementY.append(0)

    #  life count
    startLives = 3
    lives = startLives
    livesFont = pygame.font.SysFont('Comic Sans MS', 40)

    # -----------------------------Main Game Loop----------------------------------------#
    while True:
        # -----------------------------Event Handling------------------------------------#
        ev = pygame.event.poll()  # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # ... leave game loop

        # start screen (lobby) program state
        if gameState == "start screen":
            #  Checking for button clicks
            mousePos = pygame.mouse.get_pos()
            if ev.type == pygame.MOUSEBUTTONUP:
                if startButtonPos[0] <= mousePos[0] <= startButtonPos[0] + 250 and \
                        startButtonPos[1] <= mousePos[1] <= startButtonPos[1] + 100:
                    gameState = 'main game'
                    startTime = timeNow()
                elif howToPlayButton[0] <= mousePos[0] <= howToPlayButton[0] + 300 and \
                        howToPlayButton[1] <= mousePos[1] <= howToPlayButton[1] + 50:
                    gameState = 'how to play'

            #  Background image
            mainSurface.blit(menuBackground, (0, 0))
            #  Drawing buttons
            #  start button
            pygame.draw.rect(mainSurface, (135, 251, 255), startButtonPos, 5)
            playTextPos = playText.render("PLAY", False, (255, 255, 255))
            mainSurface.blit(playTextPos, (365, 395))
            #  Game title (name of game)
            titlePos = gameTitle.render("SPACE COMMOTION", False, (255, 255, 255))
            mainSurface.blit(titlePos, (100, 250))
            #  How to play button
            pygame.draw.rect(mainSurface, (255, 255, 255), howToPlayButton, 3)
            htpButtonPos = howToPlayText.render("HOW TO PLAY", False, (135, 251, 255))
            mainSurface.blit(htpButtonPos, (307, 507))

        #  How to play program state
        elif gameState == 'how to play':
            #  return button click detection
            mousePos = pygame.mouse.get_pos()
            if ev.type == pygame.MOUSEBUTTONUP:
                if returnMenuButtonPos[0] <= mousePos[0] <= returnMenuButtonPos[0] + 150 and \
                        returnMenuButtonPos[1] <= mousePos[1] <= returnMenuButtonPos[1] + 60:
                    gameState = 'start screen'

            #  wallpaper
            mainSurface.blit(htpBackground, (0, 0))
            #  instruction text
            instructionsPos1 = instructions.render('Using the arrow keys,', False, (255, 255, 255))
            mainSurface.blit(instructionsPos1, (300, 200))
            instructionsPos2 = instructions.render('move your rocket to avoid', False, (255, 255, 255))
            mainSurface.blit(instructionsPos2, (280, 240))
            instructionsPos3 = instructions.render('the asteroids! You have 3 lives,', False, (255, 255, 255))
            mainSurface.blit(instructionsPos3, (260, 280))
            instructionsPos4 = instructions.render('do not lose them.   Good Luck!', False, (255, 255, 255))
            mainSurface.blit(instructionsPos4, (240, 320))
            #  return button
            pygame.draw.rect(mainSurface, (255, 255, 255), returnMenuButtonPos, 3)
            returnTextPos = returnText.render('Return', False, (255, 255, 255))
            mainSurface.blit(returnTextPos, (405, 620))

        #  Main game program state
        elif gameState == "main game":

            #  Enabling movement with arrow keys when pressed down
            if ev.type == pygame.KEYDOWN:  # KEYDOWN has the attributes: key, mod, unicode, scancode
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
            #  Boolean usage to make transitions from keys more smooth and not stopping rocket when two clicked
            #  at the same time.
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
            #  Score increasing every second and new asteroid coming in every 10 seconds
            score = duration(startTime, timeNow())

            #  makes new asteroids come in from the right
            if score == nextLevelTime:
                nextLevelTime += levelDuration
                numAsteroids += 1
                asteroidPos.append([900, randint(0, 800)])
                astMovementX.append(0)
                astMovementY.append(0)

            #  Transition to game over screen/state
            if lives <= 0:
                gameState = "game over"
                rocketSpeed[0] = 0
                rocketSpeed[1] = 0
                for count in range(numAsteroids):
                    astMovementX[count] = 0
                    astMovementY[count] = 0

            # Rocket movement based on the rocket speed
            rocketPos[0] += rocketSpeed[0]
            rocketPos[1] += rocketSpeed[1]

            #  Horizontal boundary's for rocket ship
            if rocketPos[0] <= 5:
                rocketSpeed[0] = 0
                rocketPos[0] += abs(rocketPos[0] - 5)  # Makes it impossible to cross 5 because the difference is
                # added back

            if rocketPos[0] >= 865:
                rocketSpeed[0] = 0
                rocketPos[0] -= rocketPos[0] - 865  # Makes it impossible to cross 865 because difference is
                # subtracted back

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

                #  prevents asteroid from stopping by getting 0 for both movement X and Y
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
                    rocketAsteroidCollision.append(count)  # says which asteroid in list has collided

            #  if rocketAsteroidCollision has a value (collision), the length is greater than its original 0,
            #  and it runs
            if len(rocketAsteroidCollision) > 0:
                for count in rocketAsteroidCollision:
                    #  rocketBaseColor = (255, 0, 0)
                    asteroidPos[count][0] = 900
                    asteroidPos[count][1] = randint(0, 800)
                    astMovementX[count] = randint(-5, 5)
                    astMovementY[count] = randint(-5, 5)
                    if astMovementX[count] == 0 and astMovementY[count] == 0:
                        astMovementX[count] = randint(-5, -1)
                    lives -= 1

                rocketAsteroidCollision = []

            # -----------------------------Drawing Everything--------------------------------#

            mainSurface.blit(mainBackground, (0, 0))
            #  Lives counter
            lifeCount = str(lives)
            textSurface = livesFont.render(f"lives: {lifeCount}", False, (255, 0, 0))
            mainSurface.blit(textSurface, (0, 0))
            #  Score/time (s) counter
            scorePos = livesFont.render(f"score: {score}", False, (255, 0, 0))
            mainSurface.blit(scorePos, (775, 0))

            #  Rocket design (All parts are connected throughout movement)
            pygame.draw.ellipse(mainSurface, rocketBaseColor, (rocketPos[0], rocketPos[1], 30, 90))  # rockets main body
            pygame.draw.polygon(mainSurface, (104, 115, 114), [(rocketPos[0] + 3, rocketPos[1] + 70),
                                                               (rocketPos[0] + 27, rocketPos[1] + 70),
                                                               (rocketPos[0] - 8, rocketPos[1] + 105),
                                                               (rocketPos[0] + 38, rocketPos[1] + 105)
                                                               ])  # Bottom of Rocket
            pygame.draw.polygon(mainSurface, rocketWingColor, [(rocketPos[0] + 2, rocketPos[1] + 20),
                                                               (rocketPos[0] + 2, rocketPos[1] + 69),
                                                               (rocketPos[0] - 12, rocketPos[1] + 60)])  # Left wing
            pygame.draw.polygon(mainSurface, rocketWingColor, [(rocketPos[0] + 28, rocketPos[1] + 20),
                                                               (rocketPos[0] + 28, rocketPos[1] + 69),
                                                               (rocketPos[0] + 42, rocketPos[1] + 60)])  # Right wing
            #  Space rocks (meteors, asteroids, comet's)
            for count in range(numAsteroids):
                pygame.draw.circle(mainSurface, asteroidColor, asteroidPos[count], asteroidSize[0])

        #  game over screen
        elif gameState == "game over":
            #  button click detection
            mousePos = pygame.mouse.get_pos()
            if ev.type == pygame.MOUSEBUTTONUP:
                if replayButtonPos[0] <= mousePos[0] <= replayButtonPos[0] + 350 and \
                        replayButtonPos[1] <= mousePos[1] <= replayButtonPos[1] + 100:
                    lives = startLives
                    nextLevelTime = levelDuration
                    gameState = "main game"
                    asteroidPos = []
                    astMovementX = []
                    astMovementY = []
                    rocketAsteroidCollision = []
                    rocketPos = [435, 250]  # rocket position

                    #  makes asteroids come in from the right side
                    numAsteroids = startNumAsteroids
                    for count in range(numAsteroids):
                        asteroidPos.append([900, randint(0, 800)])
                        astMovementX.append(0)
                        astMovementY.append(0)

                    startTime = timeNow()
                    newHighScore = False

            #  background image
            mainSurface.blit(endBackground, (0, 0))

            # Score
            highScoreTxt = f"High score: {highestScore}"
            if score > highestScore:
                highestScore = score
                newHighScore = True

            if newHighScore:
                highScoreTxt = f"New high score {highestScore}!"

            highScorePos = livesFont.render(highScoreTxt, False, (0, 255, 0))
            mainSurface.blit(highScorePos, (500, 600))
            resultSurface = livesFont.render(f"Your score: {score}", False, (255, 255, 255))
            mainSurface.blit(resultSurface, (250, 600))


            #  highest score display

            #  Game over text
            gOTextPos = gameOverText.render("Game Over", False, (255, 0, 0))
            mainSurface.blit(gOTextPos, (180, 200))
            #  play again button
            pygame.draw.rect(mainSurface, (255, 255, 255), replayButtonPos, 5)
            replayTextPos = replayText.render("Play Again", False, (0, 255, 0))
            mainSurface.blit(replayTextPos, (285, 370))
        # Surface display
        pygame.display.flip()

        clock.tick(60)  # Forces frame rate to be slower

    pygame.quit()  # Once loop is left, closes the window.


main()

# def gameOver():
#
#     mainSurface.fill((39, 1, 59))
#
#
#
# gameOver()
