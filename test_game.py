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
        
    @patch('game.computer_choice', 'Water')
    @patch('game.user_choice', 'w')
    def test_result_draw_water(self):
        """Проверка, что очки не изменились, если оба выбрали воду
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 0)
        self.assertEqual(computer_points, 0)

    @patch('game.computer_choice', 'Gun')
    @patch('game.user_choice', 'g')
    def test_result_draw_gun(self):
        """Проверка, что очки не изменились, если оба выбрали пистолет
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 0)
        self.assertEqual(computer_points, 0)

    @patch('game.computer_choice', 'Snake')
    @patch('game.user_choice', 'w')
    def test_snake_drinks_water(self):
        """Проверка, что очки  изменились, если компьютер выбрал змею, а пользователь воду
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 0)
        self.assertEqual(computer_points, 1)

    @patch('game.computer_choice', 'Water')
    @patch('game.user_choice', 'g')
    def test_gun_sinks_in_water(self):
        """Проверка, что очки  изменились, если компьютер выбрал воду, а пользователь пистолет
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 0)
        self.assertEqual(computer_points, 1)
    
    @patch('game.computer_choice', 'Water')
    @patch('game.user_choice', 's')
    def test_snake_beats_water(self):
        """Проверка, что очки  изменились, если компьютер выбрал воду, а пользователь змею
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 1)
        self.assertEqual(computer_points, 0)

    @patch('game.computer_choice', 'Snake')
    @patch('game.user_choice', 'g')
    def test_gun_beats_snake(self):
        """Проверка, что очки  изменились, если компьютер выбрал змею, а пользователь пистолет
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 1)
        self.assertEqual(computer_points, 0)

    @patch('game.computer_choice', 'Gun')
    @patch('game.user_choice', 'w')
    def test_water_beats_gun(self):
        """Проверка, что очки  изменились, если компьютер выбрал оружие, а пользователь воду
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        results()
        self.assertEqual(user_points, 1)
        self.assertEqual(computer_points, 0)
        
    def test_maximum_score(self):
        """тест на максимальное количество очков
        """
        global user_points, computer_points
        user_points, computer_points = 0, 0
        max_rounds = 5
        for _ in range(max_rounds):
            with patch('game.computer_choice', 'Gun'), patch('game.user_choice', 's'):
                results()
        self.assertEqual(computer_points, max_rounds)
        self.assertEqual(user_points, 0)