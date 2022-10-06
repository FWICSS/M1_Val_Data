import pandas as pd
import numpy as np

dB = pd.read_csv("AIGLE_tp4.csv")
data = dB.copy()
data = data.loc[data["Value"] != "?"]
print(data)
Q3, Q1 = np.percentile(float(data["Value"]), [75, 25])
print("q1 : ",Q1,"q2 : ",Q3)