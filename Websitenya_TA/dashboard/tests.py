from django.test import TestCase

# Create your tests here.
import sqlite3
import datetime
import time
import random
import statistics



def input_data():
    connect = sqlite3.connect("D:\Penting\db.sqlite3")
    cursor = connect.cursor()
    count = 1
    count_m = 1
    count_j = 1
    data_detik = []
    data_menit = []
    data_jam = []
    while True:
        a = datetime.datetime.now()
        value = random.choice([1,2,3,4,5,6,7,8,9,10])
        b = """INSERT INTO data_input (ID, tanggal, senosr_1) VALUES ({count},{tanggal},{value})"""
        e = b.format(count=count, tanggal='"' + str(a) + '"', value=value)
        cursor.execute(e)
        count += 1
        if len(data_detik) < 60 :
            data_detik.append(value)
            print(count)
        else:
            c = statistics.mean(data_detik)
            d = """INSERT INTO data_permenit (ID, Tanggal, Sensor_1) VALUES ({count},{tanggal},{value})"""
            f = d.format(count=count_m, tanggal='"' + str(a) + '"', value=c)
            cursor.execute(f)
            count_m += 1
            data_detik = []
            if len(data_menit) < 60:
                data_menit.append(c)
                print(count, count_m)
            else:
                g = statistics.mean(data_menit)
                h = """INSERT INTO data_perjam (ID, tanggal, Sensor_1) VALUES ({count},{tanggal},{value})"""
                i = h.format(count=count_j, tanggal='"' + str(a) + '"', value=g)
                cursor.execute(i)
                count_j += 1
                data_menit = []
                if len(data_jam) < 24:
                    data_jam.append(g)
                    print(count, count_m, count_j)
                else:
                    print("selesaimi 1 hari")
        time.sleep(.1)
input_data()