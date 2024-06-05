from data import Data
from praktikum.bun import Bun


class TestBun:
    def test_new_bun_has_correct_name(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_name() == Data.BUN_NAME

    def test_new_bun_has_correct_price(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_price() == Data.BUN_PRICE

    def test_one_bun_get_name_successful(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_name() == Data.BUN_NAME

    def test_one_bun_get_price_successful(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_price() == Data.BUN_PRICE
