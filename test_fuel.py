import pytest
from fuel import convert
from fuel import gauge
def test_normality():
    assert convert("1/2") == 50
def test_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_valueError():
    with pytest.raises(ValueError):
        convert("2/1")
def test_valueError():
    with pytest.raises(ValueError):
        convert("-1/2")
def test_gaugeLow():
    assert gauge(1) == "E"
def test_gaugePercentage():
    assert gauge(50) == "50%"
def test_gaugeFull():
    assert gauge(99) == "F"
