tables = int(input())
l = float(input())
w = float(input())
usd = 1.85
meter_rec = 7
meter_kare = 9
sum1 = tables * (l + 2 * 0.3) * (w + 2 * 0.3)
sum2 = tables * (l / 2) * (l / 2)
sumUSD = sum1 * meter_rec + sum2 * meter_kare
sumBGN = sumUSD * 1.85
print(f'{sumUSD:.2f} USD')
print(f'{sumBGN:.2f} BGN')