"""
Dự án bắt đầu với mục đích để học Data Analyst, không có mục đích khác
Dưới đây, trong file này có ghi step by step to Start to end project
Let's Do it :))
"""
# import thư viện, 
# pandas là một thư viện giúp hỗ trợ đọc CSV làm việc với excel cực mạnh
import pandas as pd


"""
Bước 1: Sau khi có dữ liệu với file excel chúng ta cần làm gì?
"""

def main():
  df = pd.read_csv("sales_data.csv", sep=";")
  #print(df.head())
  df.info()

if __name__== "__main__":
  main()

