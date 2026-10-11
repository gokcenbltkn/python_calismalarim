# GÖREV 5: Closure ve lambda

def hamle_sayaci():
    # Her çağrıldığında hamle sayısını bir artırır
    sayac = 0
    
    def artir():
        nonlocal sayac
        sayac += 1
        return sayac
        
    return artir

def en_bagli_gezegenler(galaksi):
    # Gezegenleri bağlantı sayısına ve alfabetik sıraya göre sıralar
    baglantilar = galaksi.get("baglantilar", {})
    
    sirali_liste = sorted(
        baglantilar.keys(),
        key=lambda g: (-len(baglantilar[g]), g)
    )
    return sirali_liste

