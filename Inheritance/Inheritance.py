# from Chef import Chef
# from ChineseChef import ChineseChef

# myChef = Chef()
# myChef.make_chicken()
# myChef.make_salad()
# myChef.make_special_dish()

# myChef = ChineseChef()
# myChef.make_special_dish()
# myChef.make_fried_rice()

#------------------------------------ Inheritance---------------------------------------------------------------
from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

myChef = ChineseChef()
myChef.make_special_dish()
myChef.make_fried_rice()

myChef.make_chicken() # make chicken method removed from chinese chef but still can access it by inheritance

myChef.make_special_dish()
