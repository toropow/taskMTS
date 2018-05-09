import Check
import pytest
import allure


class TestCheckInit:

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with empty input")
    def test_empty(self):
        result = Check.check_ident("")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output without param")
    def test_without_param(self):
        with pytest.raises(TypeError):
            Check.check_ident()

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with less count number")
    def test_less_values(self):
        result = Check.check_ident("123 1")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with large count number")
    def test_large_values(self):
        resut = Check.check_ident("1231231231231233123 1")
        assert resut == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output without hyphen")
    def test_without_hyphen(self):
        result = Check.check_ident("9876543219 9")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with fractional number")
    def test_with_fractional_number(self):
        result = Check.check_ident("987.16543219 9")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with two param")
    def test_two_arg_in_func(self):
        with pytest.raises(TypeError):
            Check.check_ident("9876543219 9","9876543219 9")

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with list instead string")
    def test_not_string_in_arg_func(self):
        with pytest.raises(TypeError):
            Check.check_ident(list("9876543219 9"))

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with param as self 'check_init' function")
    def test_self(self):
        with pytest.raises(TypeError):
            Check.check_ident(Check.check_ident("98765-43219 9"))

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with boolean as param")
    def test_bool(self):
        with pytest.raises(TypeError):
            Check.check_ident(False)

    @allure.feature("Incorrect input")
    @allure.story("Checking the output without space between number and summ")
    def test_without_space(self):
        resut = Check.check_ident("98765-432199")
        assert resut == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with extra space right")
    def test_with_space_end(self):
        result = Check.check_ident("98765-43219 9 ")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with extra space left")
    def test_with_space_first(self):
        resut = Check.check_ident(" 98765-43219 9")
        assert resut == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with double space between number and summ")
    def test_with_double_space(self):
        result = Check.check_ident("98765-43219  9")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with negative number")
    def test_with_negative_number(self):
        result = Check.check_ident("98765-4321-9 9")
        assert result == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with letter within the number")
    def test_with_letter(self):
        resut = Check.check_ident("987a5-43219 9")
        assert resut == False

    @allure.feature("Incorrect input")
    @allure.story("Checking the output with letter within the symbol")
    def test_with_symbol(self):
        result = Check.check_ident("9@765-43219 -9")
        assert result == False

    @allure.feature("Correct input")
    @allure.story("Checking the output with check sum less 10")
    def test_positive_check_sum_less_10(self):
        resut = Check.check_ident("98765-43219 9")
        assert resut == True

    @allure.feature("Correct input")
    @allure.story("Checking the output with check sum more 10")
    def test_positive_check_sum_more_10(self):
        result = Check.check_ident("12345-76621 3")
        assert result == True

    @allure.feature("Correct input")
    @allure.story("Checking the output with a number consisting of 1")
    def test_positive_check_only_zerro(self):
        result = Check.check_ident("00000-00000 0")
        assert result == True

    @allure.feature("Correct input")
    @allure.story("Checking the output with a number consisting of 0")
    def test_positive_check_only_one(self):
        result = Check.check_ident("11111-11111 9")
        assert result == True