from random import randint
import pygame as pg

TAILLE_CASE = 20
NB_COLONNES = 30
NB_LIGNES = 30
LARGEUR = NB_COLONNES * TAILLE_CASE
HAUTEUR = NB_LIGNES * TAILLE_CASE
COULEUR_1 = (255, 255, 255) 
COULEUR_2 = (0, 0, 0)  
COULEUR_SERPENT=(0,255,0)
COULEUR_FRUIT=(255,0,0)

serpent = [(10, 15), (11, 15), (12, 15)]
direction = (1, 0)
fruit = (randint(0, NB_COLONNES - 1), randint(0, NB_LIGNES - 1))

def dessiner_damier(ecran):
    for ligne in range(NB_LIGNES):
        for colonne in range(NB_COLONNES):
            if (ligne + colonne) % 2 == 0:
                couleur = COULEUR_1
            else:
                couleur = COULEUR_2
            x = colonne * TAILLE_CASE
            y = ligne * TAILLE_CASE
            rect = pg.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
            pg.draw.rect(ecran, couleur, rect)

def dessiner_serpent(ecran, positions_serpent):
    for case in positions_serpent:
        x_pixel = case[0] * TAILLE_CASE
        y_pixel = case[1] * TAILLE_CASE
        
        rect = pg.Rect(x_pixel, y_pixel, TAILLE_CASE, TAILLE_CASE)
        pg.draw.rect(ecran, COULEUR_SERPENT, rect)

def dessiner_fruit(ecran, position_fruit):
    x_pixel = position_fruit[0] * TAILLE_CASE
    y_pixel = position_fruit[1] * TAILLE_CASE
    rect = pg.Rect(x_pixel, y_pixel, TAILLE_CASE, TAILLE_CASE)
    pg.draw.rect(ecran, COULEUR_FRUIT, rect)


pg.init()

screen = pg.display.set_mode((LARGEUR, HAUTEUR))
clock = pg.time.Clock()
score = 0
pg.display.set_caption(f"Score: {score}")

running = True
while running:

    clock.tick(5)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pg.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pg.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pg.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    tete_x, tete_y = serpent[-1]
    nouveau_x = tete_x + direction[0]
    nouveau_y = tete_y + direction[1]
    nouvelle_tete = (nouveau_x, nouveau_y)

#Ajout perso si il touche un mur il meurt
    if nouveau_x < 0 or nouveau_x >= NB_COLONNES or nouveau_y < 0 or nouveau_y >= NB_LIGNES: 
        print(f"Score final : {score}")
        running = False 
        continue
#Si il se mord la queue il meurt
    if nouvelle_tete in serpent:
        print(f"Score final : {score}")
        running = False 
        continue

#On ajoute comme si il grandissait
    serpent.append(nouvelle_tete)

    if nouvelle_tete == fruit:
        fruit = (randint(0, NB_COLONNES - 1), randint(0, NB_LIGNES - 1))
        score += 1
        pg.display.set_caption(f"Score: {score}")
    else:
        #On retire la tete ajoutée si il a pas mangé le fruit
        serpent.pop(0)


    dessiner_damier(screen)
    dessiner_fruit(screen, fruit)
    dessiner_serpent(screen, serpent)

    pg.display.update()

pg.quit()