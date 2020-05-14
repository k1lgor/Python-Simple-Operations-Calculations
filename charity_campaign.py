days = int(input())
pastry_cook = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
cake_prize = 45
waffle_prize = 5.8
pancake_prize = 3.2
sum_cakes_per_day = cakes * cake_prize
sum_waffles_per_day = waffles * waffle_prize
sum_pancakes_per_day = pancakes * pancake_prize
ttl_per_day = (sum_cakes_per_day + sum_waffles_per_day + sum_pancakes_per_day) * pastry_cook
ttl_for_campaign = ttl_per_day * days
grand_total = ttl_for_campaign - (ttl_for_campaign / 8)
print(f'{grand_total:.2f}')
