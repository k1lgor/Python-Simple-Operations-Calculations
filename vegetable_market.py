vegkg = float(input())
frutkg = float(input())
ttlvegkg = int(input())
ttlfrutkg = int(input())
euro = 1.94
ttl1 = vegkg * ttlvegkg
ttl2 = frutkg * ttlfrutkg
ttl3 = ttl1 + ttl2
ttl4 = ttl3 / euro
print(f'{ttl4:.2f}')