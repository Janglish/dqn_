import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./logs/0.monitor.csv', names=['r', 'l', 't'])
df = df.drop(range(2))

# 報酬のグラフ表示
x = range(len(df['r']))
y = df['r'].astype(float)
plt.plot(x, y)
plt.xlabel('episode')
plt.ylabel('reward')
plt.show()

# エピソード長のグラフ表示
x = range(len(df['l']))
y = df['l'].astype(float)
plt.plot(x, y)
plt.xlabel('episode')
plt.ylabel('episode len')
plt.show()

print(df['l'].astype(float).sum())

df['r'] = df['r'].astype(float)
df['cumsum'] = df['r'].cumsum()

# 平均報酬のグラフ表示
x = range(len(df['r']))
y = [df.loc[i + 2, 'cumsum'] / (i + 1) for i in range(len(df['cumsum']))]

plt.plot(x, y)
plt.xlabel('episode')
plt.ylabel('average reward')
plt.show()

print(df['l'].astype(float).sum())