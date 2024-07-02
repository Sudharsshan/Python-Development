# Date: 01-07-24
from sklearn import linear_model
baseModel = linear_model.LinearRegression()
inputParameters = [[1, 25], [1, 26], [1, 27], [1, 28], [1, 29], [1, 30],[2, 25], [2, 26], [2, 27], [2, 28], [2, 29], [2, 30], [3, 25], [3, 26], [3, 27], [3, 28], [3, 29], [3, 30], [4, 25], [4, 26], [4, 27], [4, 28], [4, 29], [4, 30], [5, 25], [5, 26], [5, 27], [5, 28], [5, 29], [5, 30]]
requiredOutput = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,]
baseModel.fit(inputParameters, requiredOutput)
prediction = baseModel.predict([[3, 27]])
print(prediction)