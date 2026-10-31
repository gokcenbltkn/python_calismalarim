# Ad-Soyad:Elif Gökçen Beltekin
# Numara:20253005007
# Tarih:31/10/2026
# Bonus
govde = "453914880343646"
for kontrol in range(10):
    tam = govde + str(kontrol)
    toplam = 0
    sira = 0                      # sağdan sayım; kontrol hanesi sira=0
    for karakter in tam[::-1]:
        d = int(karakter)
        if sira % 2 == 1:         # sağdan her ikinci hane iki katına çıkar
            d *= 2
            if d > 9:
                d -= 9
        toplam += d
        sira += 1
    if toplam % 10 == 0:
        print(f"Kontrol hanesi: {kontrol}")
        break 