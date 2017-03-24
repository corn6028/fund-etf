import mlfunc

if __name__ == '__main__':

    '''Get Fund Array'''
    FundData = mlfunc.get_fund_ndarr()
    #print(FundData)
    #print(FundData[1][0])

    '''Create fund_TA table'''
    #每股導向TA
    mlfunc.CreateStockTable("fund","TA")

    '''TA algorithm'''
    '''----------------------Your Code----------------------'''

    '''Insert data to Table'''
    mlfunc.ExportData("export.txt","fund_TA")
