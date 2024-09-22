# The distance between two letters in the English alphabet is one more than the number of letters between them. Alternatively, it can be defined as the number of steps needed to move from the alphabetically smaller letter to the larger letter. This is always a non-negative integer. For example:
"""
Letter-1	Letter-2	Letter-Distance
a	a	0
a	c	2
a	z	25
z	a	25
e	a	4
The distance between two words is defined as follows:

It is -1, if the words are of unequal lengths.
If the word-lengths are equal, it is the sum of the distances between letters at corresponding positions in the words. For example:
�
word
(
dog
,
cat
)
=
�
letter
(
d
,
c
)
+
�
letter
(
o
,
a
)
+
�
letter
(
g
,
t
)
=
1
+
14
+
13
=
28
d 
word
​
 (dog,cat)=d 
letter
​
 (d,c)+d 
letter
​
 (o,a)+d 
letter
​
 (g,t)=1+14+13=28
Write a function named distance that accepts two words as arguments and returns the distance between them.

You do not have to accept input from the user or print output to the console. You just have to write the function definition.""
"""


def distance(word1, word2):
    if len(word1) == len(word2):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        totaldist = 0
        for i in range(len(word1)):
            dist = abs(int(alpha.index(word1[i]))-int(alpha.index(word2[i])))
            totaldist += dist
        return totaldist
    else:
        return -1
