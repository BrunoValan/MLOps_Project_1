from app import hello

#pip freeze shows all versions that are isntalled
def test_hello():
    assert "demo hello" == hello()
