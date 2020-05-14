one_space1 = 70
one_space2 = 120
corridor = 100
w = float(input())
h = float(input())
W = w * 100
H = h * 100
from math import floor
a = floor(W / one_space2)
b = floor((H - corridor) / one_space1)
sum = a * b - 3
print(sum)
