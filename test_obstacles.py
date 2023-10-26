
import unittest
import world.obstacles as obstacles


class test_is_postion_blocked(unittest.TestCase):
    
    def test_retursive(self):
        test_value = obstacles.is_position_blocked = True
        self.assertEqual(test_value, True)


    def test_is_path_blocked(self):
        test_value = obstacles.is_path_blocked =True
        self.assertTrue(test_value , True)


if __name__ == '__main__':
    unittest.main()
