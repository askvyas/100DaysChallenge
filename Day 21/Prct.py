# Day 21 Inheritance and Snake Game Part 2

class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__()
    def swim(self):
        print("Swims in water")

nemo=Fish()
nemo.swim()
nemo.breathe()