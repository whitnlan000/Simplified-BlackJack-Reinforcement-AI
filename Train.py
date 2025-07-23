import random

from sklearn import neighbors,metrics
from sklearn.model_selection import train_test_split
import pandas

#Weather
import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
from sklearn.preprocessing import LabelEncoder

money = 1500

data = pandas.read_csv("BlackJack.csv")
print(data.columns)


x = data[["number1","draws"]].values
y = data[["win"]].values

#print(x[2])

#for i in range(len(x[0])):
#    x[:,i] = LabelEncoder().fit_transform(x[:,i])

#for i in range(len(y[0])):
#    y[:,i] = LabelEncoder().fit_transform(y[:,i])

knn = neighbors.KNeighborsRegressor(n_neighbors=2,weights="uniform")
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.2)

knn.fit(x_train,y_train)
prediction = knn.predict(x_test)
#accuracy = metrics.accuracy_score(y_test,prediction)

print("Test R^2 Score:", knn.score(x_test, y_test))

tests = input("tests:")
for i in range(int(tests)):
    print("Test",i)
    number = random.randint(1, 13)

    while number <= 14:
        draws = 1
        newcard = random.randint(1,13)
        if knn.predict([[number,draws]]) >= .8 or random.randint(1,10) == 1:
            number += newcard
            draws += 1
            open("BlackJack.csv", "a").write("\n" + str(number) + "," + str(17 <= number <= 21) + "," + str(draws))

    
    print(number,(number >= 21))