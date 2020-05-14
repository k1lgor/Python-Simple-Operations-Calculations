#1 liter = 1 cub decimeter
l = int(input())
b = int(input())
h = int(input())
percent_volume = float(input())
v = l * b * h #cc
cc = 1 / 1000 #l
ttl_liters = v * cc
percent = percent_volume / 100
liters = ttl_liters * (1 - percent)
print(f'{liters:.3f}')