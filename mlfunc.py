from dateutil import rrule
from datetime import date
import psycopg2
import numpy as np

args = {
    'host': '140.119.19.114',
    'user': 'mlstd',
    'password': 'iloveml',
    'database': 'mlclass',
    'port': 15432
}
conn = psycopg2.connect(**args)

start = 3000   #2011/7/4
end = 4350     #2016/9/5 

def day_check():
    working_days = rrule.rrule(rrule.DAILY, byweekday=range(0, 5), dtstart=date(2000,1,1), until=date(2020,12,31))
    working_days = [day.strftime("%Y-%m-%d") for day in working_days]
    return working_days


def get_fund_ndarr():
    fund = open_valid_file("valid_fund.txt")
    fund_li = ["'"+name+"'" for name in fund]
    date_li = [i+start for i in range(end-start+1)]
    with conn.cursor() as cur:
        cur.execute('SELECT net_worth FROM fund_net_worth_perday '
                    'WHERE fund_id in (%s) AND date in (%s)  order by _id '
                    %(",".join(fund_li),",".join(str(e) for e in date_li))
                   )
        fund_ndarr = np.array(cur.fetchall()).reshape((-1,end-start+1))
    return fund_ndarr


def get_etf_ndarr():
    etf = open_valid_file("valid_etf.txt")
    etf_li = ["'"+name+"'" for name in etf]
    date_li = [i+start for i in range(end-start+1)]
    with conn.cursor() as cur:
        cur.execute('SELECT open,high,low,close,volume,adj_close FROM etf_data '
                    'WHERE etf_id in (%s) AND date in (%s)  order by _id '
                    %(",".join(etf_li),",".join(str(e) for e in date_li))
                   )
        etf_ndarr = np.array(cur.fetchall()).reshape((-1,end-start+1,6))
    return etf_ndarr


def open_valid_file(filename):
    with open(filename,"r") as f:
        valid_li = [line.strip() for line in f]
        return valid_li


def create_stock_table(ftype,TA):
    with conn.cursor() as cur:
        cur.execute('CREATE TABLE {}_{} ('
                        '_id INTEGER,'
                        'fund_id INTEGER,'
                        'param VARCHAR,'
                        'date INTEGER,'
                        '{} FLOAT)'.format(ftype,TA,TA))    
    conn.commit()


def create_market_table(ftype,TA):
    with conn.cursor() as cur:
        cur.execute('CREATE TABLE {}_{} ('
                        '_id INTEGER,'
                        'param VARCHAR,'
                        'date INTEGER,'
                        '{} FLOAT)'.format(ftype,TA,TA))
    conn.commit()


def drop_table(table):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE {}".format(table))    
    

def load_data(table):
    with conn.cursor() as cur:    
        cur.execute("SELECT * FROM {} ORDER BY _id ".format(table))
        return cur.fetchall()


def export_data(fname,table):
    f = open(fname, 'r')
    with conn.cursor() as cur:
        cur.copy_from(f, table, sep="|")
    conn.commit()
    f.close()
 
