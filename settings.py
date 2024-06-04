num_of_floors = 10
num_of_elevators = 3
hight_space_floor = 43
hight_black_line = 7
hight_floor = hight_space_floor+hight_black_line
speed = 2*hight_floor
deleay_time = 2
building_width = 100
elevator_width = 70
window_size = (building_width+10+(num_of_elevators * elevator_width), num_of_floors*hight_floor)

img_building_path = r"building.jpg"



def ind_min(list):
    """"
    return (min, index(min))
    """
    return min(enumerate(list),key  = lambda x : x[1])
