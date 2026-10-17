def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler) -> str:
    """Görev kaydını başlık, adımlar, öncelik ve ek bilgilerle formatlayıp döndürür."""
    kayit_metni = f"[{oncelik.upper()}] {baslik}\n"
    
    for i, adim in enumerate(adimlar, 1):
        kayit_metni += f"{i}. {adim}\n"
        
    for anahtar, deger in ekler.items():
        kayit_metni += f"{anahtar}: {deger}"
        
    return kayit_metni.strip()

if __name__ == "__main__":
    # Test verileri
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}

    # Listeyi (*) ve sözlüğü (**) argümanlara açarak çağırma
    cikti = gorev_kaydi(
        "Kara deliğe atla",
        *adimlar_listesi,
        oncelik="yüksek",
        **ek_bilgiler
    )
    
    print(cikti)