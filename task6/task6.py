import numpy as np
import json


def getComparisonMatrices(inputCol):
  matrix = np.zeros((len(inputCol), len(inputCol)))
  for rowInd, row in enumerate(matrix):
    for colInd, col in enumerate(row):
      if inputCol[rowInd] < inputCol[colInd]:
        matrix[rowInd, colInd] = 1
      elif inputCol[rowInd] == inputCol[colInd]:
        matrix[rowInd, colInd] = 0.5
      else:
        matrix[rowInd, colInd] = 0
  return matrix


def task(jsonInput):
  inputList = np.array(json.loads(jsonInput)).T
  comparisonMatrices = []
  for inputCol in inputList.T:
    comparisonMatrices.append(getComparisonMatrices(inputCol))

  generalMatrix = np.zeros((len(inputList), len(inputList)))
  
  for i in range(len(inputList)):
    generalMatrix += comparisonMatrices[i]
  generalMatrix = generalMatrix / len(inputList)

  k0 = np.array([1 / len(inputList)] * len(inputList))
  y = generalMatrix.dot(k0)
  lambda1 = (np.ones(len(inputList))).dot(y)
  k1 = 1 / lambda1 * y
  while abs(max(k1 - k0)) >= 0.001:
    k0 = k1
    y = generalMatrix.dot(k0)
    lambda1 = (np.ones(len(inputList))).dot(y)
    k1 = 1 / lambda1 * y

  k1 = np.around(k1, 3)
  return json.dumps(k1.tolist())


