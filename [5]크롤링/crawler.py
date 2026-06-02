#%%

from datetime import datetime, timedelta

import pymysql
import pandas as pd
import yfinance as yf





mysql_conn = pymysql.connect(host='localhost', user='root', password='1234', db='us_stock')


#%%
def getCompany():
    
    mysql_cur = mysql_conn.cursor()

    today = datetime.today() + timedelta(days=1)

    try:
        mysql_cur.execute("select symbol, company_name, ipo_year, last_crawel_date_stock from us_stock.nasdaq_company where is_delete is null;")
        results = mysql_cur.fetchall()
        print(results)    
        

        for row in results:
            _symbol = row[0]
            _company_name = row[1]
            
            if row[2] is None or row[2] == 0:
                _ipo_year = '1970'
            else:
                _ipo_year = row[2]
            
            if row[3] is None:
                _last_crawel_date_stock = str(_ipo_year) + '-01-01'
            else:
                _last_crawel_date_stock = row[3]

            print (_symbol)
            if "." in _symbol:
                print(_symbol)
            else:
                if "/" in _symbol:
                    print(_symbol)
                else:
                    getStock(_symbol, _last_crawel_date_stock, today.strftime("%Y-%m-%d"))
                    
                    
    except Exception as e:
        print ("error : " + str(e))
        mysql_conn.commit()
        mysql_conn.close()
        
        return {'error': str(e)}
    


#%%
mysql_cur = mysql_conn.cursor()

_start_date = '2026-01-01'
_end_date = '2026-12-31'
_symbol = 'AMD'

query = """
delete from us_stock.stock
where date >= %s and date <= %s and symbol = %s;
"""
mysql_cur.execute(query=query, args=(_start_date, _end_date, _symbol))
mysql_conn.commit()

#%%
#yf.download already returns a DataFrame.
stock_price = yf.download(_symbol, start=_start_date, end=_end_date)

#%%
import datetime
#명시적 형변환...
d = datetime.datetime.strptime('2026-04-23', '%Y-%m-%d')
stock_price.loc[d, :]
#근데 묵시적 형변환 가능
stock_price.loc['2026-04-23', :]

#%%
# 각 행을 반복문으로 가져오기
data_list = []
for index, row in stock_price.iterrows():
    _date = index.strftime("%Y-%m-%d") # datetime -> str
    _open = str(row["Open", _symbol])
    _high = str(row["High", _symbol])
    _low = str(row["Low", _symbol])
    _close = str(row["Close", _symbol])
    _volume = str(row["Volume", _symbol])

    query = """insert into us_stock.stock 
    (date, symbol, open, high, low, close, volume)
      VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    
    # mysql_cur.execute(query, (_date, _symbol, _open, _high, _low, _close, _volume))
    data = (_date, _symbol, _open, _high, _low, _close, _volume)
    data_list.append(data)

# 효율을 생각하면 executemany 를 추천!
mysql_cur.executemany(query, data_list)
mysql_conn.commit()

#%%
try:
 
    
    

    
    mysql_cur.execute("update us_stock.nasdaq_company set open = %s, high = %s, low = %s, close = %s, adj_close = %s, volume = %s, last_crawel_date_stock = %s where symbol = %s", (_open, _high, _low, _close,  _volume, _date, _symbol))
    mysql_conn.commit()
    
except Exception as e:
    print ("error : " + str(e))
    mysql_conn.commit()
    mysql_conn.close()
    
    # return {'error': str(e)}

#%%
if __name__ == '__main__':
# execute only if run as a script
    getCompany()