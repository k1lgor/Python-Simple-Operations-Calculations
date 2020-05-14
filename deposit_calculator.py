deposit = float(input())
term = int(input())
percent = float(input())
sum1 = deposit * (percent / 100)
sum2 = sum1 / 12
sum3 = deposit + (term * sum2)
print(sum3)