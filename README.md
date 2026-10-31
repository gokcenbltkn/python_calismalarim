# python_calismalari
# Hafta 4 Lab Çalışması - Rota ve Performans Raporu

## Görev 4: Önbellekli Rota Sayacı Performans Karşılaştırması

`adim = 20` için yapılan test ölçüm sonuçları:

- **Önbelleksiz (Klasik Özyinelemeli) Süre:** ~1.452031 saniye
- **Önbellekli (`@lru_cache`) Süre:** ~0.000048 saniye

### Cache Bilgisi Output (`cache_info()`):
`CacheInfo(hits=18, misses=21, maxsize=128, currsize=21)`

**Açıklama:**
`@lru_cache` kullanımı sayesinde daha önce hesaplanan alt rota sayıları önbellekten çekildiği için `adim=20` derinliğindeki hesaplama süresi neredeyse anlık (milisaniyeler seviyesinde) bir hıza ulaşmıştır.
