import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    X=pd.read_csv("Linear_X_Train.csv")
    y=pd.read_csv("Linear_Y_Train.csv")

    x=X.values
    y=y.values
 
    model=LinearRegression()
    model.fit(x,y)
    #predicting the marks for working hours
    x_test=np.array(hrs)
    x_test=x_test.reshape((1,-1))
    return model.predict(x_test)[0]


    

