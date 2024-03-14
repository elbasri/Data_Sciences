import numpy as np
import matplotlib.pylab as plt
from sklearn import metrics

class MultipleLinearRegression:
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        self.coeffs = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    def coeffs(self):
        return self.m , self.b
    
    def predict(self, X):
        X = np.array(X)
        result = np.zeros(len(X))
        for i in range(X.shape[1]):
            result += X[:, i] * self.coeffs[i]
        return result
    
    def gradient_descent(X, y, lr=0.05, epoch=10):
        '''GD for single feature'''
        m,b = 0.2, 0.2 #params
        log, mse = [],[] #list to store learning process
        N = len(X) # number of samples

        for _ in range(epoch):
            f = y - (m*X + b)

            #updating m and b
            m -= lr * (-2 * X.dot(f).sum()/N)
            b -= lr * (-2 * f.sum() / N)

            log.append((m, b))
            mse.append(metrics.mean_squared_error(y, (m*X + b)))

        return m,b,log, mse
    
    def SGD(self, X, y, lr=0.05, epoch=10, batch_size=1):
        m, b = 0.5, 0.5  # Initial parameters
        log, mse = [], []  # Lists to store the progression of the parameters and error

        for _ in range(epoch):
            indexes = np.random.randint(0, len(X), batch_size)
            
            Xs = np.take(X, indexes, axis=0).reshape(-1)  # Ensure Xs is correctly shaped as a vector
            ys = np.take(y, indexes)
            N = len(Xs)
            f = ys - (m * Xs + b)
            
            # Update m and b using gradient descent
            m -= lr * (-2 * np.dot(Xs, f).sum() / N)
            b -= lr * (-2 * f.sum() / N)

            log.append((m, b))
            mse.append(metrics.mean_squared_error(y, m * X + b))

        return m, b, log, mse

    
    def plot_regression(self, X, y, y_pred, log=None, title="Linear Regression"):
        plt.figure(figsize=(16,6))
        plt.rcParams['figure.dpi'] = 227
        plt.scatter(X, y, label='Data', c='#388fd8', s=6)
        if log != None:
            for i in range(len(log)):
                plt.plot(X, log[i][0]*X + log[i][1], lw=1, c='#caa727', alpha=0.35)
        plt.plot(X, y_pred, c='#ff7702', lw=3, label='Regression')
        plt.title(title, fontsize=14)
        plt.xlabel('Income', fontsize=11)
        plt.ylabel('Price', fontsize=11)
        plt.legend(frameon=True, loc=1, fontsize=10, borderpad=.6)
        plt.tick_params(direction='out', length=6, color='#a0a0a0', width=1, grid_alpha=.6)
        plt.show()