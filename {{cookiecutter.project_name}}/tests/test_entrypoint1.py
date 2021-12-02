import pytest

from {{cookiecutter.project_name}}.module1.entrypoint1 import X


@pytest.fixture
def x():
    return X()


def test_do_something(x):
    assert x.do_something()