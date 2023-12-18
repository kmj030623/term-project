import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/순천대학교 정류장 차내인원.csv')

time_slots = df.columns[3:]  # 06(승차)부터 22(승차)까지의 열 선택
passenger_counts = df.iloc[5, 3:]  #  번째 행의 데이터 선택

plt.plot(time_slots, passenger_counts, marker='o', label='노선 {}'.format(df.iloc[5, 2]))
plt.title('{}에서 {}로 가는 노선의 시간대별 승차 인원'.format(df.iloc[5, 0], df.iloc[5, 1]))
plt.xlabel('시간대')
plt.ylabel('승차 인원')
plt.grid(True)
plt.legend()
plt.show()
