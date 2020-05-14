number = float(input())
cubmeter = 7.61
discount = 0.18
sum1 = number * cubmeter * discount
sum2 = number * cubmeter - sum1
print(f'The final price is: {sum2:.2f} lv.')
print(f'The discount is: {sum1:.2f} lv.')