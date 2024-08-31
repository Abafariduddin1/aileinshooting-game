import pgzrun
import random

WIDTH = 400
HEIGHT = 600
TITLE = "Shooting game"

alien = Actor("ailein.png")
alien.pos = 100, 200
message = "Shoot it."
score = 0
background_color = "white"  

def draw():
    screen.fill(background_color)  
    alien.draw()
    screen.draw.text(message, (100, 100), fontsize=60, color="Black", shadow=(1, 1), scolor="grey", gcolor="red")
    screen.draw.text(str(score), (60,100), fontsize=40, color="Black", shadow=(1,1),scolor="grey")

def moving():
    alien.pos = random.randint(0, 400), random.randint(0, 600)

def on_mouse_down(pos):
    global score
    global message
    global background_color 
    
    if alien.collidepoint(pos):
        moving()
        message = "Nice shot!"
        score += 1
        if score == 15:
            background_color = "blue"  
            message = "Congrats on 15 points"
    else:
        message = "You missed."

pgzrun.go()


 



pgzrun.go()