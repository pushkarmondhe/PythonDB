import pymysql

try:
    Prodid=input('Enter product ID ')
    Modnm=input('Enter model name ')
    cp=input('Enter Company ')
    connety=input('Enter Connectivity ')
    ram=input('Enter ram ')
    rom=input('Enter Rom ')
    clr=input('Enter color ')
    sc=input('Enter screen ')
    bt=input('Battery ')
    pr=input('Enter processer ')
    pri=int(input('Enter price '))
    rat=float(input('Enter Rating '))

    con=pymysql.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
    curs=con.cursor()
    curs.execute("insert into mobiles values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%f,'')" %(Prodid,Modnm,cp,connety,ram,rom,clr,sc,bt,pr,pri,rat))
    con.commit()
    print('New mobiles data added to cloud database')
    con.close()
except Exception as e:
    print('Error in data...cant insert',e)
