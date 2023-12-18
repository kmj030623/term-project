import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/순천대학교 정류장 차내인원.csv')

plt.plot(df.columns[3:], df.iloc[0, 3:], marker='o')
plt.title(f'{df.iloc[0, 0]}에서 {df.iloc[0, 1]}로 가는 {df.iloc[0, 2]} 노선의 시간대별 승차 인원')
plt.xlabel('시간대')
plt.ylabel('승차 인원')
plt.grid(True)
plt.show()
