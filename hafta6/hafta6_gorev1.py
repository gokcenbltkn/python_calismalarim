# Ad-Soyad:Elif Gökçen Beltekin
# Numara:20253005007
# Tarih:31/10/2026
# Görev1
import math
 
while True: 
    # while döngüsünde eğer geçersiz bir şey girilirse program çökmez,tekrar sorar.
    try:
        x = float(input("a: "))
        y = float(input("b: "))
        z = float(input("c: "))
    # float kullanırken harf girilirse hata verir ve except bunu yakalar
    except ValueError:
        print("Uyarı: Lütfen sayı girin.")
        continue
    if x <= 0 or y <= 0 or z <= 0:
        print("Uyarı: Kenarlar pozitif olmalı.")
        continue
    # en uzun kenarı a, diğerlerini b ve c yaptım (liste kullanmadıgımız için max,min kullanırız)
    a = max(x, y, z)
    c = min(x, y, z)
    b = x + y + z - a - c
    if a >= b + c:
        print("Uyarı: Üçgen eşitsizliği sağlanmıyor.")
        continue
    break
 
if math.isclose(a, b) and math.isclose(b, c):
# math.isclose ondalık sayılarda == risk olabilir bu yuzden isclose kullanmak daha dogru olur
    kenar_turu = "Eşkenar"
elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
    kenar_turu = "İkizkenar"
else:
    kenar_turu = "Çeşitkenar"
 
cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
cos_a = max(-1.0, min(1.0, cos_a))      # kayan nokta hatasına karşı sınırla
aci = math.degrees(math.acos(cos_a))  
# math.degress acıyı radyana cevirir,math.acoss dereceye çevirir
 
if math.isclose(aci, 90):               # == yerine isclose
    aci_turu = "Dik"
elif aci < 90:
    aci_turu = "Dar"
else:
    aci_turu = "Geniş"
 
cevre = a + b + c
u = cevre / 2
alan = math.sqrt(u * (u - a) * (u - b) * (u - c))   
 

print(f"Tür: {kenar_turu}, {aci_turu} açılı")
print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {aci:.2f}°")