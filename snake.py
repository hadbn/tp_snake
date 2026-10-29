"""
v02 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

snake = [
    [10, 15],
    [11, 15],
    [12, 15],
    ]

def damier():
    width, height = 20, 20 
    for j in range(31):
        for i in range(31):   
            rect = pg.Rect(j*20, i*20, width, height)
            e=255*((i+j)%2)
            color = (e, e, e) 
            pg.draw.rect(screen, color, rect)


# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False


    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...
    damier()
    # une recette pour dessiner un rectangle:
    

    for x,y in snake:
        rect = pg.Rect(x*20, y*20, 20, 20)
        color=(255,0,0)
        pg.draw.rect(screen, color, rect)

    direction=(1,0)
    for i in range(len(snake)):
        snake[i][0]+=direction[0]



    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
