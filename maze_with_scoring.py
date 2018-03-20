# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SLIGHTLY_LESS_RED = (200, 0, 0)
PURPLE = (208, 73, 229)


# Make a player
player1 =  [380, 290, 25, 25]
vel1 = [0, 0]
player1_speed = 2
score1 = 0

# make walls
wall1 =  [0, 0, 25, 600]
wall2 =  [0, 0, 25, 25]
wall3 =  [775, 0, 800, 600]
wall4 =  [0, 575, 50, 600]
wall5 =  [350, 250, 25, 100]
wall6 =  [425, 250, 25, 100]
wall7 =  [400, 250, 50, 25]
wall8 =  [375, 325, 25, 25]
wall9 =  [350, 25, 25, 225]
wall10 =  [425, 50, 25, 200]
wall11 =  [375, 200, 25, 25]
wall12 =  [400, 150, 25, 25]
wall13 =  [375, 100, 25, 25]
wall14 =  [400, 50, 25, 25]
wall15 =  [350, 350, 25, 200]
wall16 =  [425, 350, 25, 225]
wall17 =  [400, 375, 25, 25]
wall18 =  [375, 425, 25, 25]
wall19 =  [400, 475, 25, 25]
wall20 =  [375, 525, 25, 25]
wall21 =  [25, 250, 325, 100]
wall22 =  [75, 575, 750, 25]
wall23 =  [75, 525, 25, 50]
wall24 =  [50, 525, 25, 25]
wall25 =  [50, 450, 25, 50]
wall26 =  [50, 375, 25, 50]
wall27 =  [100, 375, 25, 25]
wall28 =  [25, 425, 50, 25]
wall29 =  [100, 425, 25, 25]
wall30 =  [50, 600, 25, 25]
wall31 =  [50, 0, 750, 25]
wall32 =  [25, -25, 25, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19,
         wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28
         , wall29, wall30, wall31, wall32]

#make secret walls
secret_wall1 =  [375, 250, 25, 25]
secret_wall2 =  [400, 325, 25, 25]

secret_walls =  [secret_wall1, secret_wall2]

# Make teleporters
teleporter1 =  [50, 575, 25, 25, 25, 25]
teleporter2 =  [25, 0, 25, 25, 50, 550]

teleporters = [teleporter1, teleporter2]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]

#Sounds
coin_sound = pygame.mixer.Sound("key_event_guinea.ogg")

#images
player_guinea = pygame.image.load('guinea.png')
coin_lettuce = pygame.image.load('lettuce.png')

# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if left:
        vel1[0] = -player1_speed
    elif right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]

    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coin_sound.play()
        
    if len(coins) == 0:
        win = True

    '''teleport'''
    for t in teleporters:
        if player1[:4] == t[:4]:
            player1[0] = t[4]
            player1[1] = t[5]
    
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    #pygame.draw.rect(screen, WHITE, player1)
    loc = player1[:2]
    screen.blit(player_guinea, (loc))
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        screen.blit(coin_lettuce, c)

    for s in secret_walls:
        pygame.draw.rect(screen, SLIGHTLY_LESS_RED, s)

    for t in teleporters:
        pygame.draw.rect(screen, PURPLE, t[:4])
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
