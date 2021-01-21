class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")

my_car=Car(make="nissan")
print(my_car.model)

# use unlimited Arguments known as unlimited position arguments
def add(*args):
    sum=0
    for n in args:
        sum=sum+n
    print(sum)
add(1,2,3,4,5,6,7,8,10,11,1)
add(1,9)

# Keyword Arguments / optional keyword arguments
def calculate(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["mul"]
    print(n)


calculate(2,add=3,mul=5)



