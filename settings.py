NUM_OF_FLOORS = 10
NUM_OF_ELEVATORS = 3
HEIGHT_FLOOR = 50
BUILDING_WIDTH = 50
NUM_OF_FLOORS,NUM_OF_ELEVATORS = int(input("nom of floors")),int(input("nom of elevators"))

dim_y = HEIGHT_FLOOR*NUM_OF_FLOORS
if dim_y > 620:
    HEIGHT_FLOOR = int(620/NUM_OF_FLOORS)
HEIGHT_BLACK_LINE = int(HEIGHT_FLOOR/7)
ELEVATOR_WIDTH = HEIGHT_FLOOR    




    

SPEED = 2*HEIGHT_FLOOR
DELEAY_TIME = 2
WINDOW_SIZE = (BUILDING_WIDTH+(NUM_OF_ELEVATORS * ELEVATOR_WIDTH), NUM_OF_FLOORS*HEIGHT_FLOOR)
SOUND_PATH = r"ding.mp3"
ELEVATOR_PIC = r"elv.png"
IMG_BUILDING_PATH = R"BUILDING.JPG"
SIZE_BOTTUN = BUILDING_WIDTH / 5
FONT_SIZE = int(HEIGHT_FLOOR/3)



def ind_min(list):
    """"
    return (index(min),min)
    """
    return min(enumerate(list),key  = lambda x : x[1])
