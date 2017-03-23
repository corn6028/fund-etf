# fund-etf
## --------------------------------------------------
期間： 2011/7/4 (一) ~ 2016/9/5(一) [3000~4350]</br>
基金數：1942支</br>
ETF數：434支</br>
## --------------------------------------------------
# 基金
更改fundTA.py
</br></br></br>
# ETF
更改etfTA.py
</br></br></br>
### P.S.
#### ㄧ. TA有分市場導向跟每股導向
市場導向如RSI,ADR,ADL等</br>
每股導向如SMA,RMA等</br>
確定自己的TA屬於哪一種導向，並使用對應到的CreateTable，分別為CreateStockTable（每股）,CreateMarketTable（市場）
#### 二. TA對應到的參數
在創建好的Table裡，有一個param的欄位～
1. 如果今天是算移動平均的話，就可以用"10","20","65","130","260","520"來表示
2. 如果今天是做ETF的話，由於他欄位比基金多，也可以用param來表示，如"Open","Close","High","Low","Volume","Adj_Close"
3. 如果今天做ETF剛好又要算移動平均，就這樣表示"Open_10","Open_20","Volume_130",...
4. 其他～那就直接找我討論吧哈哈哈哈
#### 三. 把算完的結果匯入資料庫（使用函式ExportData）
需要先把算好的結果存在export.txt，在使用ExportData函式匯入資料庫</br>
export.txt格式為：</br>
1. 每股導向 : (_id)|(fund_id)|(param)|(date)|(TA_value)</br>
0|1|10|0|87.87</br>
1|1|10|1|78.78</br>
2|1|10|2|87.78</br>
3|1|10|3|94.87</br>
4|1|10|4|66.66</br>
5|1|10|5|77.77</br>
...</br>
2. 市場導向(_id)|(param)|(date)|(value)
0|Volume|0|87.87</br>
1|Volume|1|78.78</br>
2|Volume|2|87.78</br>
3|Volume|3|94.87</br>
4|Volume|4|66.66</br>
5|Volume|5|77.77</br>
...</br>
