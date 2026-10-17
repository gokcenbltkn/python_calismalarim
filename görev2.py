# Görev 2:
from typing import Generator

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:

    kalan_yakit = yakit
    while kalan_yakit > 0:
        kalan_yakit -= tuketim
        if kalan_yakit < 0:
            kalan_yakit = 0
        yield kalan_yakit