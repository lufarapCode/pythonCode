
x = 'a'
if(x=='a'):
    print("this is a")
else:
    print("this is  not a") 

# Click here for the solution
rating = 8.5
if rating > 8:
    print ("This album is Amazing!")


rating = 7.5
if rating > 8:
    print ("This album is Amazing!")
elif rating <= 8 :
    print ("This album is ok")


# ***** Loops ********

A=[3,4,5]
B = ['A', 'R', 'D']
for i in A:
    print (i)
# Find the value of  x  that will print out the sequence  1,2,..,10 :
x= 11
y=1
while(y != x):
    print(y)
    y=y+1


dates = [1982,1980,1973]
N = len(dates)
print ("len: " , type(N))

for i in range(N):
    print ("i:", i)
    print(dates[i]) 

# or 

for year in dates:
    print (year)


squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

# Write a for loop the prints out all the element between -5 and 5 using the range function.

for i in range(-5,5):
    print (i)

# Print the elements of the following list: 
# Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for i in Genres:
    print(i)

# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i in squares:
    print(i)

# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is 
# less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

""" PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
score = PlayListRatings[0]

while (score > 6):
    print (score)
    i = i + 1
    score = PlayListRatings[i]

print ("The score is less 6")
"""""


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print ("longiud", len(PlayListRatings))
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1


# Write a while loop to copy the strings 
# 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while (i < len(squares) and squares[i] == 'orange'):
    # print(squares[i])
    new_squares.append(squares[i])
    i = i +1 
print (new_squares)



"""for i in range(0,5):
    print (squares[i])
    squares[i] = 'orange'"""

