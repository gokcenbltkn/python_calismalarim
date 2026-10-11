# Kapsam ve Tuzak Notları

## 1. Varsayılan Parametre Tuzağı
Fonksiyona varsayılan olarak boş liste (`depo=[]`) verdiğimizde, bu liste her çağrıda sıfırlanmıyor ve hafızada kalmaya devam ediyor. Bu yüzden ikinci çağrıda eski veriler de listede kalıyor. Bunu düzeltmek için parametreyi `None` yapıp fonksiyon içinde `if depo is None: depo = []` kontrolü ekledik. Böylece her çağrıda yeni liste oluşturuluyor.

## 2. UnboundLocalError Nedir?
Bir fonksiyonun içinde global bir değişkene değer atamaya kalktığımızda Python o değişkeni yerel kabul ediyor. Eğer değişkene henüz değer atamadan önce okumaya çalışırsak `UnboundLocalError` hatası alıyoruz. Bu labda `global` anahtar kelimesi yasak olduğu için bu tür durumlarda değişkenleri parametre olarak göndermek gerekiyor.