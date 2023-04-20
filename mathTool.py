import tkinter as tk
import numpy as np
from scipy.constants import physical_constants
import time

class Unit_Convertor_Math:

    def __init__(self, inputNumber, unit1, unit2):

        self.num   = inputNumber
        self.unit1 = unit1
        self.unit2 = unit2

    def __repr__(self):

        return f'<Convert "{self.num} {self.unit1}" units to "{self.unit2}"'
    
    def check_input(self):
	    try:
	        num_float = float(self.num)
	        return num_float
	    except ValueError:
	        return False

    def unit_convertor(self):

        if self.check_input() == False:
        	return ' ', self.unit2
        else:	
        	self.num = self.check_input()

        e = physical_constants['electron volt'][0]
        k = physical_constants['Boltzmann constant'][0]   # (J/K)
        h = physical_constants['Planck constant'][0]      # (J*s)
        c = physical_constants['speed of light in vacuum'][0] * 1e9  # (nm/s)

        def Hz_to_eV(num):
            return h * num / e

        def Hz_to_J(num):
            return h * num

        def nm_to_eV(num):
            return (h*c/e) / num

        def nm_to_J(num):
            return (h*c/e) / num * e

        def K_to_eV(num):
            return num * k / e

        def K_to_J(num):
            return num * k

        conversion_functions = {
            ('Hz', 'eV'): Hz_to_eV,
            ('Hz', 'J'): Hz_to_J,
            ('nm', 'eV'): nm_to_eV,
            ('nm', 'J'): nm_to_J,
            ('K', 'eV'): K_to_eV,
            ('K', 'J'): K_to_J,
        }

        func = conversion_functions[(self.unit1, self.unit2)]

        return float(func(self.num)), str(self.unit2)