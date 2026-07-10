# app.py icin unit testler.

from app import is_valid_email


def test_is_valid_email_returns_true_for_valid_addresses():
    assert is_valid_email("volkan@example.com") is True
    assert is_valid_email("user.name+tag@sub.domain.co") is True


def test_is_valid_email_returns_false_for_invalid_addresses():
    assert is_valid_email("invalid-email") is False
    assert is_valid_email("missing@domain") is False
    assert is_valid_email("") is False
    assert is_valid_email(None) is False