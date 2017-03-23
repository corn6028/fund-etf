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

'''Get fund Array(List)'''
fund = mlfunc.open_valid_file("valid_fund.txt")
start = 3000   #2011/7/4
end = 4350     #2016/9/5 
FundData = mlfunc.get_fund_list(cur,start,end,fund)
#fund data list to 2D ndarray
fund_ndarr = np.array(FundData).reshape((end-start+1,-1))

'''Create fund_TA table'''
#市場導向TA
mlfunc.CreateMarketTable(cur,"fund","[TA]")
#每股導向TA
mlfunc.CreateStockTable(cur,"fund","[TA]")

'''TA algorithm'''
'''----------------------Your Code----------------------'''

'''Insert data to Table'''
mlfunc.ExportData(cur,"export.txt","[table]")

