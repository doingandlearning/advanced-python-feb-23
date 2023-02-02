import numpy as np
import matplotlib.pyplot as plt

data = np.random.random(20)

plt.xlabel("Element in array")
plt.ylabel('Value')
plt.stem(data)
plt.show()

