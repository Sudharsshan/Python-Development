# A sample program given during the 6th workshop of IEEE GirlsGeek.ResourceWarning
# Date: 27-08-2024 
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
data = pd.read_excel('blaaaaaa')

Hour = data.iloc[:, 1].values.reshape(-1, 1)
TimerValue = data.iloc[:, 2].values

model = LinearRegression()
model = model.fit(Hour, TimerValue)

TImer_Predict = model.predict([[9], [10]])
print(TImer_Predict)