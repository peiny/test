import pytest
import awesome


class TestMethods:
    def test_smile(self):
        assert awesome.smile() == ":)"
    
    def test_extra(self):
        assert awesome.addmore() ==":"


