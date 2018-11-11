# connect to database
def database():

    import pymysql


    #connect to the database
    conn = pymysql.connect(host='192.168.0.40', user='phpmyadmin', passwd='2540qaan', db = 'inventoryperfection')



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


