green = 3.4
red = 4.3
x = float(input())
y = float(input())
h = float(input())
#walls
walls = 2 * pow(x, 2)
door = 1.2 * 2
#sides
sides = 2 * (x * y)
windows = 2 * pow(1.5, 2)
#roof
roof1 = 2 * (x * y)
roof2 = 2 * (x * h / 2)
sum_walls = walls - door + sides - windows
sum_roof = roof1 + roof2
green1 = sum_walls / green
red1 = sum_roof / red
print(f'{green1:.2f}')
print(f'{red1:.2f}')