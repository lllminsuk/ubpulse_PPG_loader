import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PI_path = './ubpulse/ubpulse_data.csv'

data = pd.read_csv(PI_path)
# print(data)
PI = data['PI']
PI_A = data['PI_A']

PI_xlabel = np.linspace(0, len(PI)-1, len(PI))

plt.title('PI signal export')
plt.plot(PI_xlabel, PI, color='orange', label='PI_wave')
plt.plot(PI_xlabel, PI_A, color='blue', label='PI_A_wave')
plt.legend()
plt.xlabel('Count')
plt.ylabel('PI')
plt.show()