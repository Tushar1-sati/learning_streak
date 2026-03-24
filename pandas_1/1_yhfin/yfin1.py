
import yfinance as yf
data=yf.download('RELIANCE.NS',multi_level_index=False)
print(data)
# print(data.columns)
# l1=[]
# for i in data.columns:
#     l1.append(i[0])
# data.columns=l1
# print(data)


data=yf.download('HDFCBANK.NS')
print(data)
data.columns=[[i[0] for i in data.columns]]
data
