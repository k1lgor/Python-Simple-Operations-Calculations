strawberries = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries2 = float(input())
raspberries_prize = strawberries / 2
oranges_prize = raspberries_prize - (0.4 * raspberries_prize)
bananas_prize = raspberries_prize - (0.8 * raspberries_prize)
sum_raspberries = raspberries_prize * raspberries
sum_oranges = oranges_prize * oranges
sum_bananas = bananas_prize * bananas
sum_strawberries = strawberries2 * strawberries
ttl_sum = sum_raspberries + sum_oranges + sum_bananas + sum_strawberries
print(ttl_sum)