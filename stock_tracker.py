import csv
import yfinance as yf

#note: for RNKFG,50.24,1 NOT under yfinance API
hm={}
unchanged={}
curre={}
profit=[]

#function to get data from ticker
def get_curr(symbol):
    ticker=yf.Ticker(symbol)
    today=ticker.history(period="1d")
    return today["Close"][0]
#function to process csv file
def lister(csv_name):
    name=[]
    price=[]
    count=[]
    totprofit=[]
    current_price_of_stock=[]
    with open(csv_name) as doc:
        purchased=csv.reader(doc, delimiter=",")
        for row in purchased:
            for i in range(len(row)):
                if i%3==0:
                    name.append(row[i])
                    current_price_of_stock.append(float(get_curr(row[i])))
                if i%3==1:
                    price.append(row[i])
                if i%3==2:
                    count.append(row[i])
    for i in range(len(name)):
        qprofit=float(current_price_of_stock[i])-float(price[i])
        profit.append(qprofit)
        totprofit.append(float(count[i])*qprofit)
        hm[qprofit]=name[i]
        unchanged[name[i]]=price[i]
        curre[name[i]]=current_price_of_stock[i]
#sorts the proft in terms of low to high
def sorter(array):
    arr=len(array)
    organized={}
    for i in range(arr):
        for j in range(0, arr-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
    for i in range(len(array)):
        organized[hm[array[i]]]=array[i]
    return organized

lister("purchased_stocks.csv")
print("\n \n \n \n \n \n \n \n \n \n \n \n ")
print(f"purchase price: {unchanged}")
print(f"current price: {curre}")
print(f"Organized Profit per Stock: {sorter(profit)}")
