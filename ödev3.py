from uzay_oyunu.oyun import envanter_metni, hedef_menusu

def test_envanter_metni():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(False, False, False) == ""

def test_hedef_menusu(capsys):
    hedef_menusu(["centauri", "sirius"])
    captured = capsys.readouterr()
    expected = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius\n"
    assert captured.out == expected s