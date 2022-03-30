
import random
import time
import pygame
from math import pi as pi

# runs a python file mutiple times
def run_mutiple_times(file_name, times):
    for i in range(times):
        exec(open(file_name).read())

path = "test3.py"
run_mutiple_times(path, 10)