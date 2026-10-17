def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
  """Envanterdeki duruma göre sahip olunan öğelerin metnini döndürür."""
  oge_listesi = []
  if credits:
    oge_listesi.append("bol kredi")
  if engines:
    oge_listesi.append("güçlü motor")
  if copilot:
    oge_listesi.append("yetenekli bir pilot")

  if not oge_listesi:
    return ""
  return "Sende: " + ", ".join(oge_listesi)


def hedef_menusu(hedefler: list[str]) -> str:
  """Verilen hedef liste elemanlarını numaralandırarak menü metni oluşturur."""
  menu = ["Nereye gitmek istersin?"]
  for i, hedef in enumerate(hedefler, 1):
    menu.append(f"[{i}] {hedef}")
  return "\n".join(menu)

# Denemek için
print(envanter_metni(True, False, True))

print(hedef_menusu(["Gezegen 1", "Uzay İstasyonu", "Kara Delik"]))
