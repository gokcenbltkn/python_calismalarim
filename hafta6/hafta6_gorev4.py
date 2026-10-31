# Ad-Soyad:Elif Gökçen Beltekin
# Numara:20253005007
# Tarih:31/10/2026
# Görev4

# (a) Tek sayı için analiz
while True:
    try:
        n = int(input("n: "))
        if n < 1:
            print("Uyarı: n pozitif bir tam sayı olmalı.")
            continue
        break
    except ValueError:
        print("Uyarı: Lütfen tam sayı girin.")
 
sayi = n
adim = 0
en_yuksek = n
while sayi != 1:
#  while sayi != 1: 1'e ulaşana kadar devam. Her turda adim bir artar, en_yuksek ise yeni değer daha büyükse güncellenir.
    sayi = sayi // 2 if sayi % 2 == 0 else 3 * sayi + 1   # kural tek satırda
    adim += 1
    if sayi > en_yuksek:
        en_yuksek = sayi
print(f"{n} → 1: {adim} adım, en yüksek değer {en_yuksek}")
#(b) kısmında dış for her başlangıç sayısını dener, iç while o sayının zincirini hesaplar. Bu iç içe döngüdür.
#(b) 1'den sınıra kadar en uzun zincir (iç içe döngü) 
while True:
    try:
        sinir = int(input("Üst sınır: "))
        if sinir < 1:
            print("Uyarı: Sınır pozitif olmalı.")
            continue
        break
    except ValueError:
        print("Uyarı: Lütfen tam sayı girin.")
 
en_uzun_baslangic = 1
en_uzun_adim = 0
for baslangic in range(1, sinir + 1):
    sayi = baslangic
    adim = 0
    while sayi != 1:
        sayi = sayi // 2 if sayi % 2 == 0 else 3 * sayi + 1
        adim += 1
    if adim > en_uzun_adim:
        en_uzun_adim = adim
        en_uzun_baslangic = baslangic
print(f"1–{sinir} arasında en uzun zincir: {en_uzun_baslangic} ({en_uzun_adim} adım)") 