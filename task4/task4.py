import numpy as np
import pandas as pd
import json


def task(csv_input):
    # Read data
    csv_data = []
    for csv_string in csv_input.split('\n'):
        csv_objects = csv_string.split(',')
        csv_data.append(csv_objects)
    dataframe = pd.DataFrame(csv_data)
    # Compare data
    compares = []
    for _, expert_data in dataframe.iterrows():
        row = expert_data.to_numpy()
        expert_matrix = []
        for i, e1 in enumerate(row):
            expert_matrix.append([])
            for e2 in row:
                if e1 < e2:
                    expert_matrix[i].append(1)
                elif e1 == e2:
                    expert_matrix[i].append(0.5)
                else:
                    expert_matrix[i].append(0)
        compares.append(np.matrix(expert_matrix))
    # Combine data
    combined = sum(compares) / len(compares)
    # Valued coefficients
    x = combined
    l = combined.shape[0]
    k = np.matrix([1/l] * l).T
    e = 0.001
    o = np.matrix([1, 1, 1])
    y = np.dot(x, k)
    la = np.dot(o, y)
    k_n = np.dot(1 / la, y.T).T
    while np.max(np.abs(k_n - k)) >= e:
        k = k_n
        y = np.dot(x, k)
        la = np.dot(o, y)
        k_n = np.dot(1/la, y.T).T
    coefficients = np.round(k_n, int(-np.log10(e)))
    # Return
    return json.dumps(coefficients.T.tolist()[0])


if __name__ == '__main__':
    print(task("1,3,2\n2,2,2\n1.5,3,1.5"))
    # [0.468, 0.169, 0.363]
