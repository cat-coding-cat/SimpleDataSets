import pandas as pd 
import matplotlib.pyplot as plt 
data= pd.read_csv('global_temperture.csv')


df=pd.DataFrame(data)


X = data.Year
Y = data.Lowess

# Set figure

plt.figure(figsize=(15, 12))

# Bar Plot

plt.bar(X, Y)

# Setting Ticks

plt.tick_params(axis='x',labelsize=15,rotation=90)
plt.tight_layout()

# Display

plt.show()
