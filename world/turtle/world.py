import turtle
import world.obstacles as obstacle



bot = turtle.Turtle()
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
# screen = turtle.Screen()
# screen.bgcolor('b')
min_y, max_y = -180, 180
min_x, max_x = -80, 80
bot.pencolor('cyan')


def plot_position(obstacles):
    """
    This function will plot obstacles on the robot world.
    :param obstacles:
    """
    for position in obstacles:
        bot.penup()
        x, y = position
        bot.goto(x,y)
        bot.pendown()
        bot.color('red')
        bot.begin_fill()
        bot.goto(x, y+4)
        bot.goto(x+4, y+4)
        bot.goto(x+4, y)
        bot.goto(x, y)
        bot.end_fill()
    bot.color('blue')
    bot.penup()
    bot.setpos(0,0)
    bot.fillcolor('blue')


def show_bot():
    """
    This function will show the robot in the graphic interface.
    """
    bot.penup()
    bot.setpos(-100, -200)
    bot.shape('turtle')
    bot.pensize(5)
    bot.setheading(90)
    bot.pendown()


    for i in range(2):
        bot.forward(400)
        bot.right(90)
        bot.forward(200)
        bot.right(90)
    
    bot.penup()
    bot.setpos(0,0)



def show_position(robot_name):
    bot.goto(position_x, position_y)
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, new_x, new_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        if obstacle.is_path_blocked(position_x, position_y, new_x, new_y) or obstacle.is_position_blocked(new_x, new_y):
            return False
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    # global new_x, new_y
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    if obstacle.is_position_blocked(new_x, new_y):
        return True , f"{robot_name} Sorry, there is an obstacle in the way."
    # if obs.is_path_blocked
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    # global new_x, new_y
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    if obstacle.is_position_blocked(new_x, new_y):
        return True , f"{robot_name} Sorry, there is an obstacle in the way."
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
