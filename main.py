#By Kaushal Patil
import pygame
from pygame import mixer
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background2.png')
pygame.display.set_caption("Space Shooters")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)
mixer.music.load("background.wav")
mixer.music.play(-1)
# Player.
player = pygame.image.load('space-invaders.png')
xchangeplayer = 0
ychangeplayer = 0
playerX = 370
playerY = 470

# Enemy
enemy = []
changeEnemyX = []
changeEnemyY = []
enemyX = []
enemyY = []
number_of_enemies = 8

for i in range(number_of_enemies):
    enemy.append(pygame.image.load('alien2.png'))
    changeEnemyX.append(1)
    changeEnemyY.append(30)
    enemyX.append(random.randint(0, 770))
    enemyY.append(random.randint(50, 150))

# bullet
bullet = pygame.image.load('bullet.png')
bulletY = 480
bulletX = 0
changeBulletY = 5
changeBulletX = 0
bullet_state = "ready"

# planet
planet = pygame.image.load('planet.png')
planetx = 100
planety = 450
planet2 = pygame.image.load('planet2.png')
planetx2 = 600
planety2 = 350
planet3 = pygame.image.load('planet3.png')
planetx3 = 120
planety3 = 250
planet4 = pygame.image.load('planet4.png')
planetx4 = 600
planety4 = 100

# point system
point = 0
font = pygame.font.Font("freesansbold.ttf", 20)
textX = 0
textY = 20


# player placement function.
def playerposition(x, y):
    screen.blit(player, (x, y))


# enemy placement function.
def enemyposition(x, y, i):
    screen.blit(enemy[i], (x, y))


# bullet placement with the player function.
def bulletfire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 5, y + 10))


def planetposition():
    screen.blit(planet, (100, 450))
    screen.blit(planet2, (600, 350))
    screen.blit(planet3, (120, 250))
    screen.blit(planet4, (600, 100))


# score placement function.
def scoreShow():
    point_style = font.render("score:" + str(point), True, (225, 0, 0))
    screen.blit(point_style, (textX, textY))


# When bullets hit the enemy.
def onContact(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 10:
        return True
    else:
        return False


# if you don't know how to use math module this is also callable.
# def onContact2(enemyX, enemyY, bulletX, bulletY):
#    distance2 = ((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2) ** 0.5
#    if distance2 < 10:
#        return True
#    else:
#        return False

# planet placement function.
def planetPosition():
    screen.blit(planet, (planetx, planety))
    screen.blit(planet2, (planetx2, planety2))
    screen.blit(planet3, (planetx3, planety3))
    screen.blit(planet4, (planetx4, planety4))


# loser
def BYEBYE(x, y):
    point_style = font.render("GAME OVER LOLOL", True, (225, 0, 0))
    screen.blit(point_style, (overX, overY))


running = True
while running:
    # RGB= RED,GREEN,BLUE.
    screen.fill((0, 0, 0))
    # placing the background.
    screen.blit(background, (0, 0))

    # making the screen stay by using the while loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key down means when key is pressed.
        if event.type == pygame.KEYDOWN:

            # Bullet shooting when space bar pressed.
            if event.key == pygame.K_SPACE:
                laserShot = mixer.Sound("laser-shot.wav")
                laserShot.play()
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletfire(bulletX, bulletY)
            # player moves right with speed 1 when right arrow key is pressed.
            if event.key == pygame.K_RIGHT:
                xchangeplayer += 2
            # player moves right with speed 1 when left arrow key is pressed.
            if event.key == pygame.K_LEFT:
                xchangeplayer += -2

        # Key up means when key is realized.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xchangeplayer = 0
            if event.key == pygame.K_RIGHT:
                xchangeplayer = 0
    # boarder, so the player does'nt go outside the screen.
    playerX += xchangeplayer
    if playerX <= 0:
        playerX = 0
    if playerX >= 770:
        playerX = 770

    # enemy movement and boarder, so the enemy does'nt go outside the screen.
    for i in range(number_of_enemies):
        # GAME OVER HAHAHAH
        if enemyY[i] > 467:
            for j in range(number_of_enemies):
                mixer.music.stop()

                screen.fill((0, 0, 0))
                enemyX[j] = 200000
                playerX = 2958435
                bulletY = 67586756
                bulletX = 75478576
                planetx = 73645673
                planetx2 = 45656
                planetx3 = 546456
                planetx4 = 4646564
                textX = 345454
                gameOver_text = pygame.font.Font("freesansbold.ttf", 50)
                overX = 300
                overY = 250
                BYEBYE(overX, overY)

        enemyX[i] += changeEnemyX[i]
        if enemyX[i] <= 0:
            changeEnemyX[i] = 1
            enemyY[i] += changeEnemyY[i]
        elif enemyX[i] >= 770:
            changeEnemyX[i] = -2
            enemyY[i] += changeEnemyY[i]
        # if you din't use math module then change the function call.
        collision = onContact(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            destroy = mixer.Sound("destroy.wav")
            destroy.play()
            bulletY = 480
            bullet_state = "ready"
            point += 1

            enemyX[i] = random.randint(0, 770)
            enemyY[i] = random.randint(50, 100)
        enemyposition(enemyX[i], enemyY[i], i)

    # lets player shoot multiple bullets.
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # lets bullet have it's own path.
    if bullet_state == "fire":
        bulletfire(bulletX, bulletY)
        bulletY -= changeBulletY

    # calling all the images to appear on the screen.
    planetPosition()
    playerposition(playerX, playerY)
    enemyposition(enemyX[i], enemyY[i], i)
    scoreShow()

    # updates the movement of the image.
    pygame.display.update()
