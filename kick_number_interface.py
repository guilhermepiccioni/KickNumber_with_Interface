# Guess the number.

# Create an algorithm that generates random value, yesterday try to guess until you hit the number.

from time import sleep
import PySimpleGUI as sg
import random


class GuessTheNumber:
    def __init__(self):
        self.value_random = 0
        self.value_min = 1
        self.value_max = 50
        self.try_again = True

    def start(self):
        # Layout
        layout = [
            [sg.Text('You Kick',size=(39,0))],
            [sg.Input(size=(18,0),key='ValueKick')],
            [sg.Button('Play!')],
            [sg.Output(size=(39,10))]
        ]
        # Window
        self.window = sg.Window('Kick a Number!', layout=layout)

        self.generate_number_random()
        try:
            continuar = True
            while continuar:
                # Values
                self.event, self.values = self.window.Read()

                if self.event == 'Play!':
                    self.value_kick = self.values['ValueKick']

                if self.try_again:
                    if int(self.value_kick) > self.value_random:
                        print('Kick a lower value.')
                    elif int(self.value_kick) < self.value_random:
                        print('Guess a higher value')
                    elif int(self.value_kick) == self.value_random:
                        self.try_again = False
                        print('Congratulations, you got it right!'.upper())
                        sleep(1)
                        continuar = False
            

        except:
            print('Please only number!'.upper())
            self.start()

    def generate_number_random(self):
        self.value_random = random.randint(self.value_min, self.value_max)


kick = GuessTheNumber()
kick.start()
