# Guess the number.

# Create an algorithm that generates random value, yesterday try to guess until you hit the number.

from time import sleep
import random


class GuessTheNumber:
    def __init__(self):
        self.value_random = 0
        self.value_min = 1
        self.value_max = 100
        self.try_again = True

    def start(self):
        self.generate_number_random()
        self.ask_value_random()

        try:
            while self.try_again:
                if int(self.the_kick) > self.value_random:
                    print('Kick a lower value.')
                    self.ask_value_random()
                elif int(self.the_kick) < self.value_random:
                    print('Guess a higher value')
                    self.ask_value_random()
                if int(self.the_kick) == self.value_random:
                    self.try_again = False
                    print('Congratulations, you got it right!'.upper())
                    sleep(1)
                    print(f'Generated value: {self.value_random}'.upper())
        except:
            print('Please enter numbers only!'.upper())
            self.start()

    def ask_value_random(self):
        self.the_kick = input('Kick a Number: ')

    def generate_number_random(self):
        self.value_random = random.randint(self.value_min, self.value_max)


kick = GuessTheNumber()
kick.start()
