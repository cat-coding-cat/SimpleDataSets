import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./global_temperture.csv")
print(df)
plt.plot(df.Year, df.Lowess, linewidth=3)
plt.show()
