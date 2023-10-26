import random


list_of_obstacles = []
def get_obstacles():
    """
    This function will be responsible for generating a lit of random numbers 
    tha with represent our obstacles in the range of the safe zone.
    """
    global list_of_obstacles
    num_of_obstacles = random.randint(1,10)
    for num in range(num_of_obstacles):
        list_of_obstacles.append((random.randint(-80,80),random.randint(-180,180)))

    return list_of_obstacles


def is_position_blocked(x,y):
    """
    This function will be responsible for checking if a position is blocked
    and it uses the list if obstacles to determine if the position is blocked
    by obstacles.
    :param x:
    :param y:
    """
    global list_of_obstacles

    for position in list_of_obstacles:
        if x in range(position[0], position[0]+4) and y in range(position[1], position[1]+4):
            return True
    return False


def is_path_blocked(x1,y1, x2, y2,):
    """
    This function will for checking if a path is blocked by obstacles.
    """
    global list_of_obstacles

    for obstacle in list_of_obstacles:
        x= obstacle[0]
        y= obstacle[1]
        if x2 in range(x, x+4) and y2 >= y and y1 < y:
            return True
        if y2 in range(y, y+4) and x2 >= x and x1 < x:
            return True
        if x2 in range(x, x+4) and y2 <= y+4 and y1 > y+4:
            return True
        if y2 in range(y, y+4) and x2 <= x+4 and x1 > x+4:
            return True
    return False

def show_position(list_of_obstacles):
    """
    This function will for displaying the coordinates of the obstacles
    """
    print("There are some obstacles:")
    if list_of_obstacles:
        for position in list_of_obstacles:
            print(f"- At position {position[0]},{position[1]} (to {position[0]+4},{position[1]+4})")


