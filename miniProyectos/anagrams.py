"""
Group Anagrams using Python
Grouping anagrams is one of the popular questions in coding interviews. 
Here you will be given a list of words, and you have to write an algorithm to
group all the words which are anagrams of each other. 
So below is how you can write a Python function to group anagrams:
"""

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    print(dfdict)

    for i in a:
        sorted_i = " ".join(sorted(i))
        print(sorted_i)
        dfdict[sorted_i].append(i)
        print(dfdict)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))


def is_anagram(word1, word2):

    is_anagram = sorted(word1.lower()) == sorted(word2.lower())
    print(sorted(word1))
    if is_anagram:    
        return True
    else:
        return False

word1 = "listen"
word2 = "silenta"
is_anagram(word1, word2)
print(is_anagram(word1, word2))