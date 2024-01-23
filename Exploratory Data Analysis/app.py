import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns  # data visualization library  
import matplotlib.pyplot as plt
import time

data = pd.read_csv('data.csv')

#2: Separate Target from Features

data.head()
col = data.columns
print (col)
y = data.diagnosis
drop_cols = ['Unnamed: 32', 'id', 'diagnosis']
x = data.drop(drop_cols, axis = 1)
x.head()

#3: Plot Diagnosis Distribution

ax = sns.countplot(y, label='Count')
B, M = y.value_counts()
print('Number of Benign Tumors:', B)
print('Number of Maliign Tumors:', M)

x.describe()

#3: Plot Diagnosis Distribution

ax = sns.countplot(y, label='Count')
B, M = y.value_counts()
print('Number of Benign Tumors:', B)
print('Number of Maliign Tumors:', M)

x.describe()

# Data Visualization

#4: Visualizing Standardized Data with Seaborn

data = x
data_std = (data - data.mean()) / data.std()
data = pd.concat([y, data_std.iloc[:, 0:10]], axis=1)
data = pd.melt(data, id_vars = 'diagnosis',
              var_name = 'features',
              value_name = 'value')
plt.figure(figsize=(10, 10))
sns.violinplot(x ='features', y='value', hue='diagnosis', data=data, split=True, inner='quart')
plt.xticks(rotation=45)

sns.boxplot(x= 'features', y='value', hue='diagnosis', data=data)
plt.xticks(rotation=45)

# 6: Using Joint Plots for Feature Comparison

sns.jointplot(x.loc[:, 'concavity_worst'],
            x.loc[:, 'concave points_worst'],
            kind='regg',
            color='#ce1414')

#7: Observing the Distribution of Values and their Variance with Swarm Plots

sns.set(style='whitegrid', palette="muted")
data = x
data_std = (data - data.mean()) / data.std()
data = pd.concat([y, data_std.iloc[:, 0:10]], axis=1)
data = pd.melt(data, id_vars = 'diagnosis',
              var_name = 'features',
              value_name = 'value')
plt.figure(figsize=(10, 10))
sns.swarmplot(x ='features', y='value', hue='diagnosis', data=data)
plt.xticks(rotation=45)

#8: Observing all Pair-wise Correlations

f, ax = plt.subplots(figsize=(18,18))
sns.heatmap(x.corr(), annot=True, linewidth=.5, fmt='.1f', ax=ax);

