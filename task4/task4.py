from io import StringIO
import math
import csv



def task(csvString):
  f = StringIO(csvString)
  connections = list(csv.reader(f, delimiter=','))

  nodesNumber = int(max(map(max, connections)))
  relationMatrix = getRelationMatrix(connections, nodesNumber)

  entropy = 0
  for row in range(nodesNumber):
    for col in range(5):
      if relationMatrix[row][col] != 0:
        entropy -= (relationMatrix[row][col] / (nodesNumber - 1)) * math.log(relationMatrix[row][col] / (nodesNumber - 1), 2)
  return round(entropy, 2)

def getRelationMatrix(connections: list, nodesNumber: int) -> list:
  matrix = [[0 for _ in range(5)] for _ in range(nodesNumber)]

  for connection in connections:
    node = int(connection[0])
    nextNode = int(connection[1])

    matrix[node - 1][0] += 1
    matrix[nextNode - 1][1] += 1
    for nextConnection in connections:
      if nextConnection != connections:
        if nextNode == int(nextConnection[0]):
          matrix[node - 1][2] += 1
          matrix[int(nextConnection[1]) - 1][3] += 1
        elif node == int(nextConnection[0]):
          matrix[nextNode - 1][4] += 1
  for row in matrix:
    if row[4] > 0:
      row[4] -= 1

  return matrix
