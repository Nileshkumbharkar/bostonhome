import pickle
import numpy as np


class Boston():
    def __init__(self,CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT):
        self.CRIM =CRIM
        self.ZN = ZN
        self.INDUS =INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX 
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT
        
    def load_model(self):
        with open('knn_model.pkl','rb') as f:
            self.model = pickle.load(f)
        with open('scaling.pkl','rb') as f :
            self.scale =pickle.load(f)

    def predict(self):
        self.load_model()
        test = np.array([self.CRIM, self.ZN, self.INDUS, self.CHAS, self.NOX, self.RM, self.AGE, self.DIS, self.RAD, self.TAX,
       self.PTRATIO, self.B, self.LSTAT],ndmin=2)

        self.scale_test=self.scale.transform(test)
        s=self.model.predict(self.scale_test)[0]
        return f'home price is {s} lacs INR'
    

if __name__ == '__main__':
    obj = Boston(6.320e-03, 1.800e+01, 2.310e+00, 0.000e+00, 5.380e-01, 6.575e+00,6.520e+01, 4.090e+00, 1.000e+00, 2.960e+02, 1.530e+01, 3.969e+02,4.980e+00)