def uploadinventory(filename):
    import pymysql
    import csv
    import config as cfg
    conn = pymysql.connect(cfg.database_Config['host'],
                           cfg.database_Config['user'],
                           cfg.database_Config['password'],
                           cfg.database_Config['dbname'])


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