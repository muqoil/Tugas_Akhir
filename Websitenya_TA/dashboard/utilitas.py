import mysql.connector
import datetime
import serial
import os
import sshtunnel

def get_data(ser): # membaca data yang dikirimkan melalui XBEE
    incoming = ser.readline().strip()
    data = str(incoming)
    return data[2:-1]

def get_data_perdetik(connect, cursor, data): #menyimpan data perdetik ke database
    sql = """INSERT INTO dashboard_data_sensor(tanggal,curah_hujan)VALUES (%s,%s)"""
    tanggal = datetime.datetime.now()
    nilai = data
    value = tuple((tanggal, nilai))
    cursor.execute(sql, value)
    connect.commit()

def get_data_permenit(connect, cursor):
    curah_hujan_m = []
    sql = """SELECT * FROM dashboard_data_sensor
            WHERE DATE_FORMAT(tanggal, '%Y-%m-%d %H:%i') = """
    tanggal = datetime.datetime.now() - datetime.timedelta(minutes=1)
    a = "'" + str(tanggal.strftime('%Y-%m-%d %H:%M')) + "'"
    execute = sql + a
    cursor.execute(execute)
    b = cursor.fetchall()
    for c in b:
        curah_hujan.append(c[2])
    sql_m = """INSERT INTO dashboard_data_permenit(tanggal,curah_hujan)VALUES (%s,%s)"""
    value_m = tuple((tanggal,
              round(statistics.mean(curah_hujan_m))))
    cursor.execute(sql_m, value_m)
    connect.commit()

def get_data_perjam(connect, cursor):
    curah_hujan_j = []
    sql = """SELECT * FROM dashboard_data_permenit
            WHERE DATE_FORMAT(tanggal, '%Y-%m-%d %H') = """
    tanggal = datetime.datetime.now() - datetime.timedelta(hours=1)
    a = "'" + str(tanggal.strftime('%Y-%m-%d %H')) + "'"
    execute = sql + a
    cursor.execute(execute)
    b = cursor.fetchall()
    for c in b:
        curah_hujan.append(c[2])
    sql_j = """INSERT INTO dashboard_data_perjam(tanggal,curah_hujan)VALUES (%s,%s)"""
    value_j = tuple((tanggal,
              round(statistics.mean(curah_hujan_j), 2)))
    cursor.execute(sql_j, value_j)
    connect.commit()

def get_data_perhari(connect, cursor):
    curah_hujan_h = []
    sql = """SELECT * FROM dashboard_data_perjam
            WHERE DATE_FORMAT(tanggal, '%Y-%m-%d') = """
    tanggal = datetime.datetime.now() - datetime.timedelta(days=1)
    a = "'" + str(tanggal.strftime('%Y-%m-%d')) + "'"
    execute = sql + a
    cursor.execute(execute)
    b = cursor.fetchall()
    for c in b:
        curah_hujan.append(c[2])
    sql_h = """INSERT INTO dashboard_data_perhari(tanggal,curah_hujan)VALUES (%s,%s)"""
    value_h = tuple((tanggal,
              round(statistics.mean(curah_hujan_h), 2)))
    cursor.execute(sql_h, value_h)
    connect.commit()

if __name__ == '__main__':
    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com',22),
        ssh_username='muqoil17',
        ssh_password='MuQ0!l...',
        remote_bind_address=('muqoil17.mysql.pythonanywhere-services.com',3306)
    ) as tunnel:
        connection = mysql.connector.connect(
            user='muqoil17',
            password='MuQ0!l...',
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            database='muqoil17$ujicoba')

    # connect = mysql.connector.connect(
    #         user='muqoil17',
    #         password='MuQ0!l...',
    #         host='muqoil17.mysql.pythonanywhere-services.com',
    #         database='muqoil17$ujicoba'
    #         )
    # connect = MySQLdb.connect('muqoil17.mysql.pythonanywhere-services.com', 'MuQ0!l...', 'muqoil17', 'muqoil17$ujicoba')
    cursor = connect.cursor()
    print("Success")
    ser = serial.Serial(port='COM6', baudrate=9600, timeout=1.5)
    count_d = 0
    count_m = 0
    count_j = 0
    count_h = 0
    while True:
        data = get_data(ser)
        for a in range(24):
            for b in range(60):
                for c in range(60):
                    get_data_perdetik(connect, cursor, data)
                    count_d += 1
                    if count_d == 60:
                        count_d = 0
                    print(count_h, count_j, count_m, count_d)
                get_data_permenit(connect, cursor)
                count_m += 1
                if count_m == 60:
                    count_m = 0
            get_data_perjam(connect, cursor)
            count_j += 1
            if count_j == 24:
                count_j = 0
        get_data_perhari(connect, cursor)
        count_h += 1
