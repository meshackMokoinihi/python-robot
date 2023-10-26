
import unittest
from io import StringIO
from unittest.mock import patch
import robot
import world


class Test_robot(unittest.TestCase):
    def test_for_import(self):
        import turtle
        import world.text.world as world
        import sys

        self.assertTrue('turtle' in sys.modules, "turtle module should be imported")
        self.assertTrue("world" in sys.modules, "word module should be imported")
        self.assertTrue("sys" in sys.modules, "sys module should be imported")


    @patch("sys.stdin", StringIO("HAL\n"))
    def test_robot_name(self):
        self.assertEqual(robot.get_robot_name(), """HAL""")

        
    @patch("sys.stdin", StringIO("forward 10\nback 10\nright\nleft\nreplay\nhelp\n" ))    
    def test_command(self):
        self.assertEqual(robot.get_command(robot_name="HAL"), """forward 10""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """back 10""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """right""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """left""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """replay""")
        self.assertEqual(robot.get_command(robot_name="HAL"), """help""")


    @patch("sys.stdin", StringIO("back\n"))
    def test_do_back(self):
        names = world.w("HAL", 10)
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

        

if __name__ == '__main__':
    unittest.main()
