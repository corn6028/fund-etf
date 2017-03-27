import mlfunc

if __name__ == '__main__':

    '''Get Fund Array'''
    FundData = mlfunc.get_fund_ndarr()
    #print(FundData)
    #print(FundData.shape)

    '''Create fund_TA table'''
    #TA per stock
    mlfunc.create_stock_table("fund","TA")

    '''TA algorithm'''
    '''----------------------Your Code----------------------'''

    '''Insert data to Table'''
    mlfunc.export_data("export.txt","fund_TA")
