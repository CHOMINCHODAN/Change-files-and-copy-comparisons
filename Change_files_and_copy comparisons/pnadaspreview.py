import pandas as pd
# 판다스의 대표적인 두 자료구조 시리즈 와 데이터프레임 에 대한 설명

# series = pd.Series([1,2,3,4]) # 인덱스를 따로 지정하지 않았기에 1, 2, 3, 4 옆에 자동으로 지정된 0, 1, 2, 3이라는 인덱스를 확일

# series2 = pd.Series([20,30,40,50], index=['first', 'sec', 'three', 'four']) # 생성할 때 인덱싱를 직접 지정할 수 있습니다.

#dataframe 생성

df = pd.read_csv("/home/rastech/PycharmProjects/pythonstudy/pandas basal/test.csv")

#행 바꾸기   갯수맞춰줘야해
df.index = ['fir', "sec", 'thre', 'four','five']

ds = pd.DataFrame(df)
# 특정 혹 열행만변경  rename()
#ds.rename(index= , inplace=True)

print(df.columns) #행 출력
print(ds.index) #인덱스 열 출력
print(ds)

# df.to_csv("time2.csv", index = False)

