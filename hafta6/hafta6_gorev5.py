# Ad-Soyad:Elif Gökçen Beltekin
# Numara:20253005007
# Tarih:31/10/2026
# Görev5

kelime = "KOŞUL"
tahminler = ""      # denenen harfler karakter dizisinde birikir
hata = 0
MAKS_HATA = 6
 
while hata < MAKS_HATA:
    # kelimenin görünümünü oluştur
    gorunum = ""
    eksik = 0
    for h in kelime:
        if h in tahminler:
            gorunum += h + " "
        else:
            gorunum += "_ "
            eksik += 1
    print(f"{gorunum.strip()} (hata: {hata}/{MAKS_HATA})", end=" ")
#  Her turda for h in kelime ile kelimeyi baştan dolaşıyoruz. Harf tahminlerde varsa gösteriyoruz,
#  yoksa _. eksik sayacı kaç harf eksik olduğunu tutar. eksik == 0 ise kelime tamamlanmıştır.
    if eksik == 0:
        print("Kazandınız!")
        break
    # break: Kazanınca döngüden hemen çıkar.
    print()
    giris = input("Harf: ").strip()
    if len(giris) != 1 or not giris.isalpha():
        print("Uyarı: Lütfen tek bir harf girin.")
        continue
    # continue: Geçersiz girişte (tek harf değil) ya da tekrar eden harfte turun geri kalanını atlayıp başa döner. Bu durumlarda hata sayılmaz.
 
    # Türkçe büyütme: i -> İ, ı -> I ("i".upper() "I" verir!)
    if giris == "i":
        harf = "İ"
    elif giris == "ı":
        harf = "I"
    else:
        harf = giris.upper()
 
    if harf in tahminler:
        print("Bu harfi zaten denediniz.")
        continue
 
    tahminler += harf
    if harf not in kelime:
        hata += 1
else:
    # break ile çıkılmadıysa (6 hata doldu)
    print(f"Kaybettiniz! Kelime: {kelime}")
    # while … else: Döngü break ile bitmezse, yani 6 hata dolduğu için normal şekilde biterse else çalışır ve “Kaybettiniz” yazılır. 
    # Kazanınca break olduğu için else atlanır.