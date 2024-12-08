import unittest

from core.rover import Rover


class TestRover(unittest.TestCase):

    def setUp(self):
        self.rover = Rover()

    def test_rover_move_r_0(self):
        movements = "R"
        self.assertEqual(self.rover.rover_move(movements), "0:0:E")
        self.assertEqual(self.rover.rover_move(movements), "0:0:S")
        self.assertEqual(self.rover.rover_move(movements), "0:0:W")
        self.assertEqual(self.rover.rover_move(movements), "0:0:N")

    def test_rover_move_l(self):
        movements = "L"
        self.assertEqual(self.rover.rover_move(movements), "0:0:W")
        self.assertEqual(self.rover.rover_move(movements), "0:0:S")
        self.assertEqual(self.rover.rover_move(movements), "0:0:E")
        self.assertEqual(self.rover.rover_move(movements), "0:0:N")

    def test_rover_move_m_n(self):
        movements = "M"
        self.assertEqual(self.rover.rover_move(movements), "0:1:N")
        self.assertEqual(self.rover.rover_move(movements), "0:2:N")

    def test_rover_move_m_e(self):
        movements = "M"
        self.rover.current_state = "0:0:E"
        self.assertEqual(self.rover.rover_move(movements), "1:0:E")
        self.assertEqual(self.rover.rover_move(movements), "2:0:E")

    def test_rover_move_m_s(self):
        movements = "M"
        self.rover.current_state = "0:0:S"
        self.assertEqual(self.rover.rover_move(movements), "0:1:S")
        self.assertEqual(self.rover.rover_move(movements), "0:2:S")

    def test_rover_move_m_w(self):
        movements = "M"
        self.rover.current_state = "0:0:W"
        self.assertEqual(self.rover.rover_move(movements), "1:0:W")
        self.assertEqual(self.rover.rover_move(movements), "2:0:W")

    def test_rover_moves(self):
        movements = "RMMLML"
        self.assertEqual(self.rover.rover_move(movements), "2:1:W")
