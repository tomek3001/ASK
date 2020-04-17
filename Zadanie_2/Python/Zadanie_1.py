import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
kivy.require('1.11.1')
from Register import Register


class Zadanie1App(App):
    def build(self):
        return Label()


Zadanie1 = Zadanie1App()

Zadanie1.run()

