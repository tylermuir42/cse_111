from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("John", "Smith") == "Smith; John"
    assert make_full_name("", "Smith") == "Smith; "
    assert make_full_name("John", "") == "; John"


def test_extract_family_name():
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("; John") == ""
    assert extract_family_name("Smith; ") == "Smith"

def test_extract_given_name():
    assert extract_given_name("Smith; John") == "John"
    assert extract_given_name("; John") == "John"
    assert extract_given_name("Smith; ") == ""


pytest.main(["-v", "--tb=line", "-rN", __file__])