import itertools
import random
import unittest

# Задача 1: Расчет вероятности выпадения определенного числа на кубике
def probability_of_dice_roll(dice_number, target_number):
    total_outcomes = 6  # Общее количество возможных исходов при броске кубика
    favorable_outcomes = 0  # Количество благоприятных исходов

    for outcome in range(1, total_outcomes + 1):
        if outcome == target_number:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

print("Задача 1: Вероятность выпадения числа 3 на кубике =", probability_of_dice_roll(1, 3))

# Задача 2: Расчет вероятности комбинации при броске двух кубиков
def probability_of_dice_combination(target_sum):
    total_outcomes = 6 * 6  # Общее количество возможных исходов при броске двух кубиков
    favorable_outcomes = 0  # Количество благоприятных исходов

    for outcome in itertools.product(range(1, 7), repeat=2):
        if sum(outcome) == target_sum:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

print("Задача 2: Вероятность выпадения суммы 7 при броске двух кубиков =", probability_of_dice_combination(7))

# Задача 3: Расчет вероятности выпадения определенной последовательности в подбрасывании монеты
def probability_of_coin_sequence(sequence, num_trials):
    total_outcomes = 2 ** len(sequence)  # Общее количество возможных исходов при броске монеты
    favorable_outcomes = 0  # Количество благоприятных исходов

    for outcome in itertools.product("HT", repeat=len(sequence)):
        if "".join(outcome) == sequence:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

sequence_to_check = "HTH"
#print("Задача 3: Вероятность получения последовательности", sequence_to_check,  "подбрасываниях монеты =", probability_of_coin_sequence(sequence_to_check))


# Задача 4: Моделирование броска монеты
def coin_toss_simulation(num_tosses):
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        outcome = random.choice(["H", "T"])
        if outcome == "H":
            heads_count += 1
        else:
            tails_count += 1

    probability_heads = heads_count / num_tosses
    probability_tails = tails_count / num_tosses

    return probability_heads, probability_tails

num_tosses = 1000
print("Задача 4: Моделирование броска монеты (", num_tosses, "попыток):")
probability_heads, probability_tails = coin_toss_simulation(num_tosses)
print("Вероятность выпадения орла:", probability_heads)
print("Вероятность выпадения решки:", probability_tails)

# Задача 5: Расчет вероятности суммы значений двух кубиков после броска
def probability_of_dice_sum(target_sum, num_dice):
    total_outcomes = 6 ** num_dice  # Общее количество возможных исходов при броске num_dice кубиков
    favorable_outcomes = 0  # Количество благоприятных исходов

    for outcome in itertools.product(range(1, 7), repeat=num_dice):
        if sum(outcome) == target_sum:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

target_sum = 7
num_dice = 2
print("Задача 5: Вероятность выпадения суммы", target_sum, "при броске", num_dice, "кубиков =", probability_of_dice_sum(target_sum, num_dice))

def probability_of_dice_roll(dice_number, target_number):
    total_outcomes = 6
    favorable_outcomes = 0

    for outcome in range(1, total_outcomes + 1):
        if outcome == target_number:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

def probability_of_dice_combination(target_sum):
    total_outcomes = 6 * 6
    favorable_outcomes = 0

    for outcome in itertools.product(range(1, 7), repeat=2):
        if sum(outcome) == target_sum:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

def probability_of_coin_sequence(sequence, num_trials):
    total_outcomes = 2 ** len(sequence)
    favorable_outcomes = 0

    for outcome in itertools.product("HT", repeat=len(sequence)):
        if "".join(outcome) == sequence:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

def coin_toss_simulation(num_tosses):
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        outcome = random.choice(["H", "T"])
        if outcome == "H":
            heads_count += 1
        else:
            tails_count += 1

    probability_heads = heads_count / num_tosses
    probability_tails = tails_count / num_tosses

    return probability_heads, probability_tails

def probability_of_dice_sum(target_sum, num_dice):
    total_outcomes = 6 ** num_dice
    favorable_outcomes = 0

    for outcome in itertools.product(range(1, 7), repeat=num_dice):
        if sum(outcome) == target_sum:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

def main():
    print("Задача 1: Вероятность выпадения числа 3 на кубике =", probability_of_dice_roll(1, 3))
    
    target_sum = 7
    print("Задача 2: Вероятность выпадения суммы", target_sum, "при броске двух кубиков =", probability_of_dice_combination(target_sum))
    
    sequence_to_check = "HTH"
    num_trials = 100
    print("Задача 3: Вероятность получения последовательности", sequence_to_check, "при", num_trials, "подбрасываниях монеты =", probability_of_coin_sequence(sequence_to_check, num_trials))
    
    num_tosses = 1000
    print("Задача 4: Моделирование броска монеты (", num_tosses, "попыток):")
    probability_heads, probability_tails = coin_toss_simulation(num_tosses)
    print("Вероятность выпадения орла:", probability_heads)
    print("Вероятность выпадения решки:", probability_tails)
    
    target_sum = 7
    num_dice = 2
    print("Задача 5: Вероятность выпадения суммы", target_sum, "при броске", num_dice, "кубиков =", probability_of_dice_sum(target_sum, num_dice))

    class TestProbabilityFunctions(unittest.TestCase):
        def test_probability_of_dice_roll(self):
            self.assertEqual(probability_of_dice_roll(1, 3), 1/6)

        def test_probability_of_dice_combination(self):
            self.assertEqual(probability_of_dice_combination(7), 6/36)

        def test_probability_of_coin_sequence(self):
            self.assertAlmostEqual(probability_of_coin_sequence("HTH", 100), 0.25, delta=0.01)

        def test_coin_toss_simulation(self):
            heads, tails = coin_toss_simulation(1000)
            self.assertAlmostEqual(heads + tails, 1.0, delta=0.05)

        def test_probability_of_dice_sum(self):
            self.assertAlmostEqual(probability_of_dice_sum(7, 2), 6/36)
if __name__ == "__main__":
    unittest.main()