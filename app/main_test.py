from main import return_backwards_string, get_mode
import unittest
import os

class TestMain(unittest.TestCase):
    
    def test_return_backwards_string(self):
        self.assertEqual(return_backwards_string("hello"), "olleh")
        self.assertEqual(return_backwards_string("world"), "dlrow")
        self.assertEqual(return_backwards_string(""), "")

    def test_get_mode(self):
        os.environ['MODE'] = 'test'
        self.assertEqual(get_mode(), 'test')
        del os.environ['MODE']
        self.assertEqual(get_mode(), 'No mode set')
        
if __name__ == '__main__':
    unittest.main()