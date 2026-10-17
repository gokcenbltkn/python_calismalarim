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
    # Yakıt sıfıra ulaşıp bitince de oyunu kaybetme mesajını bastırıp döngüyü break ile bitirdim."
    
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