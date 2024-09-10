"""
Sample tests.
"""
from django.test import SimpleTestCase

from app import function


class CalcTests(SimpleTestCase):
    """Test the fucntion module."""

    def test_add_numbers(self):
        """Test adding numbers."""
        res = function.add(5, 6)

        self.assertEqual(res, 11)
