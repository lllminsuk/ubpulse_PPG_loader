import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

HI_path = './ubpulse/ubpulse_data.csv'

data = pd.read_csv(HI_path)
# print(data)
HI = data['HI']

HI_xlabel = np.linspace(0, len(HI)-1, len(HI))

plt.title('HI signal export')
plt.plot(HI_xlabel, HI, color='orange', label='HI_wave')
plt.legend()
plt.xlabel('Count')
plt.ylabel('HI')
plt.show()