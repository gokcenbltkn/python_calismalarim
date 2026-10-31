# Görev 1:
import itertools
from typing import Generator

def fibonacci() -> Generator[int, None, None]:
# Sonsuz Fibonacci serisi üreten üreteç (generator) fonksiyonu.
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        # Normal bir fonksiyonda return deyine tek bir değer veya liste döndürür.Bu sebepten sonsuz dizi için ve belleği patlatmamak için yield kullandık.

# 1. next() ile ilk 3 değer:
g = fibonacci()
print(next(g), next(g), next(g))


# 2. itertools.islice ile ilk 12 değer:
print(list(itertools.islice(fibonacci(), 12)))


# 3. itertools.takewhile ile 100'den küçük değerler:
print(list(itertools.takewhile(lambda x: x < 100, fibonacci())))
    
# Tek kullanımlık
def test_fibonacci_tek_kullanimlik():
    # Aynı üreteç nesnesini iki kez tükettiğimizde ikinci çağrı farklı sonuç vermelidir
    g = fibonacci()

    ilk_5 = list(itertools.islice(g, 5))  # [0, 1, 1, 2, 3]
    ikinci_5 = list(itertools.islice(g, 5))  # [5, 8, 13, 21, 34]

    # Üreteç sıfırlanmadığı ve kaldığı yerden devam ettiği için sonuçlar eşit olamaz!
    assert ilk_5 != ikinci_5

# Görev 2:
from typing import Generator

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:

  kalan_yakit = yakit
  while kalan_yakit > 0:
    kalan_yakit -= tuketim
    if kalan_yakit < 0:
      kalan_yakit = 0
    yield kalan_yakit
# Fonksiyon her next() çağrıldığında while döngüsünün kaldığı yerden devam eder ve o anki kalan yakıt miktarını yield ile dışarıya verir.
def oyun_seyahati():
  """Oyuncunun galatada yakıt göstergesiyle seyahat etmesini simüle eder."""
  # Başlangıç yakıtı 100, her hamledeki tüketim 5
 
  gosterge = yakit_gostergesi(100, 5)

  print("Uzay yolculuğu başladı!")

  while True:
    input("İlerlemek için Enter'a bas...")
    try:
      kalan = next(gosterge)
      print(f"Yolculuk yapıldı. Kalan yakıt: {kalan}")
    except StopIteration:
      print("Yakıtın bitti, uzayda sürükleniyorsun...")
      break
    # Yakıt göstergesi bir üreteç olduğu için her adımda next() ile sıradaki değeri çekmem gerekiyordu. StopIteration hatası Python'da üreteç bittiğinde kendiliğinden fırlatıldığı için, bunu try-except bloğuyla yakaladım. 
    # Yakıt sıfıra ulaşıp bitince de oyunu kaybetme mesajını bastırıp döngüyü break ile bitirdim.
    
  # Görev 3:
  def satirlari_oku(dosya_yolu):
   with open(dosya_yolu, "r", encoding="utf-8") as dosya:
    for satir in dosya:
      temiz = satir.strip()
      if temiz and not temiz.startswith("#"):
        yield temiz

def ayristir(satirlar):
 
  for satir in satirlar:
    parcalar = satir.split()
    kaynak = parcalar[0]
    hedef = parcalar[2]
    yakit = int(parcalar[3])
    yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar, sinir_deger):

  for kaynak, hedef, yakit in kayitlar:
    if yakit > sinir_deger:
      yield hedef 
  # Bu görevde veriyi belleği yormadan işlemek için üreteç (yield) mantığını kullandım.
  # İlk fonksiyon olan satirlari_oku dosyayı açarak strip() ile gereksiz boşlukları, startswith('#') ile de yorum satırlarını temizliyor.
  # Ardından ayristir fonksiyonu bu satırları split() ile parçalara ayırarak kaynak, hedef ve yakıt bilgilerini birer demet (tuple) haline getiriyor. Son olarak uzun_yolculuklar bu verileri süzerek eşik değerini geçen hedefleri döndürüyor. 
  # Bu fonksiyonlar birbirinin çıktısını girdi olarak aldığı için tıpkı bir boru hattı gibi bellekte yer kaplamadan sırayla çalışıyor.

  # Görev 4:
  from functools import lru_cache

from functools import lru_cache
import time

def rota_sayaci(baglantilar):

    @lru_cache(maxsize=128)
    def rota_sayisi(gezegen, adim):
        if adim == 0:
            return 1

        toplam = 0

        for hedef in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(hedef, adim - 1)

        return toplam

    return rota_sayisi
say = rota_sayaci(galaksi["baglantilar"])

print(say("dünya", 3))
print(say("dünya", 10))
print(say("dünya", 40))
# Sözlükler (dict) değiştirilebilir (unhashable) olduğu için doğrudan @lru_cache ile dekore edilemiyor. 
# Bu yüzden dışarıya rota_sayaci adında bir ana fonksiyon yazdım, içine de @lru_cache ile önbelleklenen özyinelemeli (recursive) rota_sayisi fonksiyonunu koydum. 
# Bu sayede aynı gezegen ve adım kombinasyonları tekrar hesaplanmadan bellekten hızlıca çekiliyor.

# Görev 5:
from functools import reduce, partial

# 1. Gezegen adlarının büyük harfli listesi (map ve liste üreteci ile)
gezegenler = ["dünya", "centauri", "sirius", "orion", "kara_delik"]

# map yöntemi
buyuk_map = list(map(lambda x: x.upper(), gezegenler))
# liste üreteci yöntemi
buyuk_lc = [g.upper() for g in gezegenler]

# Gezegen isimlerini büyük harfe çevirirken map ve upper() kullandım, alternatif olarak liste üreteci ile tek satırda yaptım.
# 2. En az iki bağlantısı olan gezegenler
baglantilar = {
    "dünya": ["sirius", "orion"],
    "centauri": ["orion"],
    "sirius": ["orion", "kara_delik"],
    "orion": ["centauri", "sirius"],
    "kara_delik": [],
}
# En az iki bağlantısı olanları bulurken filter ile koşul verdim.

# filter yöntemi
ikiden_fazla_filter = list(
    filter(lambda g: len(baglantilar.get(g, [])) >= 2, gezegenler)
)
# liste üreteci yöntemi
ikiden_fazla_lc = [
    g for g in gezegenler if len(baglantilar.get(g, [])) >= 2
]

# reduce yöntemi
toplam_reduce = reduce(
    lambda toplam, g: toplam + len(baglantilar.get(g, [])), gezegenler, 0
)
# Toplam bağlantı sayısını bulurken reduce ile biriktirerek toplama yaptım.
toplam_lc = sum(len(b) for b in baglantilar.values())

def yolculuk(mesafe, hiz):
  return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)

# Bence liste üreteci (list comprehension) yapısı düz bir cümle gibi okunduğu için lambda ve 
# map/filter kombinasyonuna göre insan gözüyle çok daha kolay okunur ve anlaşılırdır.