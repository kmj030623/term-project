import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/순천대학교 정류장 차내인원.csv')

time_slots = df.columns[3:]
passenger_counts = df.iloc[4, 3:]

plt.plot(time_slots, passenger_counts, marker='o', label='노선 {}'.format(df.iloc[4, 2]))
plt.title('{}에서 {}로 가는 노선의 시간대별 승차 인원'.format(df.iloc[4, 0], df.iloc[4, 1]))
plt.xlabel('시간대')
plt.ylabel('승차 인원')
plt.grid(True)
plt.legend()
plt.show()