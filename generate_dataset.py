import random
import pandas as pd
import numpy as np

NUM_ROWS = 5000
data = []

for _ in range(NUM_ROWS):
    age = random.randint(18, 85)
    gender = random.choice(["Male", "Female"])

