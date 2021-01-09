# Day 21 Inheritance,Slicing and Snake Game Part 2

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("Swims in water")


# nemo = Fish()
# nemo.swim()
# nemo.breathe()

piano_keys=["a","b","c","d","e","f","g"]
piano_tup=("a","b","c","d","e","f","g")

print(piano_tup[2:4])
