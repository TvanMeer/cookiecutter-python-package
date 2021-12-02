import pytest

from {{cookiecutter.project_name}}.client import Client


@pytest.fixture
def client():
    return Client()
    
    
def test_func_1(client):
    assert client.func_1()
    
    
def test_func_2(client):
    assert client.func_2()