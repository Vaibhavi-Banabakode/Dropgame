import pygame
import random
import math
pygame.mixer.init()
pygame.init()

font = pygame.font.SysFont(None, 55)
width = 800
height = 600
aqua = (0, 255, 255)
over = True
img_x = 300
bucketx_chg = 4
img_y = 470
clock = pygame.time.Clock()
fps = 50
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("***Drop Game***")
icon = pygame.image.load("images.jfif")
pygame.display.set_icon(icon)
image = pygame.image.load("drop.png")
drop_x = random.randint(20, 740)
drop_y = 0
dropy_chg = 3
score = 0
image1 = pygame.image.load("bucket.png")
bg = pygame.image.load("back.png")


def score_display(text, color, s_x, s_y):
    text_score = font.render(text, True, color)
    screen.blit(text_score, [s_x, s_y])


def collision(drop_x, drop_y, img_x, img_y):
    dist = math.sqrt((math.pow(drop_x - img_x, 2)) + (math.pow(drop_y - img_y, 2)))
    if dist < 39.9:
        return True
    else:
        return False


def drop(x, y):
    screen.blit(image, (x, y))


def bucket(x, y):
    screen.blit(image1, (x, y))


running = True
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            img_x = img_x + bucketx_chg
        if event.key == pygame.K_LEFT:
            img_x = img_x - bucketx_chg
    if img_x <= 0:
        img_x = 0
    elif img_x >= 700:
        img_x = 700
    drop_y += dropy_chg
    col = collision(drop_x, drop_y, img_x, img_y)
    if col:
        score += 1
        pygame.mixer.music.load('Beep_Short.mp3')
        pygame.mixer.music.play()
        drop_x = random.randint(20, 740)
        drop_y = 0

    bucket(img_x, img_y)
    drop(drop_x, drop_y)
    if drop_y >= height:
        over = False
    if over == False:
        pygame.mixer.music.load('gameover.mp3')
        pygame.mixer.music.play()
        screen.fill(aqua)
        text = font.render("GAME OVER!!", True, (255, 0, 0))
        screen.blit(text, [300, 300])
    score_display("SCORE :" + str(score), (200, 0, 0), 5, 5)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
