
# ['A','B','C','A','B','C']

set1 = {'A','B','C','A','B','C'}

set(['A','B','C','A','B','C'])
print (set1)
print (set)

# Add the string 'D' to the set S. S={'A','B','C'}

S={'A','B','C'}
S.add('D')

print(S)

# Find the intersection of set A and B.
A={1,2,3,4,5}
B={1,3,9, 12}

C = A & B
# OR 
print ( A.intersection(B))
  
print(C)


S={'A','B','C'}
U={'A','Z','C'}

#
print( U.union(S) )
#print( S.union(U) )

# A set is a unique collection of objects in Python.
#  You can denote a set with a pair of curly brackets {}. Python will automatically remove duplicate items:

set2 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set2)

# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A.add("NSYNC")
print(A)

A.remove("NSYNC")

print("AC/DC" in A)

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Find the intersections

intersection = album_set1 & album_set2
print (intersection)

# Find the difference in set1 but not set2

print (album_set1.difference(album_set2))

# The elements in album_set2 but not in album_set1 is given by:
print (album_set2.difference(album_set1))

# Find the union of two sets

print ( album_set1.union(album_set2) )

# Check if superset
# And you can check if a set is a superset or subset of another set, respectively, like this:
print (set(album_set1).issuperset(album_set2) )
print (set(album_set2).issubset(album_set1) )

# Here is an example where issubset() and issuperset() return true:

set({"Back in Black", "AC/DC"}).issubset(album_set1) 
album_set1.issuperset({"Back in Black", "AC/DC"})   



# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

print (sum(A))
print (sum(B))

print (sum(A) == sum(B))

# Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


album_set3 = album_set1.union(album_set2)
print (album_set3)


print (album_set1.issubset(album_set3))
