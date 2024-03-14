import numpy as np
import matplotlib.pylab as plt

class SimpleLinearRegression:
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.m = ((np.mean(X) * np.mean(y) - np.mean(X*y)) / ((np.mean(X)**2) - np.mean(X**2)))

        self.b = np.mean(y) -self.m * np.mean(X)

    def coeffs(self):
        return self.m , self.b
    
    def predict(self):
        self.y_pred = self.m * self.X + self.b
        return self.y_pred
    
    def r_squared(self):
        self.y_mean = np.full((len(self.y)), np.mean(self.y))
        err_reg = sum((self.y - self.y_pred)**2)
        err_y_mean = sum((self.y - self.y_mean)**2)
        return (1 - (err_reg / err_y_mean))
    @staticmethod
    def plot_regression (X, y, y_pred, log=None, title="Linear Regression"):
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