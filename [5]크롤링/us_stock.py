#%%
from datetime import datetime, timedelta
import pymysql
import pandas as pd
import yfinance as yf

# 하나의 커넥션을 전역으로 공유합니다.
mysql_conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='1234', 
    database='us_stock',
    autocommit=False
)

#%%
def getCompany():
    # 1. getCompany 전용 커서 생성
    mysql_cur = mysql_conn.cursor()
    today = datetime.today() + timedelta(days=1)

    try:
        mysql_cur.execute("select symbol, company_name, ipo_year, last_crawel_date_stock from us_stock.nasdaq_company where is_delete is null;")
        results = mysql_cur.fetchall()
        
        mysql_cur.close() 
        print(f"총 {len(results)}개의 회사를 조회했습니다.")    

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

            if "." in _symbol or "/" in _symbol:
                continue
                
            print(f"진행 중인 심볼: {_symbol}")
            getStock(_symbol, _last_crawel_date_stock, today.strftime("%Y-%m-%d"))
                    
    except Exception as e:
        print("getCompany error : " + str(e))
        return {'error': str(e)}

#%%
def getStock(_symbol, _start_date, _end_date):
    stock_cur = mysql_conn.cursor()

    try:
        query = """
        delete from us_stock.stock 
        where date >= %s and date <= %s and symbol = %s;
        """
        stock_cur.execute(query, (_start_date, _end_date, _symbol))
        mysql_conn.commit()

        stock_price = yf.download(_symbol, start=_start_date, end=_end_date)
        
        if stock_price.empty:
            print(f"{_symbol} 데이터가 없습니다.")
            stock_cur.close()
            return

        # yfinance 버전에 따라 컬럼이 MultiIndex일 수 있어 1차원으로 압축
        if isinstance(stock_price.columns, pd.MultiIndex):
            stock_price.columns = stock_price.columns.get_level_values(0)

        _date, _open, _high, _low, _close, _volume = None, None, None, None, None, None

        for index, row in stock_price.iterrows():
            _date = index.strftime("%Y-%m-%d")
            _open = str(row["Open"])
            _high = str(row["High"])
            _low = str(row["Low"])
            _close = str(row["Close"])
            _volume = str(row["Volume"])
        
            stock_cur.execute(
                "insert into us_stock.stock (date, symbol, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                (_date, _symbol, _open, _high, _low, _close, _volume)
            )
        mysql_conn.commit()

        if _date is not None:
            stock_cur.execute(
                "update us_stock.nasdaq_company set open = %s, high = %s, low = %s, close = %s, volume = %s, last_crawel_date_stock = %s where symbol = %s", 
                (_open, _high, _low, _close, _volume, _date, _symbol))
            mysql_conn.commit()
            
    except Exception as e:
        print(f"getStock ({_symbol}) error : " + str(e))
        mysql_conn.rollback()
    finally:
        stock_cur.close()

#%%
if __name__ == '__main__':
    try:
        getCompany()
    finally:
        mysql_conn.close()