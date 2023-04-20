from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    dicts_traduzido = read_brazilian_file(path)
    for dict_traduzido in dicts_traduzido:
        assert 'title' in dict_traduzido
        assert 'salary' in dict_traduzido
        assert 'type' in dict_traduzido
