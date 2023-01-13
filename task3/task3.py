from io import StringIO
import csv


def postProcessRelations(relations):
  return [sorted(list(set([int(node) for node in relation]))) for relation in relations]


def task(csvString):
  f = StringIO(csvString)  
  connections = list(csv.reader(f, delimiter=','))
  relations = [[], [], [], [], []]

  for connection in connections:
    relations[0].append(connection[0])
    relations[1].append(connection[1])
    for next_connection in connections:
      if next_connection != connection:
        if connection[1] == next_connection[0]:
          relations[2].append(connection[0])
          relations[3].append(next_connection[1])
        elif connection[0] == next_connection[0]:
          relations[4].append(connection[1])

  return postProcessRelations(relations)


