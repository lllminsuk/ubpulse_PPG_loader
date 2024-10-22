import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PPG_path = './ubpulse/ubpulse_data.csv'

data = pd.read_csv(PPG_path)
# print(data)
PPG = data['PPG'][:]

PPG_xlabel = np.linspace(0, len(PPG)-1, len(PPG))

plt.title('PPG signal export')
plt.plot(PPG_xlabel, PPG, color='orange', label='PPG_wave')
plt.legend()
plt.xlabel('Count')
plt.ylabel('PPG')
plt.show()