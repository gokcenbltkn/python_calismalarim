from uzay_oyunu.oyun import yakit_ekle


def test_yakit_ekle():
  # İlk çağrı
  sonuc1 = yakit_ekle(10)
  assert sonuc1 == [10]

  # İkinci çağrıda liste sıfırdan başlamalı, [10, 20] olmamalı
  sonuc2 = yakit_ekle(20)
  assert sonuc2 == [20] 