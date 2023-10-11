from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as mysql

def scan(request):
    inp = ""
    try:
        if request.method == "POST":
            inp = (request.POST['details'])
        with open('logic.txt','w') as wr:
            wrr = wr.write(inp)
            
        with open('logic.txt','r') as f:
            lines = f.read().strip('\n')
        print(lines)
        arr = []

        l1 = lines.split(':')
        print(l1)
        
        for x in l1:
            arr.append(x)
            #print(x)
        #print(arr)
        URN = (arr[0])
        NAME = (arr[1])
        DESIGNATION =(arr[2])        
        COMPANY = arr[3] 
        CITY = (arr[4])
        STATE = (arr[5])
        COUNTRY = (arr[6])
        CONTACT = (arr[8])
        EMAIL = (arr[7])
        cont = int(CONTACT)
        print(type(cont))

    #def excel(self):
        tab = []
        
        tab.append(URN)
        tab.append(NAME)
        tab.append(DESIGNATION)
        tab.append(COMPANY)
        tab.append(STATE)
        tab.append(CITY)
        tab.append(COUNTRY)
        tab.append(CONTACT)
        tab.append(EMAIL)
        import csv
        import numpy as np
        exce = np.asarray(tab)
        with open ('Report.csv','a',newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(exce)

        conn = mysql.connect(host="localhost",user="root",password="")
        cur = conn.cursor()
        cur.execute("use qrscan")
        sql = "insert into details(urn,name,designation,company,state,city,country,email,contact) values ('"+URN+"','"+NAME+"','"+DESIGNATION+"','"+COMPANY+"','"+STATE+"','"+CITY+"','"+COUNTRY+"','"+EMAIL+"','"+CONTACT+"')"
        cur.execute(sql)
        conn.commit()

    except:
        print("INVALID")
    return render(request,"scan.html",{"ump":inp})


"""
obj = Event()
obj.inpp()
obj.gen()
obj.excel()
obj.sql()
"""
