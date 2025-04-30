import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Valid1$Password", True),
    ("Another@123", True),
    ("Strong-Pass1!", True),
    ("A1$LongerPassword", False),
    ("Short1!", False),
    ("1!A", False),
    ("1234567", False),
    ("!@#$%^&*", False),
    ("ThisPasswordIsWayTooLong1!", False),
    ("12345678901234567", False),
    ("NoDigit!A", False),
    ("NoSpecialChar1", False),
    ("OnlyLetters", False),
    ("NoSpecialChar1", False),
    ("12345678A", False),
    ("lowercase1!", False),
    ("12345678!", False),
    ("Invalid@Char#1!", True),
    ("InvalidChar1*", False),
    ("InvalidChar1%", False),
    ("InvalidChar1+", False),
    ("A1$", False),
    ("A1$" * 5, True),
    ("A1$" * 4 + "A", True),
    ("A1$" * 4 + "B", True),
    ("A1$" * 4 + "B!", True),
    ("A1$" * 4 + "B!C", True),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
