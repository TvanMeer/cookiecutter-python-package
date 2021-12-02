import pytest

from {{cookiecutter.project_name}}.module2.entrypoint2 import Y


@pytest.fixture
def y():
    return Y()


def test_do_something(y):
    assert y.do_something()