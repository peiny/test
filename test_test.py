import pytest
import awesome


class TestMethods:
    def test_smile(self):
        assert awesome.smile() == ":)"
    
    def test_addmore(self):
        assert awesome.addmore() ==":"
    
    def test_frown(self):
        assert awesome.frown() == ":("

