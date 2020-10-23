import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s1.settings")
    import django
    django.setup()
    from app01 import models
    # ob_list = []

    # for i in range(10):
    #     ob_list.append(models.Test2(device_name='cc'+str(i),event_time=i,product_key_id='sdsadsadsa',CurrentTemperature=i,CurrentHumidity=i,event_date='2020-1-12'))
    # # models.Test2.objects.bulk_create(ob_list)
    # # print(models.Test2.objects.filter(event_time__lt=2019-1-12))
    # dd = models.Test2.objects.last()
    # print(dd.id)
    import datetime
    s = datetime.datetime.now()
    print(type(s),s)
    # import time
    # for i in range(1000):
    #     models.Test2.objects.create(device_name='cc'+str(i),event_time=i,product_key_id='sdsadsadsa',CurrentTemperature=i,CurrentHumidity=i+1,event_date='2020-10-14 5:22:33')
    #     time.sleep(2)

    # models.Test2.objects.all().delete()
    import pymysql
    from pymysql.cursors import DictCursor
    # conn=pymysql.connect(host='192.168.1.114',user='root',password='654321',database='day1',charset='utf-8')
    conn = pymysql.connect(host='192.168.1.114', user='root', passwd='654321', db='day1', port=3306, charset='utf8')
    cursor = conn.cursor(DictCursor)
    sql ="select * from app01_hh where t0_time_before<'2020-10-16 09:51:41'"
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(type(res),res)


