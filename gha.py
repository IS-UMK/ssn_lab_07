import numpy as np

class GHA(object):
    
    def __init__(self, n_components=1, eta=0.01, epochs=100):
        self.eta = eta
        self.n_components = n_components
        self.epochs = epochs
        
    def init(self, X):
        # TODO inicjuj macierz wag self.W o kształcie [n_components, ilość zmiennych ] 
        
        return self

    def fit(self, X):
        # TODO algorytm uczenia GHA

        return self
            
    def transform(self, X):
        return (self.W @ X.T).T

    def inverse_transform(self, Y):
        return Y @ self.W