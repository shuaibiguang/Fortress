from django.shortcuts import render
from django.http import HttpResponse
from opsapp.apps import OpsappConfig as C
from opsapp.models import serverlist as serverlistModel
from django.contrib.auth.decorators import login_required
import opsapp.ajaxTool as atool
import json,socket,pickle,time,threading

@login_required(login_url="/accounts/login/")
def index(request):
    return render(request,'index.html')

# 查看数据库详情
def serverinfo(request,id):
    if 'POST' == request.method:
        id = request.POST['id']
        a = serverlistModel.objects.get(id=id)
        return atool.apiReturn('200','ok',json.loads(a.info))
    # return render(request,'serverinfo.html',{'id':id,'local':'http://guang.unnaming.net'﻿﻿})
    return render(request, 'serverinfo.html', {'id':id, 'local': 'http://guang.unnaming.net'})

# 查看数据库列表
def serverlist(request):
    if 'POST' == request.method:
        serverlist = serverlistModel.objects.all()
        return atool.apiReturn2(serverlist)
    serverlist = serverlistModel.objects.all()
    slist = []
    for i in serverlist:
        try:
            info = json.loads(i.info)
        except:
            info = []
        print (type(info))
        arr= {'id':i.id,'ip':i.ip,'info':info}
        slist.append(arr)
    print (slist)
    return render(request,'serverlist.html',{'serverlist':slist})


# 添加新的服务器
def addserver(request):
    if 'POST' == request.method:
        ip = request.POST['ip'];
        # 判断数据库中是否已经存在
        serverlist = serverlistModel.objects.all()
        for i in serverlist:
            if i.ip == ip:
                return atool.apiReturn(403,'当前ip已经存在...','')
        serverlistModel.objects.create(ip=ip)
        return atool.apiReturn(200,'添加完成...','')
    else:
        # 渲染模板
        serverlist = serverlistModel.objects.all()
        return render(request,'addserver.html',{'serverlist':serverlist})

# 删除服务器
def deleteServer(request):
    if 'POST' == request.method:
        sid = request.POST['id']
        data = serverlistModel.objects.get(id=sid)
        data.delete()
        return atool.apiReturn(200,"删除完毕...",'')

# 返回服务器监控详情
def apiserverinfo(request):
    data = connect(C.OPSIP,"serverinfo")
    response = HttpResponse(data,content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

# 进行连接数据库操作
def connect(ip,mass):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, C.OPSPORT))
    sock.send(mass.encode())
    data = sock.recv(100000)
    data = json.dumps(pickle.loads(data))
    return data
    # M.eit_ops_info(ip,data)
