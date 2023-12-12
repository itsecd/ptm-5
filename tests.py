import unittest
from unittest.mock import patch
from game import results

class TestGame(unittest.TestCase):
    
    @patch('game.computer_choice', 'Snake')
    @patch('game.user_choice', 's')
    def test_result_draw_snake(self):
        """Проверка, что очки не изменились, если оба выбрали змею
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 0)
        self.assertEqual(computer_points, 0)
        

if __name__ == '__main__':
    unittest.main()