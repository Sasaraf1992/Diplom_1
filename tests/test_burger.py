from data import Data
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.bun import Bun
from unittest.mock import Mock, patch


class TestBurger:
    def test_set_buns_successful(self):
        mock_bun = Mock()
        mock_bun.bun = Bun(Data.MOCK_BUN_NAME, Data.MOCK_BUN_PRICE)
        new_burger = Burger()

        new_burger.set_buns(mock_bun.bun)

        assert new_burger.bun.get_name() == Data.MOCK_BUN_NAME

    def test_add_one_ingredient_in_burger_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient(Data.MOCK_INGREDIENT_TYPE, Data.MOCK_INGREDIENT_NAME,
                                                 Data.MOCK_INGREDIENT_PRICE)
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient.ingredients)
        assert len(new_burger.ingredients) == 1

    def test_one_ingredient_remove_from_burger(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients_1 = Ingredient(Data.MOCK_INGREDIENT_TYPE, Data.MOCK_INGREDIENT_NAME,
                                                   Data.MOCK_INGREDIENT_PRICE)
        mock_ingredient.ingredients_2 = Ingredient(Data.INGREDIENT_TYPE, Data.MOCK_INGREDIENT_NAME,
                                                   Data.MOCK_INGREDIENT_PRICE)
        new_burger = Burger()

        new_burger.add_ingredient(mock_ingredient.ingredients_2)
        new_burger.add_ingredient(mock_ingredient.ingredients_1)
        new_burger.move_ingredient(0, 1)
        assert new_burger.ingredients.index(mock_ingredient.ingredients_1) == 0

    def test_get_one_burger_price(self):
        mock_bun = Mock()
        mock_bun.bun = Bun(Data.MOCK_BUN_NAME, Data.MOCK_BUN_PRICE)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient(Data.MOCK_INGREDIENT_TYPE, Data.MOCK_INGREDIENT_NAME,
                                                 Data.MOCK_INGREDIENT_PRICE)
        new_burger = Burger()
        new_burger.set_buns(mock_bun.bun)
        new_burger.add_ingredient(mock_ingredient.ingredients)
        assert new_burger.get_price() == 2964

    @patch('praktikum.bun.Bun.get_name', return_value=Data.MOCK_BUN_NAME)
    @patch('praktikum.ingredient.Ingredient.get_name', return_value=Data.MOCK_INGREDIENT_NAME)
    @patch('praktikum.ingredient.Ingredient.get_type', return_value=Data.MOCK_INGREDIENT_TYPE)
    def test_get_receipt_for_one_burger(self, mock_bun_get_name, mock_ingredient_get_name, mock_ingredient_get_type):
        mock_bun = Mock()
        mock_bun.bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME,
                                                 Data.INGREDIENT_PRICE)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)

        assert burger.get_receipt() == '(==== Флюоресцентная булка R2-D3 ====)\n''= filling' \
                                       ' Филе Люминесцентного тетраодонтимформа =\n' \
                                       '(==== Флюоресцентная булка R2-D3 ====)\n''\n''Price: 2598'
