import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

HR_path = './ubpulse/ubpulse_data.csv'

data = pd.read_csv(HR_path)
# print(data)
HR = data['HR']
HR_A = data['HR_A']

HR_xlabel = np.linspace(0, len(HR)-1, len(HR))

plt.title('HR signal export')
plt.plot(HR_xlabel, HR, color='orange', label='HR_wave')
plt.plot(HR_xlabel, HR_A, color='blue', label='HR_A_wave')
plt.legend()
plt.xlabel('Count')
plt.ylabel('HR')
plt.show()