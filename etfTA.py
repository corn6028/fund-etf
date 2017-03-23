import psycopg2
import numpy as np
import mlfunc

'''資料庫參數設定'''
hostname = '140.119.19.114'
username = 'mlstd'
password = 'iloveml'
database = 'mlclass'
port = 15432

'''Connect to Database'''
myConnection = psycopg2.connect( host=hostname, user=username, password=password, database=database, port=port )
cur = myConnection.cursor()

'''Get ETF Array(List)'''
etf = mlfunc.open_valid_file("valid_etf.txt")
start = 3000   #2011/7/4
end = 4350     #2016/9/5 
ETFData = mlfunc.get_etf_list(cur,start,end,etf)
#ETF data list to 3D ndarray
ETF_ndarr = np.array(ETFData).reshape((6,end-start+1,-1))

'''Create etf_TA table'''
#市場導向TA
mlfunc.CreateMarketTable(cur,"etf","[TA]")
#每股導向TA
mlfunc.CreateStockTable(cur,"etf","[TA]")

'''TA algorithm'''
'''----------------------Your Code----------------------'''

'''Insert data to Table'''
mlfunc.ExportData(cur,"export.txt","[table]")

