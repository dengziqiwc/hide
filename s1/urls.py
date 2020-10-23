"""s1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from app01 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    # path(r'test/', views.export_xls_out),
    # path(r'page/', views.page),
    #创建用户
    path(r'api/account/create',views.accountcreate),

    #创建产品
    path(r'api/product/create',views.productcreate),
    #获取所有的产品
    path(r'api/product/all',views.productall),

    #创建设备
    path(r'api/device/create',views.devicecreate),
    # 导出Excel文件
    path(r'excel/export/<str:typee>', views.export_student_excel),
    #同时导出多个excel
    path(r'api/exportmany/', views.export_xls_many),
    path(r'currentdevice/query/', views.query_devices),
    #返回所有的设备及其信息
    path(r'api/productshow/', views.productshow),
    path(r'api/deviceshow/', views.deviceshow),
    #按条件查询设备数据
    path(r'api/querydevicedata/humidity', views.querydevicehumidity),
    path(r'api/querydevicedata/temperature', views.querydevicetemperature),

    #获取当前的湿度
    path(r'api/getcurrenth/<str:productname>/<str:devicename>/',views.getcurrenth),
    #获取当前的湿度
    path(r'api/getcurrenth/',views.getcurrenthc),
    #获取当前的温度
    path(r'api/getcurrentt/<str:productname>/<str:devicename>/',views.getcurrentt),
    #获取当前的温度
    path(r'api/getcurrentt/',views.getcurrenttc),
    #图表测试url
    path(r'api/chart/test',views.charttest),
    #错误信息读取
    path(r'api/data/error',views.dataerror)
]
#添加这行--- 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

