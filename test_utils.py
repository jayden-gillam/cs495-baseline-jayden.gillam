from utils import caesar_cipher


def test_basic_shift():
    assert caesar_cipher("hello", 3) == "khoor"


def test_wrapping():
    assert caesar_cipher("lazy", 7) == "shgf"


def test_non_alpha_characters():
    assert caesar_cipher("hello, world! 123", 5) == "mjqqt, btwqi! 123"


def test_case_insensitivity():
    assert caesar_cipher("HeLloO", 3) == "khoorr"

