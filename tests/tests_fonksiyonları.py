import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from uzay_oyunu import envanter_metni, hedef_menusu

def test_envanter_metni():
  # Eşyalar varken doğru metni döndürmeli
  assert (
      envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
  )
  # Hiç eşya yokken boş metin (None veya boş string) döndürmeli
  assert envanter_metni(False, False, False) in ("", None)


def test_hedef_menusu():
  beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
  assert hedef_menusu(["centauri", "sirius"]) == beklenen
  