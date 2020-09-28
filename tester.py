import numpy as np
from sklearn.model_selection import KFold
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([9, 10, 11, 12])
kf = KFold(n_splits=2)
kf.get_n_splits(X)
2
print(kf)
KFold(n_splits=4, random_state=None, shuffle=False)
for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
#TRAIN: [2 3] TEST: [0 1]
#TRAIN: [0 1] TEST: [2 3]