import unittest
from main import subtract

class TestAdd(unittest.TestCase):

   def test_subtract(self):
       self.assertEqual(subtract(2, 1), 1)
       self.assertEqual(subtract(5, 1), 4)
       self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
   unittest.main()
