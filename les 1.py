import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
#
# print("mean:", np.mean(data))
# print("median:", np.median(data))
# print("50th percentile (median):", np.percentile(data, 50))
# print("25th percentile:", np.percentile(data, 25))
# print("75th percentile:", np.percentile(data, 75))
# print("standard deviation:", np.std(data))
# print("variance:", np.var(data))

df = pd.read_csv('titanic.csv')
pd.options.display.max_columns = 8
# print(df.head())
# print(df.describe())
# small_df = df[['Age', 'Sex', 'Survived']]
# df['male'] = df['Sex'] == 'male'
# arr = df[['Pclass', 'Fare', 'Age']].values
# mask = arr[:, 2] < 18
# print(arr[mask])
# print(mask.sum())
# plt.scatter(df['Age'], df['Fare'])

df['male'] = df['Sex'] == 'male'
# X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
# y = df['Survived'].values
# print(df)
# # print('=====')
# # print(X)
# # print(y)

from sklearn.linear_model import LogisticRegression

# model = LogisticRegression()
#
# X = df[['Fare', 'Age']].values
# y = df['Survived'].values
#
# model.fit(X, y)
# print(model.coef_, model.intercept_)

# X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
# y = df['Survived'].values
#
# # model = LogisticRegression()
# # model.fit(X, y)
# #
# # # print(model.predict([[3, True, 22.0, 1, 0, 7.25]]))
# # print(df)
# # print(model.predict(X[:5]))
# # print(y[:5])
#
#
# model = LogisticRegression()
# model.fit(X, y)
# print(y.shape[0])
# y_pred = model.predict(X)
# print((y == y_pred).sum())
# print((y == y_pred).sum() / y.shape[0])
# print(model.score(X, y))


from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()

print(cancer_data.keys())
df = pd.DataFrame(cancer_data['data'], columns=cancer_data['feature_names'])
df['target'] = cancer_data['target']
X = df[cancer_data.feature_names].values
y = df['target'].values

model = LogisticRegression(solver='liblinear')
model.fit(X, y)
print("prediction for datapoint 0:", model.predict([X[0]]))
print(model.score(X, y))