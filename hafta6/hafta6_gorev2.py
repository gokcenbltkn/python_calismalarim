# Ad-Soyad:Elif Gökçen Beltekin
# Numara:20253005007
# Tarih:31/10/2026
# Görev2
cumle = input("Cümle: ")
 
harf = sesli = sessiz = rakam = kelime = 0
kelime_icinde = False      # bayrak: şu an bir kelimenin içinde miyiz?
temiz = ""                 # yalnızca küçük harfler (palindrom kontrolü için)
 
# Türkçe büyük/küçük harf sorunu olduğu için sesli kümesi büyük harfleri de içerir
SESLILER = "aeıioöuüAEIİOÖUÜ"
 
#Bayrak (kelime_icinde): Kelime sayımının püf noktası. Boşluk görünce bayrak False olur. Boşluk olmayan bir karaktere gelince bayrak False ise yeni bir kelime başlamıştır, kelime += 1 yapıp bayrağı True yaparız. 
#Böylece aynı kelimenin her harfinde tekrar saymayız.
for karakter in cumle:
    # kelime sayımı (bayrak)
    if karakter == " ":
        kelime_icinde = False
    elif not kelime_icinde:
        kelime += 1
        kelime_icinde = True
#karakter.isalpha() harf, isdigit() rakam mı diye bakar.
    if karakter.isalpha():
        harf += 1
        if karakter in SESLILER:
            sesli += 1
        else:
            sessiz += 1
        # Türkçe'ye uygun küçültme: İ -> i, I -> ı
        if karakter == "İ":
            temiz += "i"
        elif karakter == "I":
            temiz += "ı"
        else:
            temiz += karakter.lower()
    elif karakter.isdigit():
        rakam += 1
#  temiz: Sadece harfleri küçültüp birleştirdiğimiz yeni bir metin
# cumle[::-1]: Dilimleme ile metni tersine çevirir.
# temiz == temiz[::-1]: Düz ve ters hâli aynıysa palindromdur.
print(f"Harf: {harf} Sesli: {sesli} Sessiz: {sessiz} Rakam: {rakam} Kelime: {kelime}")
 
# Ters yazdırma (dilimleme ile)
ters = cumle[::-1]
print(f"Ters: {ters}")
 
if temiz == temiz[::-1]:
    print("Palindrom")
else:
    print("Palindrom değil") 
