import turtle
import time
import random

WIDTH, HEIGHT = 800, 800
COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink', 'brown', 'cyan', 'black']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int (racers)
        else:
            print("Invalid input. Please enter a number between 2 and 10.")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid input. Please enter a number between 2 and 10.") 

def race(colors):
    turtles = create_turtles(colors)
    winner = None
    while not winner:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)
           
            x, y = racer.position()
            if y >= HEIGHT // 2 - 20:
                winner = racer.pencolor()
                break
    return winner   


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #set position
        racer.goto(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtles(): 
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


racers = get_number_of_racers()
init_turtles()
random.shuffle(COLORS)
COLORS = COLORS[:racers]

race_winner = race(COLORS)
print(f"The winner is: {race_winner}") 