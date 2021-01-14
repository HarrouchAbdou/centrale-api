#!/usr/bin/env python
# coding: utf-8

# In[11]:



from openpyxl import Workbook
import time

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
# load dataset
def arima(filename):
    ts = open(filename)
    tsA = ts.read().split('\n')
    tsA = list(map(int, tsA))

    #oepn the exel file
    book = Workbook()
    sheet = book.active

    sheet['A1'] = "Predicted"
    sheet['B1'] = "Expected"
    sheet['C1'] = "Error"

    now = time.strftime("%x")
    sheet['A3'] = now



    # split into train and test sets

    size = int(len(tsA) * 0.66)
    train, test = tsA[0:size], tsA[size:len(tsA)]
    history = [x for x in train]
    predictions = list()
    # walk-forward validation
    j=2
    for t in range(len(test)):
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        sheet['A%d'%j] = yhat
        sheet['B%d'%j] = obs
        j+=1

    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    sheet['C2'] = '%.3f' % rmse
    book.save("sent.xlsx")

