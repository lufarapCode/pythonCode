""""
class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
        print (self.owner_number)

make="BMW"
model="M3"
color="red"

my_car = Car(make,model,color)

my_car.car_info()
for i in range(5):
    my_car.sell()

my_car.car_info()


"""
## Probando la libreria matplotlib

"""x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()"""

"""plt.style.use('_mpl-gallery-nogrid')

# make data: correlated + noise
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3

# plot:
fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=20)

ax.set(xlim=(-2, 2), ylim=(-3, 3))

plt.show()"""

import numpy as np
import matplotlib.pyplot as plt 




class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 


# Create an object RedCircle

RedCircle = Circle(0, 'red')
#print (dir(RedCircle))

#RedCircle.radius = 1
#print(RedCircle.radius)

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# RedCircle.drawCircle()

BlueCircle = Circle(radius=100)

#BlueCircle.drawCircle()


#

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
FatYellowRectangle = Rectangle(20, 5, 'pink')

SkinnyBlueRectangle.drawRectangle()
FatYellowRectangle.drawRectangle()