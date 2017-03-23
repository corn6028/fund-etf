from dateutil import rrule
from datetime import date

def day_Check():
    working_days = rrule.rrule(rrule.DAILY, byweekday=range(0, 5), dtstart=date(2000,1,1), until=date(2020,12,31))
    working_days = [day.strftime("%Y-%m-%d") for day in working_days]
    return working_days

def get_fund_list(cur,start,end,fund_li):
    fund_li = ["'"+name+"'" for name in fund_li]
    date_li = [i+start for i in range(end-start+1)]
    cur.execute('SELECT net_worth FROM fund_net_worth_perday '
                'WHERE fund_id in (%s) AND date in (%s)  order by _id '
                %(",".join(fund_li),",".join(str(e) for e in date_li))
               )
    return cur.fetchall()

def get_etf_list(cur,start,end,etf_li):
    etf_li = ["'"+name+"'" for name in etf_li]
    date_li = [i+start for i in range(end-start+1)]
    cur.execute('SELECT open,high,low,close,volume,adj_close FROM etf_data '
                'WHERE etf_id in (%s) AND date in (%s)  order by _id '
                %(",".join(etf_li),",".join(str(e) for e in date_li))
               )
    return cur.fetchall()

def open_valid_file(filename):
    with open(filename,"r") as f:
        valid_li = [line.strip() for line in f]
        return valid_li

def CreateStockTable(cur,ftype,TA):
    cur.execute('CREATE TABLE {}_{} ('
                        '_id INTEGER,'
                        'fund_id INTEGER,'
			'param STRING,'
                        'date INTEGER,'
                        '{} FLOAT)'.format(ftype,TA,TA))    

def CreateMarketTable(cur,ftype,TA):
    cur.execute('CREATE TABLE {}_{} ('
                        '_id INTEGER,'
                        'param STRING,'
                        'date INTEGER,'
                        '{} FLOAT)'.format(ftype,TA,TA))

def DropTable(cur,table):
    cur.execute("DROP TABLE {}".format(table))    
    
def LoadData(cur,table):
    cur.execute("SELECT * FROM {} ORDER BY _id ".format(table))
    return cur.fetchall()

def ExportData(cur,fname,table):
    f = open(fname, 'r')
    cur.copy_from(f, table, sep="|")
    f.close() 
