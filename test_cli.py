import pytest
from cli import generate_summary

@pytest.fixture
def get_function(): 
    return generate_summary

def test_non_string_input():
    with pytest.raises(TypeError):
        generate_summary(123)
