num_of_floors = 10
num_of_elevators = 3
height_space_floor = 43
height_black_line = 7
height_floor = height_space_floor+height_black_line
speed = 2*height_floor
deleay_time = 2
building_width = 100
elevator_width = 70
window_size = (building_width+10+(num_of_elevators * elevator_width), num_of_floors*height_floor)
sound_path = r"ding.mp3"
elevator_pic = r"C:\Users\meir\Desktop\elv.png"
img_building_path = r"building.jpg"
size_bottun = building_width / 5
FONT_SIZE = 15



def ind_min(list):
    """"
    return (index(min),min)
    """
    return min(enumerate(list),key  = lambda x : x[1])
