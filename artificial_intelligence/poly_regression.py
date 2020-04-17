import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

f, n = map(int, input().split())
data = {"F1":[],"F2":[],"Price":[]}

## stdin data
#for i in range(n):
#    data.append(map(float, input().split()))

data_file = open("data/poly_reg_data.txt","r")
# print(*data_file)
for line in data_file:
    data["F1"].append(line.split()[0])
    data["F2"].append(line.split()[1])
    data["Price"].append(line.split()[2])

## index_col=0
#df = pd.read_csv("poly_reg_data.txt", delimiter=" ")
#df.columns = ['F1','F2','Price']
#print(df["F1"].values)

df = pd.DataFrame(data)

plt.scatter(df["F1"],df["Price"])
plt.scatter(df["F2"],df["Price"])


X = df.iloc[:, :2].values
y = df.iloc[:, 2].values

model = LinearRegression()
model.fit(X, y)
print(model.predict([[0.05, 0.54]]))

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
poly.fit(X_poly, y)
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
print(poly_model.predict(poly.fit_transform([[0.51, 0.31]])))

tests = [[0.05, 0.54], [0.91, 0.91], [0.31, 0.76], [0.51, 0.31]]

for i in range(len(tests)) :
    print(poly_model.predict(poly.fit_transform([tests[i]])))

#plt.plot(X, model.predict(X), color = 'red') 
#plt.show()

#r_sq = model.score(X, y)
#intercept = model.intercept_
#slope = model.coef_

#print(str(slope) + " X + " + str(intercept) + " r_square = " + str(r_sq))
