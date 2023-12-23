import itertools
import random
import matplotlib.pyplot as plt

class DiceRollProbability:
    def probability_of_dice_roll(self, dice_number, target_number):
        total_outcomes = 6
        favorable_outcomes = 0

        for outcome in range(1, total_outcomes + 1):
            if outcome == target_number:
                favorable_outcomes += 1

        probability = favorable_outcomes / total_outcomes
        return probability

class DiceCombinationProbability:
    def probability_of_dice_combination(self, target_sum):
        total_outcomes = 6 * 6
        favorable_outcomes = 0

        for outcome in itertools.product(range(1, 7), repeat=2):
            if sum(outcome) == target_sum:
                favorable_outcomes += 1

        probability = favorable_outcomes / total_outcomes
        return probability

class CoinSequenceProbability:
    def probability_of_coin_sequence(self, sequence, num_trials):
        total_outcomes = 2 ** len(sequence)
        favorable_outcomes = 0

        for outcome in itertools.product("HT", repeat=len(sequence)):
            if "".join(outcome) == sequence:
                favorable_outcomes += 1

        probability = favorable_outcomes / total_outcomes
        return probability

class CoinTossSimulation:
    def coin_toss_simulation(self, num_tosses):
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

class DiceSumProbability:
    def probability_of_dice_sum(self, target_sum, num_dice):
        total_outcomes = 6 ** num_dice
        favorable_outcomes = 0

        for outcome in itertools.product(range(1, 7), repeat=num_dice):
            if sum(outcome) == target_sum:
                favorable_outcomes += 1

        probability = favorable_outcomes / total_outcomes
        return probability

class ProbabilityCalculator:
    def __init__(self):
        self.dice_roll_probability = DiceRollProbability()
        self.dice_combination_probability = DiceCombinationProbability()
        self.coin_sequence_probability = CoinSequenceProbability()
        self.coin_toss_simulation = CoinTossSimulation()
        self.dice_sum_probability = DiceSumProbability()

    def main(self):
        print("Задача 1: Вероятность выпадения числа 3 на кубике =", self.dice_roll_probability.probability_of_dice_roll(1, 3))

        target_sum = 7
        print("Задача 2: Вероятность выпадения суммы", target_sum, "при броске двух кубиков =", self.dice_combination_probability.probability_of_dice_combination(target_sum))

        sequence_to_check = "HTH"
        num_trials = 100
        print("Задача 3: Вероятность получения последовательности", sequence_to_check, "при", num_trials, "подбрасываниях монеты =", self.coin_sequence_probability.probability_of_coin_sequence(sequence_to_check, num_trials))

        num_tosses = 1000
        print("Задача 4: Моделирование броска монеты (", num_tosses, "попыток):")
        probability_heads, probability_tails = self.coin_toss_simulation.coin_toss_simulation(num_tosses)
        print("Вероятность выпадения орла:", probability_heads)
        print("Вероятность выпадения решки:", probability_tails)

        target_sum = 7
        num_dice = 2
        print("Задача 5: Вероятность выпадения суммы", target_sum, "при броске", num_dice, "кубиков =", self.dice_sum_probability.probability_of_dice_sum(target_sum, num_dice))

    def read_input_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines

    def write_output_file(self, filename, content):
        with open(filename, 'w') as file:
            file.writelines(content)

    def solve_dice_sum_problem(self, target_sum, num_dice):
        dice_sum_probability = DiceSumProbability()
        return dice_sum_probability.probability_of_dice_sum(target_sum, num_dice)


    def plot_dice_sum_probability(self, num_dice):
        x_values = list(range(num_dice, 6 * num_dice + 1))
        y_values = [self.solve_dice_sum_problem(target_sum, num_dice) for target_sum in x_values]

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, marker='o')
        plt.title(f"Probability of Dice Sum for {num_dice} Dice")
        plt.xlabel("Sum of Dice")
        plt.ylabel("Probability")
        plt.grid(True)
        plt.show()
