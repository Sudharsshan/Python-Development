import pandas
import numpy as np
from sklearn import linear_model

# Read only the column required and convert them into numpy array for usage
# And use Ravel for converting the 2D array into 1D array
# Current column
current_Data = pandas.read_excel('C:/Games/Python Dev folder/Python-Development/LabPrograms/dataset/datasheet.xlsx', usecols=['Current']).to_numpy().ravel()
# Temperature column
temperature_Data = pandas.read_excel('C:/Games/Python Dev folder/Python-Development/LabPrograms/dataset/datasheet.xlsx', usecols=['Temperature']).to_numpy().ravel()
# MCB trip column
MCB_Data = pandas.read_excel('C:/Games/Python Dev folder/Python-Development/LabPrograms/dataset/datasheet.xlsx', usecols=['MCB state']).to_numpy().ravel()
# fit the linear regression model within these values
# Choose the required model for training it
baseModel = linear_model.LinearRegression()
# Convert the two obtained array values from excel sheet into a single 2D numpy array of format [[1,2],[3,4]]
inputParameters = np.stack((current_Data, temperature_Data))
inputParameters = np.array(inputParameters)
newArray = [0]*20
for i in range(0, 20, 1):
    newArray[i] = [inputParameters[0][i], inputParameters[1][i]]
inputParameters = newArray
# provide the required output 
requiredOutput = MCB_Data
# Train the model
baseModel.fit(inputParameters, requiredOutput)
# use the trained model to predict for the given parameters
model_output = baseModel.predict([[5, 27]])
prediction = np.round(model_output).astype(int)
print('Given input: 5A at 27*C')
print('Predicted output (MCB State): ','OFF' if (prediction[0] == 0) else 'ON')