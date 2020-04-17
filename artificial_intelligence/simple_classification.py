# Basic pandas reading, correlating, plotting of iris data 
# ‘data’, the data to learn, 
# ‘target’, the classification labels, 
# ‘target_names’, the meaning of the labels, 
# ‘feature_names’, the meaning of the features, 
# ‘DESCR’, the full description of the dataset, 
# ‘filename’, the physical location of iris csv dataset 

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris_data = load_iris()
# print(iris_data["data"])
# print(iris_data.data.shape) # 150 x 4
# print(iris_data.target) # 0 1 2
# print(iris_data.target_names) # 'setosa' 'versicolor' 'virginica'
# print(iris_data.feature_names) # 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'

iris_df = pd.DataFrame(iris_data.data)
iris_df.columns = iris_data["feature_names"]
print(iris_df.dtypes)
iris_setosa = iris_df.loc[iris_data.target == 0]
iris_versicolor = iris_df.loc[iris_data.target == 1]
iris_virginica = iris_df.loc[iris_data.target == 2]
# print(iris_virginica.head())

plt.grid()
plt.plot(iris_setosa["petal length (cm)"],'o')
plt.plot(iris_versicolor["petal length (cm)"],'o')
plt.plot(iris_virginica["petal length (cm)"],'o')
plt.show()

pd.set_option("precision",2)
# print(*iris_df.groupby(iris_data.target).size())
print(iris_df.describe()) # statistical summary
print(iris_df.corr(method="pearson")) # variables correlation
print(iris_df.skew()) # skewness from normal distribution

# histogram plot 
iris_df.hist()
plt.show()

# density plot
iris_df.plot(kind='density', subplots=True, layout=(2,2), sharex=False)
plt.show()

# Box and whisker plot
iris_df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# correlations matrix plot
correlations = iris_df.corr(method="pearson")
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,4,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(iris_df.columns)
ax.set_yticklabels(iris_df.columns)
plt.show()

# scatter matrix plot
pd.plotting.scatter_matrix(iris_df)
plt.show()