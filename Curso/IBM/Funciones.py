"""def g(c):
    c = []
    #lista = [5,10,6]
    suma = 0
    for i in c:
        sumaLista = i
        suma = suma + sumaLista
        print (suma)
    
    return suma"""

# Complete the function g such that the input c is a list of integers and the output is the sum of all the elements in the list.
from ast import arg


def e(c):

    return sum(c) 

lista = [5,10,6]
print (e(lista))



"""def f(a,b):
    return a*b


print (f(2,2))"""

a=1

def add(b):
    return a+b

c=add(10)
print (c)

def f(x):
    return sum(x)

l = [2,2,5]

print (f(l))


def add(a):
    """
    add 1 to # This block show help()
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# help(add)

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)


def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

square(5)
print (square(5))

# If there is no return statement, the function returns None. The following two functions are equivalent:
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)


MJ()
MJ1()


a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
print (c1 )
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating()
isGoodRating(3)

artist = "Michael Jackson"

def printer1(artist):
    internal_var1 = artist
    print(internal_var1, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 

myFavouriteBand = "AC/DC"

# del myFavouriteBand

def getBandRating(bandname):
    # myFavouriteBand = "Deep Purple" Local variable 
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


# Collections and Functions

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    print (args)
    for argument in args:
        print(argument)


#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# Similarly, The arguments can also be packed into a dictionary as shown:

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')


def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print (myList)

def divide(a, b):
    return a / b

print(divide(5,5))
