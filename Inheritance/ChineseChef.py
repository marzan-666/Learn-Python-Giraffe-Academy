'''class ChineseChef:
    def make_chicken(self):
        print("The chef makes a chicken ")

    def make_salad(self):
        print("The chef makes a salad ")

    def make_special_dish(self):
        print("The chef makes am orange chicken ")

    def make_fried_rice(self):
        print("The chef makes fried rice ")'''

#--------------------------------------------Inheritance---------------------------------------------------

from Chef import  Chef

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice ")

    def make_special_dish(self):
        print("The chef makes am orange chicken ")