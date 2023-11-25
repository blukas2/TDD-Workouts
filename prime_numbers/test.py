from main import is_prime, dividable_by_any

def test_is_prime():
    assert isinstance(is_prime(1), bool)
    assert is_prime(0) == False
    assert is_prime(1) == True
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False

test_is_prime()


def test_dividable_by_any():
    assert isinstance(dividable_by_any(0), bool)
    assert dividable_by_any(0) == False
    assert dividable_by_any(2) == False
    assert dividable_by_any(4) == True
    assert dividable_by_any(3) == False
    assert dividable_by_any(6) == True
    assert dividable_by_any(9) == True
    assert dividable_by_any(10) == True
    assert dividable_by_any(11) == False

test_dividable_by_any()