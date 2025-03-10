#8-14


def make_car (manufacturer:str, model:str, color:str, tow_package:bool):

    car:dict={"manufactorer":manufacturer, "model":model, "color":color, "tow_package":tow_package}
    return car

print(make_car ("pegeot", "208", "gigia", True))