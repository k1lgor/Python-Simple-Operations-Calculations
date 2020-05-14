cena_Skum = float(input())
cena_caca = float(input())
kgPala = float(input())
kgSaf = float(input())
kgMidi = float(input())
cena_pala = cena_Skum + cena_Skum * 0.6
cena_saf = cena_caca + cena_caca * 0.8
cena_midi = 7.5
pala = cena_pala * kgPala
saf = cena_saf * kgSaf
midi = cena_midi * kgMidi
sum = pala + saf + midi
print(f'{sum:.2f}')