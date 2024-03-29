import random

from scipy.spatial import distance
def euc(a,b):
    return distance.euclidean(a,b)

class scrappyKNN():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train


    def predict ( self, x_test ):
        predictions = []
        for row in x_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest ( self, row ):
        best_dist = euc ( row, self.x_train[0] )
        best_index = 0
        for i in range ( 1, len(self.x_train) ):
            dist = euc( row, self.x_train[i] )
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]