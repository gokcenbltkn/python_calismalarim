# Ad-Soyad:Elif Gökçen Beltekin
# Numara:20253005007
# Tarih:31/10/2026
# Görev3

numara = input("T.C. kimlik no: ").strip()
#  len(numara) != 11, isdigit(), numara[0] == "0": Üç biçim kontrolü. Biri başarısızsa hesaba girmeden “GEÇERSİZ” yazılır.
# DOĞRULA: biçim
if len(numara) != 11:
    print(f"T.C. kimlik no: {numara} → GEÇERSİZ (11 karakter olmalı)")
elif not numara.isdigit():
    print(f"T.C. kimlik no: {numara} → GEÇERSİZ (yalnızca rakam olmalı)")
elif numara[0] == "0":
    print(f"T.C. kimlik no: {numara} → GEÇERSİZ (ilk hane 0 olamaz)")
else:
    # İŞLE: 1,3,5,7,9. haneler (indeks 0,2,4,6,8) = tek; 2,4,6,8. haneler = çift
    tek = 0
    cift = 0
    for i in range(9):
        if i % 2 == 0:
            tek += int(numara[i])
        else:
            cift += int(numara[i])
 
    h10 = (7 * tek - cift) % 10
    h11 = (tek + cift + h10) % 10
 
    sonuc = "GEÇERLİ" if h10 == int(numara[9]) and h11 == int(numara[10]) else "GEÇERSİZ"
    print(f"Tek: {tek} Çift: {cift} 10. hane: {h10} 11. hane: {h11} → {sonuc}")
 