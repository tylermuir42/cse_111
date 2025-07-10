from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("525 S Center St, , ID 83460") == ""
    assert extract_city(", Rexburg, ID 83460") == "Rexburg"
    assert extract_city("525 S Center St, Rexburg, 83460") == "Rexburg"

def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("525 S Center St, , ID 83460") == "ID"
    assert extract_state(", Rexburg, ID 83460") == "ID"
    assert extract_state("525 S Center St, Rexburg, 83460") == ""

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("525 S Center St, , ID 83460") == "83460"
    assert extract_zipcode(", Rexburg, ID 83460") == "83460"
    assert extract_zipcode("525 S Center St, Rexburg, 83460") == "83460"
    # assert extract_zipcode("525 S Center St, Rexburg, ID ") == ""
    

pytest.main(["-v", "--tb=line", "-rN", __file__])