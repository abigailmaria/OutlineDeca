# test_outlinedeca.py
"""
Tests for OutlineDeca module.
"""

import unittest
from outlinedeca import OutlineDeca

class TestOutlineDeca(unittest.TestCase):
    """Test cases for OutlineDeca class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OutlineDeca()
        self.assertIsInstance(instance, OutlineDeca)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OutlineDeca()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
