a = float(input())
if 26 <= a <= 35:
    print("Hot")
elif 20.1 <= a <= 25.9:
    print("Warm")
elif 15 <= a <= 20:
    print("Mild")
elif 12 <= a <= 14.9:
    print("Cool")
elif 5 <= a <= 11.9:
    print("Cold")
else:
    print("unknown")
