from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch


def test_counter():
    path = "data/jobs.csv"

    text_base = """Texto para finalidade de testar a função
    com muitas palavras só preciso de mais repetição nesse texto"""

    with patch("builtins.open", mock_open(read_data=text_base)):
        assert count_ocurrences(path, "Texto") == 2
        assert count_ocurrences(path, "notworld") == 0
        assert count_ocurrences(path, "texto") == 2
