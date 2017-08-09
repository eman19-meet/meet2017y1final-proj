import turtle
import random
square_size = 20
turtle.tracer(1,0)
wall_list = []
def draw_square(x,y,a, color):
    drawer = turtle.clone()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(x,y)
    drawer.pendown()
    drawer.begin_fill()
    drawer.goto(x,y-a)
    drawer.goto(x+a,y-a)
    drawer.goto(x+a,y)
    drawer.goto(x,y)
    drawer.end_fill()
    drawer.fillcolor(color)
    wall_list.append(drawer.pos())
################################ making a random maze ##########################
def random_maze(n):
    """
    Choose n random positions
    on the maze board, add them
    to a list which will be returned
    later

    It will also fill the area that
    a block occupies
    """
    all_points = []
    for x in range(-250, 250 - square_size +1, square_size):
        for y in range(-250 + square_size, 250 + 1, square_size):
            all_points.append((x,y))

    set_wall_list = set()
    while len(set_wall_list) != n:
        rand_index = random.randint(0, len(all_points) - 1)
        set_wall_list.add(all_points[rand_index])
        draw_square(all_points[rand_index][0], all_points[rand_index][1], square_size, "black")

    return list(set_wall_list)    
#window
x_size = 600
y_size = 600
turtle.hideturtle()
turtle.setup(x_size, y_size)

#border
border = turtle.clone()
border.hideturtle()
border.pensize(5)
border.penup()
border.goto(250,250)
border.pendown()
border.goto(250,-250)
border.goto(-250,-250)
border.goto(-250,250)
border.goto(250,250)
border.penup()

# random_maze ( how many blocks )
wall_list = random_maze(150)



#################################the food and the score##########################

#printing the score on the screen
turtle.hideturtle()
turtle.penup()
turtle.pensize(5)
turtle.goto(175, 250)
turtle.pendown()
turtle.goto(175, 280)
turtle.goto(110, 280)
turtle.goto(110, 250)
turtle.goto(175, 250)
##############################
score=0
turtle.register_shape('car.gif')
car = turtle.clone()
car.shape("car.gif")
turtle.penup()
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
number_of_burgers=random.randint(5,15)
turtle.register_shape("burger.gif")
food = turtle.clone()
food.shape("burger.gif")
food_pos=[]
food_stamps=[]
food_list = []
all_points = []
for x in range(-250, 250 - square_size + 1, square_size):
    for y in range(-250 + square_size, 250 + 1, square_size):
        all_points.append((x,y))

s_all_points = set(all_points)
s_wall_points = set(wall_list)
s_free_points = s_all_points - s_wall_points
free_points = list(s_free_points)

def make_food():

    for i in range(number_of_burgers):
        food_list.append(food.clone())


    if car.pos() in food_pos:
        food_ind=food_pos.index(car.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        score+=1
        turtle.penup() 
        turtle.goto(142.5, 260.5)
        turtle.write(score)
        c = turtle.clone()
        c.penup()
        c.showturtle()
        c.shape("square")
        c.color("white")
        c.goto(142.5, 265)

    for clone in food_list:
        rand_index = random.randint(0, len(free_points) - 1)
        position = free_points[rand_index]
        while position in wall_list:
            rand_index = random.randint(0, len(free_points) - 1)
            position = free_points[rand_index]
            

        food_pos.append(position)
        clone.goto(position)
        b=clone.stamp()
        food_stamps.append(b)
        clone.hideturtle()
make_food()


#####################################car movement################################
import turtle

sizex = 800
sizey = 500

turtle.setup(sizex,sizey)

# car movement


turtle.penup()

square_size = 20
starlen = 1
car_pos_list = []
car_stamp_list =[]
car = turtle.clone()
car.shape("turtle")
turtle.hideturtle()

for i in range (starlen):
    mycarx = car.pos()[0]
    mycary = car.pos()[1]
    mycarx += 20
    car.goto(mycarx,mycary)
    car_pos_list.append(car.pos())
    

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

UP  = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP

def up1():
    global direction
    direction = UP 
    move_car()
    print("u press up")
    
def left1():
    global direction
    direction = LEFT
    move_car()
    print("u press left")
    
def right1():
    global direction
    direction = RIGHT
    move_car()
    print("u press right")
    
def down1():
    global direction
    direction = DOWN
    move_car()
    print("u press down")
    
def move_car():
    global direction
    my_car = car.pos()
    carx_pos = my_car[0]
    cary_pos = my_car[1]
    
    if direction == UP:
        car.goto(carx_pos , cary_pos + square_size)
        print("go up")
    elif direction == DOWN:
        car.goto(carx_pos , cary_pos - square_size)
        print("go down")
    elif direction == RIGHT:
        car.goto(carx_pos + square_size , cary_pos)
        print("go right")
    elif direction == LEFT:
        car.goto(carx_pos - square_size , cary_pos)
        print("go left")
    
        
    

    my_car = car.pos()
    car_pos_list.append(my_car)
    new_car_stamp = car.stamp()
    car_stamp_list.append(new_car_stamp)
    old_car_stamp = car_stamp_list.pop(0)
    car.clearstamp(old_car_stamp)
    car_pos_list.pop(0)
    




turtle.onkeypress(up1 ,UP_ARROW)
turtle.onkeypress(left1 , LEFT_ARROW)
turtle.onkeypress(down1 , DOWN_ARROW)
turtle.onkeypress(right1 , RIGHT_ARROW)
turtle.listen()


#################################timer##########################################

import turtle


import time



turtle.hideturtle()
turtle.penup()
turtle.pensize(5)
turtle.goto(250, 250)
turtle.pendown()
turtle.goto(250, 280)
turtle.goto(180, 280)
turtle.goto(180, 250)
turtle.goto(250, 250)
turtle.penup() 
turtle.goto(215, 255)


timer = turtle.clone()
b = turtle.clone()
b.penup()
b.showturtle()
b.shape("square")

b.color("white")
b.goto(223,265)

def countdown(t):    
    while t >= 0:
        b.stamp()
        timer.write(t)
        time.sleep(1)
        t -= 1        
    quit()

countdown(10)
#################################################################################
