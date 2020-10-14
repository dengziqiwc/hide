from django.shortcuts import render,HttpResponse
# 引入JsonResponse模块
from django.http import JsonResponse
# Create your views here.

import pymysql
import xlwt
from io import BytesIO
from django.shortcuts import HttpResponse
# 引入处理Excel模块
import openpyxl
# 导入uuid类
import uuid
# 导入哈希库
import hashlib
import os
# 导入Setting
from django.conf import settings
from app01 import models
from pymysql.cursors import DictCursor

def export_xls_out(request):
    conn =pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='day11',port=3306,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
#数据库参数自己配置
    sql='select * from app01_device'
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()#获取查询结果
    print(result)
    response = HttpResponse(content_type='application/vnd.ms-excel')#指定返回为excel文件
    response['Content-Disposition'] = 'attachment;filename=test.xls'#指定返回文件名
    wb = xlwt.Workbook(encoding = 'utf-8')#设定编码类型为utf8
    sheet = wb.add_sheet(u'表格')#excel里添加类别
    sheet.write(0,0,'id')
    sheet.write(0,1,'devicename')
    sheet.write(0,2,'devicesecret')
    sheet.write(0,3,'productname')

    row = 1
    for list in result:
        sheet.write(row,0, list['id'])
        sheet.write(row,1, list['devicename'])
        sheet.write(row,2, list['devicesecret'])
        sheet.write(row,3, list['productname_id'])
        row=row + 1

    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response

def page(request):
    return render(request,'page.html')


def get_random_str():
    #获取uuid的随机数
    uuid_val = uuid.uuid4()
    #获取uuid的随机数字符串
    uuid_str = str(uuid_val).encode('utf-8')
    #获取md5实例
    md5 = hashlib.md5()
    #拿取uuid的md5摘要
    md5.update(uuid_str)
    #返回固定长度的字符串
    return md5.hexdigest()

def export_student_excel(request):
    """到处数据到excel"""
    # 获取所有的学生信息
    obj_students = models.TT.objects.all().values()

    # 转为List
    students = list(obj_students)
    # 准备名称
    excel_name = get_random_str() + ".xlsx"
    # 准备写入的路劲
    path = os.path.join(settings.MEDIA_ROOT, excel_name)
    # 写入到Excel
    write_to_excel(students, path)
    # 返回
    return JsonResponse({'code':1, 'name':excel_name })


def write_to_excel(data:list, path:str):
    """把数据库写入到Excel"""
    # 实例化一个workbook
    workbook = openpyxl.Workbook()
    # 激活一个sheet
    sheet = workbook.active
    # 为sheet命名
    sheet.title = 'student'
    # 准备keys
    keys = data[0].keys()
    # 准备写入数据
    for index, item in enumerate(data):
        # 遍历每一个元素
        for k,v in enumerate(keys):
            sheet.cell(row=index + 1, column=k+ 1, value=str(item[v]))
    # 写入到文件
    workbook.save(path)
import json
def query_devices(request):
    def query_students(request):
        """查询设备信息"""
        # 接收传递过来的查询条件--- axios默认是json --- 字典类型（'inputstr'）-- data['inputstr']
        data = json.loads(request.body.decode('utf-8'))
        try:
            # 使用ORM获取满足条件的学生信息 并把对象转为字典格式
            obj_devices = models.TT.objects.values()
            # 把外层的容器转为List
            devices = list(obj_devices)
            # 返回
            return JsonResponse({'code': 1, 'data': devices})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "查询学生信息出现异常，具体错误：" + str(e)})

def deviceshow(request):
    # device_data = models.Device.objects.values_list('devicename','devicesecret','productname')
    # return render(request,'deviceshow.html',{'device_data':device_data})
    """获取所有设备的信息"""
    try:
        device_data = models.Device.objects.values('pk','devicename','devicesecret','productname')
        # 把外层的容器转为List
        devices= list(device_data)
        # 返回
        return JsonResponse({'code':1, 'data':devices})
    except Exception as e:
        # 如果出现异常，返回
        return JsonResponse({'code': 0, 'msg': "获取设备信息出现异常，具体错误：" + str(e)})

def productshow(request):
    # product_data = models.Product.objects.values('productname','productkey','productsecret')
    # # 把外层的容器转为List
    # products = list(product_data)
    """获取所有产品的信息"""
    try:
        product_data = models.Product.objects.values('productname', 'productkey', 'productsecret')
        # 把外层的容器转为List
        products = list(product_data)
        # 返回
        return JsonResponse({'code':1, 'data':products})
    except Exception as e:
        # 如果出现异常，返回
        return JsonResponse({'code': 0, 'msg': "获取设产品信息出现异常，具体错误：" + str(e)})

import datetime
def changtime(oldtime):

    oldtime = oldtime.rsplit('.',maxsplit=1)[0]
    newtime = oldtime.replace('T',' ')
    utc_date = datetime.datetime.strptime(newtime, "%Y-%m-%d %H:%M:%S")
    local_date = utc_date + datetime.timedelta(hours=8)
    local_date_str = datetime.datetime.strftime(local_date, '%Y-%m-%d %H:%M:%S')
    # print(local_date_str)  # 2019-07-26 16:20:54

    dateTime_p = datetime.datetime.strptime(local_date_str, '%Y-%m-%d %H:%M:%S')
    print(dateTime_p)  # 2019-01-30 15:29:08
    return dateTime_p

# UTC 转换为 格式化的时间字符串
# def u2s(origin_date_str):
#     utc_date = datetime.datetime.strptime(origin_date_str, "%Y-%m-%d %H:%M:%S")
#     local_date = utc_date + datetime.timedelta(hours=8)
#     local_date_str = datetime.datetime.strftime(local_date, '%Y-%m-%d %H:%M:%S')
#     print(local_date_str)  # 2019-07-26 16:20:54
#     return local_date_str

#查数据
def querydevicedata(request):
    data = request.body.decode('utf-8')
    data = eval(data)
    print(data,type(data))
    pid = data.get('id')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    end_time = changtime(end_time)
    start_time = changtime(start_time)

    print(start_time,end_time)
    print(type(start_time),type(end_time))
    return HttpResponse('123')