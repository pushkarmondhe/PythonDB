import pymysql as my
try: 
    con = my.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
    curs=con.cursor()

    ram=input('Enter Ram : ')
    rom=input('Enter Rom : ')
    curs.execute("select * from mobiles where ram='%s' and rom='%s'" %(ram, rom))
    data=curs.fetchall()
    if data:
        for rec in data:
            print(rec)
    else:
        print('No mobile having these ram and rom combination')
except Exception as e:
    print('Error : %s' %e)