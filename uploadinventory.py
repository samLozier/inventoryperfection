def uploadinventory(filename):
    import pymysql
    import csv
    conn = pymysql.connect(host='192.168.0.40', user='phpmyadmin', passwd='2540qaan', db='inventoryperfection')

    with open(filename, encoding='utf-8', errors='ignore') as f:
        print(f)
        reader = csv.reader(f)
        sql = ("insert into inventory " 
                "(UPC,StoreID,qoh,date) "
                 "VALUES (%s,%s,%s,%s)")
        cursor = conn.cursor()
        for data in reader:
            print(data)
            cursor.execute(sql, data)
        conn.commit()
        cursor.close()