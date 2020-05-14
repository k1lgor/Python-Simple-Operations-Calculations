l = float(input())
w = float(input())
a = float(input())
hall = (l * 100) * (w * 100)
wardrobe = pow((a * 100), 2)
bench = hall / 10
free_space = hall - wardrobe - bench
dancer = free_space / (40 + 7000)
from math import floor
print(floor(dancer))