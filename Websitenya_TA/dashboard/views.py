from django.shortcuts import render
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from dashboard.models import *
import time
import sqlite3
import datetime
# Create your views here.


def index(request):
    while True:
        data = Data_sensor.objects.latest('id')
        return render(request, 'index.html', {'data': data})


def index1(request):
    return render(request, 'index1.html')


def data_pengukuran(request):
    return render(request, 'data_pengukuran.html')


def daftar_sensor(request):
    sensor = Daftar_sensor.objects.all()
    return render(request, "daftar_sensor.html", {'sensor': sensor})


def get_data_sensor(request):
    def event_get():
        while True:
            data = Data_sensor.objects.latest('id')
            datanya = [data.curah_hujan,
                       data.intensitas_cahaya,
                       data.ketinggian_air,
                       data.ph,
                       data.salinitas,
                       data.suhu]
            kirim = ''
            for i in datanya:
                kirim += str(i) + ","
            time.sleep(1)
            yield 'data: %s\n\n' % kirim
    return StreamingHttpResponse(event_get(), content_type='text/event-stream')


def ajax_posting(request):
    if request.is_ajax():
        dari = request.POST.get('Dari', None)
        sampai = request.POST.get('Sampai', None)
        rentang = request.POST.get('Rentang', None)
        dari = dari.replace("T", " ")
        sampai = sampai.replace("T", " ")
        data_didapat = get_data(dari, sampai, rentang)
        if dari and sampai and rentang:
            response = {
                         'pesan': data_didapat,
            }
            return JsonResponse(response)  # return response as JSON
        else:
            response = {
                         'alert': "Harap Isi Semua Form"
            }
            return JsonResponse(response)  # return response as JSON


def get_data(dari, sampai, rentang):
    connect = sqlite3.connect("D:\Penting\Websitenya_TA\db.sqlite3")
    cursor = connect.cursor()
    delta = datetime.timedelta(minutes=int(rentang))
    a = datetime.datetime.strptime(dari, '%Y-%m-%d %H:%M')
    b = datetime.datetime.strptime(sampai, '%Y-%m-%d %H:%M')
    c = a + delta
    data = []
    while str(c) < str(b):
        if len(data) < 2:
            d = """SELECT tanggal, avg(curah_hujan), avg(suhu), avg(intensitas_cahaya), avg(ph), avg(salinitas), 
                avg(ketinggian_air) FROM dashboard_data_sensor WHERE strftime('%Y-%m-%d %H:%M',tanggal) = {waktu}"""
            e = d.format(waktu='"' + str(c) + '"')
            cursor.execute(e)
            data.append(cursor.fetchall())
            for f in data:
                if f[0][1] == None:
                    data.pop()
                else:
                    pass
        else:
            break
    print(data)
    return data