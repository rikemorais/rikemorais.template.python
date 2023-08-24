import sys


def test_python_version():
    assert sys.version_info.major > 2, "A versão do Python não é maior que 2."
