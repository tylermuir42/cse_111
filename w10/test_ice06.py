from ice_06 import compute_monthly_payment, compute_total_payment
from pytest import approx 
import pytest

def test_compute_monthly_payment():
    assert compute_monthly_payment(1000, 0.06, 10) == approx(11.02, abs=0.1)
    assert compute_monthly_payment(100, 0.06, 10) == approx(1.10, abs=0.1)

def test_compute_total_payment():
    assert compute_total_payment(1000, 12) == approx(12000, abs=0.01)



pytest.main(["-v", "--tb=line", "-rN", __file__])