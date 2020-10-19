class Student:

   def __init__(self, name, major, cgpa):
       self.name = name
       self.major = major
       self.cgpa = cgpa

   def on_honor_roll(self):
       if self.cgpa >= 3.5:
           return True
       else:
           return False
