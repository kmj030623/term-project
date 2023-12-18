import pandas as pd

def find_data_by_destination(csv_file_path, target_destination):
    # CSV 파일을 pandas DataFrame으로 읽어오기
    data = pd.read_csv(csv_file_path, encoding='cp949')

    # "도착정류장역"을 기준으로 데이터 필터링
    result_data = data[data['도착정류장역'] == target_destination]

    return result_data

csv_file_path = '/content/버스 시간 통계.csv'
target_destination = input("찾고자 하는 도착 정류장 역을 입력하세요: ")

result_data = find_data_by_destination(csv_file_path, target_destination)
print(result_data)
