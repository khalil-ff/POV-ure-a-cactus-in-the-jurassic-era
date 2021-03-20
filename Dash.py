import pygame, sys # importation de pygame et sys

clock = pygame.time.Clock() # mise en place de l'horloge

from pygame.locals import * # importation des modules de pygame
from random import * # importation de random
pygame.init() # initialisation de pygame


pygame.display.set_caption('POV : ure a cactus living in the jurassic era') # mise en place du nom de la fenêtre

WINDOW_SIZE = (800,400) # mise en place de la taille de la fenêtre

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initialisation de l'écran

""" --- Importation des images --- """
# importe écran d'acceuil et game over
start_images = [pygame.image.load('images/screen/screen_0.png'), pygame.image.load('images/screen/screen_1.png'), pygame.image.load('images/screen/screen_2.png'), pygame.image.load('images/screen/screen_3.png')]
# importe les images du joueur
player_image = [pygame.image.load('images/cactus/cactus_0.png'), pygame.image.load('images/cactus/cactus_0.png'), pygame.image.load('images/cactus/cactus_0.png'),
pygame.image.load('images/cactus/cactus_1.png'), pygame.image.load('images/cactus/cactus_1.png'), pygame.image.load('images/cactus/cactus_1.png'),
pygame.image.load('images/cactus/cactus_2.png'), pygame.image.load('images/cactus/cactus_2.png'), pygame.image.load('images/cactus/cactus_2.png'),
pygame.image.load('images/cactus/cactus_3.png'), pygame.image.load('images/cactus/cactus_3.png'), pygame.image.load('images/cactus/cactus_3.png')]
"""
player_image = [pygame.image.load('images/steve/steve_01.png'), pygame.image.load('images/steve/steve_01.png'), pygame.image.load('images/steve/steve_01.png'),
pygame.image.load('images/steve/steve_02.png'), pygame.image.load('images/steve/steve_02.png'), pygame.image.load('images/steve/steve_02.png'),
pygame.image.load('images/steve/steve_01.png'), pygame.image.load('images/steve/steve_01.png'), pygame.image.load('images/steve/steve_01.png'),
pygame.image.load('images/steve/steve_03.png'), pygame.image.load('images/steve/steve_03.png'), pygame.image.load('images/steve/steve_03.png')]
for i in range(len(player_image)):
    player_image[i] = pygame.transform.scale(player_image[i], (50,60))
"""
# récupère les images des ennemis
enemy_images = [pygame.image.load('images/dino/dino_2.png'), pygame.image.load('images/dino/dino_2.png'), pygame.image.load('images/dino/dino_2.png'), pygame.image.load('images/dino/dino_2.png'), pygame.image.load('images/dino/dino_2.png'), pygame.image.load('images/dino/dino_2.png'),
pygame.image.load('images/dino/dino_3.png'), pygame.image.load('images/dino/dino_3.png'), pygame.image.load('images/dino/dino_3.png'), pygame.image.load('images/dino/dino_3.png'), pygame.image.load('images/dino/dino_3.png'), pygame.image.load('images/dino/dino_3.png')]
# images des éléments de décor
cloud_images = [pygame.image.load('images/clouds/cloud_0.png'), pygame.image.load('images/clouds/cloud_1.png'), pygame.image.load('images/clouds/cloud_2.png')]
skeleton_images = [pygame.image.load('images/skeleton/skeleton_0.png'), pygame.image.load('images/skeleton/skeleton_1.png'), pygame.image.load('images/skeleton/skeleton_2.png')]
backG = pygame.image.load('images/background.png')
platform_image = pygame.image.load('images/grass.png')
buisson = pygame.image.load('images/bush.png')
galet = pygame.image.load('images/pebble.png')
herbe = pygame.image.load('images/small grass.png')

""" --- Importation de la musique --- """
file = 'musique/son.mp3'
pygame.mixer.init() # initialise la fonction mixer de pygame
pygame.mixer.music.load(file) # importe notre fichier mp3
pygame.mixer.music.play(-1) # la musique entre dans une boucle infinie donc se répetera si terminée (vous serez pas assez fort pour survivre toute la musique)

""" --- Variables du joueur --- """
jump = False # est-ce qu'on est en train de sauter ? (booléen)
jumpCount = 10 # valeur utilisée dans la fonction 2nd degrès plus tard chez player()
walkCount = 0 # nombre de pas du joueur (pour l'animation)

player_location = [50, WINDOW_SIZE[1]/2] # coordonnées initiales du joueur
player_vel = 8 # vitesse du joueur
player_y_momentum = 0 # valeur ajoutée à la coordonnée y du joueur
player_hitbox = (player_location[0] + 7, player_location[1] + 1, 45, 52) # hitbox du joueur (utile pour les collisions)

""" --- Variables de la fenêtre --- """
platform_y = WINDOW_SIZE[1] * 0.6 # coordonnée y sur laquelle le joueur a une mobilité
b = randint(1,2) # choisi aléatoirement si il fait jour ou nuit

start_ = False # est-ce que la partie à comencée ? (booléen)
score = 0 # score de départ
score_gained = False # est-ce que l'on gagne des points ? (booléen)

""" --- Variables des ennemis --- """
enemy_walkcount = 0
enemy_vel = 4 # vitesse initiale de l'ennemi
vel_Count = 0 # utilisé pour l'ennemi qui accélère au fur et à mesure que l'on avance dans le jeu
is_enemy = False # est-ce qu'un ennemi est à l'écran ? (booléen)
enemy_Count = 0 # nombre de pas de l'ennemi (pour l'animation)

enemy_x = 900 # coordonnée x initiale des ennemis
enemy_y = WINDOW_SIZE[1] * 0.60 # coordonnée y des ennemis
enemy_hitbox = (enemy_x, enemy_y + 1, 32, 32) # hitbox de l'ennemi

""" --- Variables des éléments de décor --- """
bush_x = randint(1000,1400) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en x
pebble_x = randint(1000,1200) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en x
grass_x = randint(1000,1400) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en x
skeleton_x = randint(1200,1400) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en x
cloud_x = randint(1000,1200) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en x
pebble_y = randint(255, 300) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en y
grass_y = randint(255, 300) # fenêtre d'ouverture dans laquelle l'objet peut apparaître en y
c = randint(0,2) # choisi aléatoirement l'image utilisée pour les nuages (c pour clouds)
s = randint(0,2) # choisi aléatoirement l'image utilisée pour les squelettes (s pour skeletons)

""" --- Différentes fonctions --- """

""" - Affichage des dessins - """
def redrawGameWindow():
    global walkCount, enemy_Count, player_hitbox, enemy_hitbox, bush_x, pebble_x, pebble_y, grass_x, grass_y, cloud_x, skeleton_x, c, s

    # fond : jour ou nuit
    if b == 1:
        screen.fill((85,185,227)) # couleur du ciel : jour
        screen.blit(backG, (0,0)) # affichage du soleil
    else:
        screen.fill((5, 24, 31)) # couleur du ciel : nuit
        screen.blit(backG, (0,0-(WINDOW_SIZE[1] - platform_y))) # affichage de la lune

    # affichage : plateforme
    screen.blit(platform_image, (0, platform_y + 25))

    # affichage : décor
    # buisson
    screen.blit(buisson, (bush_x, platform_y - 25)) # affichage du buisson
    bush_x -= 2 # mouvement
    if bush_x <= -100:
        bush_x = randint(900,1200) # nouvelle position une fois que sorti de l'écran
    # herbe
    screen.blit(herbe, (grass_x, grass_y)) # affichage de l'herbe
    grass_x -= 3 # mouvement
    if grass_x <= -27:
        grass_x = randint(900,1200) # nouvelle position une fois que sorti de l'écran
        grass_y = randint(255, 300) # nouvelle position une fois que sorti de l'écran
    # galet
    screen.blit(galet, (pebble_x, pebble_y)) # affichage du galet
    pebble_x -= 3 # mouvement
    if pebble_x <= -27:
        pebble_x = randint(900,1200) # nouvelle position une fois que sorti de l'écran
        pebble_y = randint(255, 300) # nouvelle position une fois que sorti de l'écran
    # squelette
    screen.blit(skeleton_images[s], (skeleton_x, platform_y + 100)) # affichage des squelettes
    skeleton_x -= 3 # mouvement
    if skeleton_x <= -100:
        skeleton_x = randint(900,1200) # nouvelle position une fois que sorti de l'écran
        s = randint(0,2) # nouvelle image aléatoire une fois que sorti de l'écran
    # nuages
    screen.blit(cloud_images[c], (cloud_x, platform_y + 25 -200)) # affichage des nuages
    cloud_x -= 1 # mouvement
    if cloud_x <= -64:
        cloud_x = randint(900,1200) # nouvelle position une fois que sorti de l'écran
        c = randint(0,2) # nouvelle image aléatoire une fois que sorti de l'écran

    # animation : joueur
    if walkCount >= 12:
        walkCount = 0 # une fois qu'on a traversé toutes les images de la liste player_image, on revient à la première
    screen.blit(player_image[walkCount], player_location) # affichage du joueur
    walkCount += 1 # image suivante

    # animation : ennemis
    if enemy_Count >= 12:
        enemy_Count = 0 # une fois qu'on a traversé toutes les images de la liste enemy_images, on revient à la première
    screen.blit(enemy_images[enemy_Count], (enemy_x, enemy_y)) # affichage de l'ennemi
    enemy_Count += 1 # image suivante

    # hitbox : player
    player_hitbox = (player_location[0] + 7, player_location[1] + 1, 42, 52) # redéfini la hitbox selon la nouvelle position du joueur
    #pygame.draw.rect(screen, (255,0,0), player_hitbox, 2)
    # vous pouvez afficher la ligne ci-dessus pour rendre la hitbox du joueur visible

    # hitbox : enemy
    enemy_hitbox = (enemy_x, enemy_y , 45, 52) # redéfini la hitbox selon la nouvelle position de l'ennemi
    #pygame.draw.rect(screen, (255,0,0), enemy_hitbox, 2)
    # vous pouvez afficher la ligne ci-dessus pour rendre la hitbox de l'ennemi visible

    # affichage : score
    screen.blit(pygame.font.SysFont('Alien Encounters', 25).render("Score: " + str(score), True, (100,100,242)  ), (690,20))

    pygame.display.update() # actualise l'affichage

""" - Joueur - """
def player():
    global player_y_momentum, player_location, jump, player_image, platform_y, jumpCount

    # saut : fonction 2nd degrès pour la trajectoire (peut modifier jumpCount et neg pour changer la façon dont le joueur saute)
    if jump:
        if jumpCount >= -10:
            neg = 5
            if jumpCount < 0:
                neg = -neg
            player_location[1] -= (jumpCount ** 2) / neg
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10
    # gravité : augmentation de la vitesse de chute (seulement si on ne saute pas déjà)
    else:
        player_y_momentum += 0.3

    # collision : mobilité sur la plateforme
    if player_location[1] <= platform_y and player_location[1] + player_y_momentum >= platform_y:
        player_location[1] = platform_y - 5 # si le joueur se retrouve à traverser la plateforme, on le remet sur la plateforme

    # gravité : changement des coordonnées y du joueur (seulement si on ne saute pas déjà)
    else:
        if not jump:
            player_location[1] += player_y_momentum

    if player_y_momentum > 8:
        player_y_momentum = 8 # vitesse maximale de chute du joueur

""" - Mouvement de l'ennemi - """
def enemy_movement():
    global enemy_walkcount, enemy_x, is_enemy, enemy_vel, vel_Count

    if not is_enemy:
        is_enemy = True # fait apparaître un ennemi dès qu'il n'y en a plus à l'écran
    else:
        if enemy_x - enemy_vel >= -32:
            enemy_x -= enemy_vel
            if enemy_walkcount + 1 >= 30:
                enemy_walkcount = 0
            else:
                enemy_walkcount += 1
        else:
            enemy_x = 900 # ennemi non visible à l'écran
            is_enemy = False

    vel_Count += 1
    if enemy_vel <= 13: # vitesse maximale de l'ennemi (modifiable selon la difficulté voulue)
        if vel_Count == 1000:
            enemy_vel += 1 # on ajoure 1 à la vélocité de l'ennemi toutes les 1000 frames
            vel_Count = 0

""" - Collisions - """
def hit():
    if player_hitbox[1] <= enemy_hitbox[1] + enemy_hitbox[3] and player_hitbox[1] + player_hitbox[3] >= enemy_hitbox[1]:
        if player_hitbox[0] + player_hitbox[2] >= enemy_hitbox[0] and player_hitbox[0] <= enemy_hitbox[0] + enemy_hitbox[2]:
            gameover() # fait appel à la fonction gameover() si jamais la hitbox du joueur et celle de l'ennemi entrent en contact

""" - Contrôles - """
def controls():
    global moving_left, moving_right, jump, player_image, player_location, player_vel, WINDOW_SIZE

    for event in pygame.event.get(): # boucle de l'évènement
        if event.type == QUIT: # vérification du statue de la fenêtre (pour éviter l'affichage d'erreurs)
            pygame.quit() # arrêt de pygame si sorti de la fenêtre
            sys.exit() # arrêt du script si sorti de la fenêtre

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player_location[0] + 32 < WINDOW_SIZE[0]:
        player_location[0] += player_vel # va à droite
    if keys[pygame.K_LEFT] and player_location[0] > player_vel:
        player_location[0] -= player_vel-1 # va à gauche
    if keys[pygame.K_UP]:
        jump = True # enclanche le début du saute

""" - Score - """
def draw_score():
    global score, score_gained
    if not score_gained: # si le joueur n'a pas déjà gagné de points pendant que l'ennemi était là
        if player_location[0] > enemy_x: # et si le joueur à évité l'ennemi
            score += 10 # alors le jouer gagne 10 points
            score_gained = True
    else:
        if not is_enemy:
            score_gained = False # sinon il ne gagne rien

""" - Ecran d'acceuil - """
def start():
    global start_, walkCount, enemy_Count
    # affichage de l'écran d'acceuil
    screen.fill((22,22,22))
    screen.blit(start_images[0], (0,0))
    pygame.display.flip()
    while not start_: # tant qu'on n'a pas commencé, attendre
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    start_ = True # si le joueur appuie sur une touche, la partie commence
                    waiting = False # on n'attend plus

""" - Game over - """
def gameover():
    global game_over
    # affichage de l'écran d'acceuil
    screen.blit(start_images[1], (0,0))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    waiting = True # on attend
    while waiting: # tant qu'on attend
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False # si le joueur appuie sur une touche, on attend plus
                reset() # appel de la fonction reset qui recommence la partie

""" - Reset des variables - """
def reset():
    global enemy_walkcount, score, enemy_x, is_enemy, score_gained, moving_right, moving_left, walkCount, enemy_Count, jump, jumpCount, player_location, player_y_momentum, b, bush_x, pebble_x, grass_x, skeleton_x, cloud_x, pebble_x, grass_x, c, s, enemy_vel, vel_Count
    # redéfinition de toutes les valeurs de départ
    enemy_walkcount = 0
    score = 0
    enemy_x = 900
    is_enemy = False
    score_gained = False
    moving_right = False
    moving_left = False
    walkCount = 0
    jump = False
    jumpCount = 10
    player_location = [50,WINDOW_SIZE[1]/2]
    player_y_momentum = 0
    b = randint(1,2)
    bush_x = randint(1000,1400)
    pebble_x = randint(1000,1200)
    grass_x = randint(1000,1400)
    skeleton_x = randint(1200,1400)
    cloud_x = randint(1000,1200)
    pebble_y = randint(255, 300)
    grass_y = randint(255, 300)
    c = randint(0,2)
    s = randint(0,2)
    enemy_vel = 4 # vitesse
    vel_Count = 0

""" --- Boucle infinie --- """
start()

while True:
    redrawGameWindow()
    draw_score()
    enemy_movement()
    player()

    controls()

    hit()

    clock.tick(60) # 60 images par seconde (fps)
