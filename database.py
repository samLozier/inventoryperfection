# connect to database
def database():
    import pymysql
    import config as cfg
    conn = pymysql.connect(cfg.database_Config['host'],
                           cfg.database_Config['user'],
                           cfg.database_Config['password'],
                           cfg.database_Config['dbname'])


    try:
        with conn.cursor() as cursor:
            sql = "select inventorylocation from stores"
            cursor.execute(sql)
            result = cursor.fetchall()
            finalresult = list(sum(result, ()))  #converts output to list
        print(finalresult)
    finally:
        conn.close()
    return finalresult


