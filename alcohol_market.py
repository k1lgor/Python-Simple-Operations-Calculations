wisky_cena = float(input())
ml_bira = float(input())
ml_wino = float(input())
ml_rakiq = float(input())
ml_wisky = float(input())
rakiq_cena = wisky_cena / 2
wino_cena = rakiq_cena - rakiq_cena * 0.4
bira_cena = rakiq_cena - rakiq_cena * 0.8
wisky = wisky_cena * ml_wisky
bira = bira_cena * ml_bira
rakiq = rakiq_cena * ml_rakiq
wino = wino_cena * ml_wino
ttl = wisky + bira + rakiq + wino
print(f'{ttl:.2f}')