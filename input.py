import pandas as pd
import numpy as np
import scipy
import MySQLdb

conn = MySQLdb.connect(host = "localhost", 
                                   user = "root", 
                                   passwd = "", 
                                   db = "stockmarket")

sql = ("select count(*) from information_schema.tables where table_schema = 'stockmarket'")
df = pd.read_sql(sql, conn)
tables_no = df.loc[:,"count(*)"]

diff = []
closing = []
maxdiff = []
mindiff = []
amountdiff = []
sharesdiff = []
transdiff = []


def get_traindata(val):
    
    for i in range(2,tables_no[0]-2):
        j=i-1
        a="stock_exchange_day" + str(i)
        b="stock_exchange_day" + str(j)
        sql1 = ("""SELECT companyAlias,difference,maxPrice,minPrice,amount,tradedShares,noOfTransactions FROM """+b)
        sql2 = ("""SELECT companyAlias,difference,maxPrice,minPrice,amount,tradedShares,noOfTransactions FROM """+a)
    
        df1 = pd.read_sql(sql1, conn)
        df2 = pd.read_sql(sql2, conn)
        
        alias = df1.loc[:, "companyAlias"]
    
        for g in range(0, len(alias)):
            if(alias[g] == val):
                diff1 = df2.loc[:,"difference"]
            
                maxprice1 = df1.loc[:,"maxPrice"]
                maxprice2 = df2.loc[:,"maxPrice"]
                
                minprice1 = df1.loc[:,"minPrice"]
                minprice2 = df2.loc[:,"minPrice"]
                
                amount1 = df1.loc[:,"amount"]
                amount2 = df2.loc[:,"amount"]
                
                shares1 = df1.loc[:,"tradedShares"]
                shares2 = df2.loc[:,"tradedShares"]
                
                trans1 = df1.loc[:,"noOfTransactions"]
                trans2 = df2.loc[:,"noOfTransactions"]
                
                diff.append(float(diff1[g]))
                
                maxdiff.append(float(maxprice2[g]) - float(maxprice1[g]))
                
                mindiff.append(float(minprice2[g]) - float(minprice1[g]))
                
                amountdiff.append(float(amount2[g]) - float(amount1[g]))
                
                sharesdiff.append(float(shares2[g]) - float(shares1[g]))
                
                transdiff.append(float(trans2[g]) - float(trans1[g]))
                
    val=[]
    
    for a in range(1,len(diff)):
        b=a-1
        fval = [[int(float(diff[b])),int(float(maxdiff[b])),int(float(mindiff[b])),int(float(amountdiff[b])),int(float(sharesdiff[b])),int(float(transdiff[b]))]]        
        temp = [[int(float(diff[a])),int(float(maxdiff[a])),int(float(mindiff[a])),int(float(amountdiff[a])),int(float(sharesdiff[a])),int(float(transdiff[a]))]]
        val.append(np.concatenate((fval, temp), axis=0))
    
    p= np.concatenate(val,axis=0)
    p = scipy.sparse.csr_matrix(p)
    p = p.todense()
    
    return p

def get_testdata(val):
    j = tables_no[0]-2
    a = "stock_exchange_day" + str(tables_no[0]-1)
    b = "stock_exchange_day" + str(j)
    sql1 = ("""SELECT companyAlias,difference,maxPrice,minPrice,amount,tradedShares,noOfTransactions FROM """+b)
    sql2 = ("""SELECT companyAlias,difference,maxPrice,minPrice,amount,tradedShares,noOfTransactions FROM """+a)

    df1 = pd.read_sql(sql1, conn)
    df2 = pd.read_sql(sql2, conn)
    
    alias = df1.loc[:, "companyAlias"]

    for g in range(0, len(alias)):
        if(alias[g] == val):
            diff1 = df2.loc[:,"difference"]
        
            maxprice1 = df1.loc[:,"maxPrice"]
            maxprice2 = df2.loc[:,"maxPrice"]
            
            minprice1 = df1.loc[:,"minPrice"]
            minprice2 = df2.loc[:,"minPrice"]
            
            amount1 = df1.loc[:,"amount"]
            amount2 = df2.loc[:,"amount"]
            
            shares1 = df1.loc[:,"tradedShares"]
            shares2 = df2.loc[:,"tradedShares"]
            
            trans1 = df1.loc[:,"noOfTransactions"]
            trans2 = df2.loc[:,"noOfTransactions"]
            
            diff.append(float(diff1[g]))
            
            maxdiff.append(float(maxprice2[g]) - float(maxprice1[g]))
            
            mindiff.append(float(minprice2[g]) - float(minprice1[g]))
            
            amountdiff.append(float(amount2[g]) - float(amount1[g]))
            
            sharesdiff.append(float(shares2[g]) - float(shares1[g]))
            
            transdiff.append(float(trans2[g]) - float(trans1[g]))
    
    val = [[int(float(diff[0])),int(float(maxdiff[0])),int(float(mindiff[0])),int(float(amountdiff[0])),int(float(sharesdiff[0])),int(float(transdiff[0]))]]        
    
    test = np.concatenate(val,axis=0)
    test = scipy.sparse.csr_matrix(test)
    test = test.todense()

    return test

def get_accdata(val):
    j = tables_no[0]
    b = "stock_exchange_day" + str(j)
    sql1 = ("""SELECT companyAlias,closingPrice,maxPrice,minPrice,amount,tradedShares,noOfTransactions FROM """+b)

    df1 = pd.read_sql(sql1, conn)
    
    alias = df1.loc[:, "companyAlias"]

    for g in range(0, len(alias)):
        if(alias[g] == val):
            closingprice = df1.loc[:,"closingPrice"]
        
            maxprice = df1.loc[:,"maxPrice"]
                        
            minprice = df1.loc[:,"minPrice"]
            
            amount = df1.loc[:,"amount"]
            
            shares = df1.loc[:,"tradedShares"]
            
            trans = df1.loc[:,"noOfTransactions"]
            
            closing = (float(closingprice[g]))
            
            maxdiff = (float(maxprice[g]))
            
            mindiff = (float(minprice[g]))
            
            amountdiff = (float(amount[g]))
            
            sharesdiff = (float(shares[g]))
            
            transdiff = (float(trans[g]))
    
    acc = [closing, maxdiff,mindiff,amountdiff,sharesdiff,transdiff]        

    return acc


def get_value(val):  
    a = "stock_exchange_day" + str(tables_no[0])
    sql1 = ("""SELECT companyAlias,companyName,closingPrice,maxPrice,minPrice,amount,tradedShares,noOfTransactions FROM """+a)
    
    df1 = pd.read_sql(sql1, conn)
    
    alias = df1.loc[:, "companyAlias"]
    name = df1.loc[:, "companyName"]
    closingprice = df1.loc[:, "closingPrice"]
    maxprice = df1.loc[:, "maxPrice"]
    minprice = df1.loc[:, "minPrice"]
    amount = df1.loc[:, "amount"]
    tradedShares = df1.loc[:, "tradedShares"]
    noOfTrans = df1.loc[:, "noOfTransactions"]

    
    for g in range(0, len(alias)):
        if(alias[g] == val):
            values = [alias[g],name[g],float(closingprice[g]),float(maxprice[g]),float(minprice[g]),float(amount[g]),float(tradedShares[g]),float(noOfTrans[g])]    
    
    return values

def get_alias():
    a = "stock_exchange_day" + str(tables_no[0])
    sql1 = ("""SELECT companyAlias,companyName FROM """+a)
    
    df1 = pd.read_sql(sql1, conn)
    
    alias = df1.loc[:, "companyAlias"]
    name = df1.loc[:, "companyName"]

    
    values = [alias,name]
    
    
    
    return values
#print(get_traindata())

#print(tables_no[0]-1)