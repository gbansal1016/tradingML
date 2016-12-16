
#%%

def areacircle(radius):
    area = 3.14*radius*radius
    print("area of circle" , area)

#%%

#%%

def areatriange(base, height):
    area = 0.5*base*height
    print("area of triangel" , area)

#%%

#%%

fname=input("Enter name")
print('Input name is ', fname)
#%%

#%%

def absolutevalue(number):
    if number >0:
        print(number)
    elif number <0:
        print( -1*number)
    else:
        print (0)
    

absolutevalue(-5)
absolutevalue(-5)
absolutevalue(0)


#%%

#%%
def fahtocelsius(fah):
    temp_str = input("enter fah")
    temp =int(temp_str)
    newtemp = (5/9)*(temp - 32)
    print(newtemp,"degree celsius")
#%%

#%%
nlis = [1,2,1,2,1,2]
#%%
#%%
def average(lis):
    sum = 0
    cnt = 0        
    for num in range(0,len(lis)):
        sum = sum + nlis[num]
        cnt = cnt + 1
    average = sum/len(lis)
    print("average is ", average)
#%%

#%%
import pandas as pd

def get_mean_volum(symbol):
    df = pd.read_csv("C:\\Users\\gbans6\\gbansalmba\\mlearning\\tradingML\\data\\{}.csv".format(symbol))
    return df['Volume'].mean()
    
    
    

def test_run():
    for symbol in ['AAPL', 'IBM']:
        print("MEAN VOLUME")
        print (symbol, get_mean_volum(symbol))

#%%
        
        
#%%
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(symbol):
    df = pd.read_csv("C:\\Users\\gbans6\\gbansalmba\\mlearning\\tradingML\\data\\{}.csv".format(symbol))
    df[['High', 'Adj Close']].plot()
    plt.show()
    
    
    

def test_plot():
    for symbol in ['AAPL', 'IBM']:
        plot_data(symbol)
#%%

#%%
import pandas as pd
import matplotlib.pyplot as plt
import os

print(os.getcwd())

start_date="2016-12-07"
end_date="2016-12-12"

dates = pd.date_range(start_date, end_date)
df1=pd.DataFrame(index=dates)


dfAAPL=pd.read_csv("data\\AAPL.csv",
                   index_col="Date",parse_dates=True,usecols=["Date", "Adj Close"],
                   na_values=['nan'])

df1=df1.join(dfAAPL, how="inner")
#df1= df1.dropna()
print(df1)

#%%


