import unittest
import pytest
import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        # self.assertEqual(awesome.smile(), ":)")
        assert awesome.smile() == ":)"


# if __name__ == '__main__':
#     unittest.main()
