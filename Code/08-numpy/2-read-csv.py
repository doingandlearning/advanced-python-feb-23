import numpy as np
import pandas as pd

dataframe = pd.read_csv("WorldCupWinners.csv")

data = np.array(dataframe)
print(data[0][0])