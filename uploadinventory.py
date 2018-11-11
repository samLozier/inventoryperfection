def uploadinventory(filename):
    import pymysql
    import csv
    conn = pymysql.connect(host='192.168.0.40', user='phpmyadmin', passwd='2540qaan', db='inventoryperfection')
    cursor = conn.cursor()
    csv_data = csv.reader(filename)

    for row in csv_data:
        cursor.execute('INSERT INTO inventory(names, \
                  classes, mark )' \
                       'VALUES("%s", "%s", "%s")',
                       row)
        # close the connection to the database.
    cursor.close()
    print
    "Done"