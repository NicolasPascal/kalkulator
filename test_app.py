# test_app.py

import pytest
from app import tambah, kurang, kali, bagi

def test_tambah():
    assert tambah(3, 2) == 5

def test_kurang():
    assert kurang(5, 2) == 3

def test_kali():
    assert kali(4, 3) == 12

def test_bagi():
    assert bagi(10, 2) == 5

def test_bagi_dengan_nol():
    with pytest.raises(ValueError):
        bagi(10, 0)
