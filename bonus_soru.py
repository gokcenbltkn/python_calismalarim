import time

# BONUS: Çalışma süresini ölçen dekoratör (sure_olc)
def sure_olc(fonksiyon):
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        gecen_sure = bitis - baslangic
        print(f"İşlem süresi: {gecen_sure:.4f} saniye")
        return sonuc
    return sarmalayici
# Test etmek için:
# en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)