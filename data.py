import bs4 as bs
import urllib.request
import string
import MySQLdb

def getData():
	url = urllib.request.urlopen('https://nepse-data-api.herokuapp.com/data/todaysprice').read()

	scrapped_data = bs.BeautifulSoup(url, 'lxml')
	data = scrapped_data.getText()

	for c in string.punctuation:
		if(c=='['or c==']' or c=='{' or c=='}' or c=='"'):
			data= data.replace(c,"")

	datalist = data.split(',')
	new_datalist=[]

	for i in range(len(datalist)):
		new_datalist.append(datalist[i].split(':'))

	data_dict={}

	for j in range(len(new_datalist)):
		temp = new_datalist[j]
		if temp[0] in data_dict:
			data_dict[temp[0]].append(temp[1])
		else:
			data_dict[temp[0]]=[temp[1]]

	return data_dict


def insertToDatabase():
	conn = MySQLdb.connect(host = "localhost", 
	                           user = "root", 
	                           passwd = "", 
	                           db = "stockmarket")
	x = conn.cursor() 

	names=list(getData().values())[0]
	transactions=list(getData().values())[1]
	max_price=list(getData().values())[2]
	min_price=list(getData().values())[3]
	closing_price=list(getData().values())[4]
	traded_shares=list(getData().values())[5]
	amount_val=list(getData().values())[6]
	previous_closing=list(getData().values())[7]
	difference_val=list(getData().values())[8]
	alias=[]

	for no in range(len(names)):
		words = names[no].split()
		letters = [word[0] for word in words]
		a = "".join(letters)
		alias.append(a)

	for no in range(len(names)):
		for c in string.punctuation:
			if(c=='('):
				alias[no]= alias[no].replace(c,"")

	for no in range(len(names)):
		x.execute("""INSERT INTO stock_exchange_day14 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(alias[no],names[no],transactions[no],max_price[no],min_price[no],closing_price[no],traded_shares[no],amount_val[no],previous_closing[no],difference_val[no]))
		conn.commit()

	conn.close()

insertToDatabase()
