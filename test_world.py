
import unittest
from io import StringIO
from unittest.mock import patch
import robot
import world.text.world as world


class MyTest(unittest.TestCase):

    @patch("sys.stdin", StringIO("forward 10\nback 10\nright\nleft\n" ))    
    def test_command(self):
        self.assertEqual(robot.get_command(robot_name="HAL"), """forward 10""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """back 10""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """right""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """left""")


    @patch("sys.stdin", StringIO("forward 10\n"))
    def test_do_forward(self):
        names = world.do_forward("HAL", '10')
        self.assertTrue(""" > HAL moved forward by 10 steps.""", names)


    @patch("sys.stdin", StringIO("back\n"))
    def test_do_back(self):
        names = world.do_back("HAL", 10)
        self.assertTrue(""" > HAL moved back by 10 steps.""", names)


    @patch("sys.stdin", StringIO("right\n"))
    def test_do_back(self):
        names = robot.do_right_turn("HAL")
        self.assertTrue(""" > HAL turned right.""", names)


    @patch("sys.stdin", StringIO("left\n"))
    def test_do_back(self):
        names = robot.do_left_turn("HAL")
        self.assertTrue(""" > HAL turned left.""", names)


    @patch("sys.stdin", StringIO("left\n"))
    def test_do_back(self):
        names = robot.do_left_turn("HAL")
        self.assertTrue(""" > HAL turned left.""", names)

    @patch("sys.stdin", StringIO("replay\n"))
    def test_do_back(self):
        names = robot.do_replay("HAL", "2")
        self.assertTrue(""" > HAL replayed 2 commands.""", names)

if __name__ == "__main__":
    unittest.main()
