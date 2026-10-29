from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

#initialisation
direction = (1,0) 
score = 0
end_time = 0
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
            e = 255*((i+j)%2)
            color = (e, e, e) 
            pg.draw.rect(screen, color, rect)

def fruit(x,y):
     color = (255, 0, 0) 
     rect = pg.Rect(x*20, y*20, 20, 20)
     pg.draw.rect(screen, color, rect)

def lose(snake):
    unique=[]
    for position in snake:
        if position in unique :
            return True
        unique.append(position)
    return False
     

#premier fruit
x_fruit=randint(0,31)
y_fruit=randint(0,31)
fruit(x_fruit,y_fruit)

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running and (not lose(snake)) and snake[-1][0]>=0 and snake[-1][1]>=0 and snake[-1][0]<30 and snake[-1][1]<30:
    
    clock.tick(4)
    
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

            if event.key == pg.K_UP and direction!=(0,1):
                direction = (0,-1)

            if event.key == pg.K_DOWN and direction!=(0,-1):
                direction = (0,1)

            if event.key == pg.K_RIGHT and direction!=(-1,0):
                direction = (1,0)

            if event.key == pg.K_LEFT and direction!=(1,0):
                            direction = (-1,0)

    damier()

    #gestion fruit et déplacement
    if [x_fruit,y_fruit] in snake: 
        score+=1       
        x_fruit=randint(0,31)
        y_fruit=randint(0,31)
        snake.append([snake[-1][0]+direction[0],snake[-1][1]+direction[1]])
    else: 
        snake.append([snake[-1][0]+direction[0],snake[-1][1]+direction[1]])
        snake.pop(0)

    pg.display.set_caption(f"Score: {score}")
    fruit(x_fruit,y_fruit)

    #affichage du snake
    for x,y in snake:
        rect = pg.Rect(x*20, y*20, 20, 20)
        color=(0,255,0)
        pg.draw.rect(screen, color, rect)

    end_time=pg.time.get_ticks()  #on met à jours le temps de fin

    pg.display.update()

end_time=pg.time.get_ticks()
end=True
while end :
    police = pg.font.SysFont("arial", 32)
    screen.fill((255,255,255))
    text_end = police.render("GAME OVER", True, (0, 0, 0))
    screen.blit(text_end, (220, 250))
     
    if pg.time.get_ticks() - end_time > 3000: #c'est 2000ms soit 2s
        end=False

    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()

