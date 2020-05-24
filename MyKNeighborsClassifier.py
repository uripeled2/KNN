
const_random_num = 5
const_k = 1

class MyKNeighborsClassifier:
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def pradict(self, x_test):
        predictions = []
        i = 0
        for row in x_test:
            i += 1
            lst_of_closest = self.closest(row, const_k)
            lst_of_closest.sort(key= lambda t: self.y_train[t])
            lable = self.domint(lst_of_closest)
            predictions.append(lable)
        return predictions

    def closest(self, row, k):
        min = 2 ** 16 - 1
        best = []
        for i in range(len(self.x_train)):
            if distance.euclidean(row, self.x_train[i]) < min:
                min = distance.euclidean(row, self.x_train[i])
                if len(best) == k:
                    best[k - 1] = i
                    best.sort(key=lambda t: distance.euclidean(row, self.x_train[t]))
                    min = distance.euclidean(row, self.x_train[best[k - 1]])
                else:
                    best.append(i)
        return best

    def domint(self, lst_of_closest):
        num = 0
        lable = None
        best_l = None
        best_num = 0
        for i in range(len(lst_of_closest) - 1):
            if y_train[lst_of_closest[i]] == y_train[lst_of_closest[i + 1]]:
                num += 1
            else:
                if num > best_num:
                    best_l = y_train[lst_of_closest[i]]
                    best_num = num
                num = 0
        if best_l is None:
            best_l = y_train[lst_of_closest[len(lst_of_closest) - 1]]
        return best_l


def split_data(x, y):
    x_train = []
    x_test = []
    y_train = []
    y_test = []
    for i in range(len(x)):
        if random.choice(range(1, 11)) >= const_random_num:
            x_train.append(x[i])
            y_train.append(y[i])
        else:
            x_test.append(x[i])
            y_test.append(y[i])
    return x_train, x_test, y_train, y_test
