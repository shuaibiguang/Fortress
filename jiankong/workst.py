import threading,time,json,socket,pickle,os
import pymysql.cursors
from opsapp.apps import OpsappConfig as C

ipList = []
ipInfo = {}

# 将监控结果写入数据库
def save_info(cont):
    while True:
        if len(ipInfo) > 0:
            print ('我在存储数据')
            for ip in ipInfo:
                with cont.cursor() as cursor:
                    sql = 'update opsapp_serverlist set info = %s where ip = %s'
                    cursor.execute(sql,(ipInfo[ip],ip))
            cont.commit()
        time.sleep(1)

#工作中继器，给不同的ip分配不同的线程，10s 刷新一下

def socket_Repeater():
    work_thread = []
    while True:
        if len(ipList) > 0:
                for ip in ipList:
                    t = threading.Thread(target=socket_work,args=(ip,))
                    t.setName(ip)
                    work_thread.append(t)
                for thre in work_thread:
                    print (thre)
                    thre.setDaemon(True)
                    thre.start()
                    print (thre.isAlive())
        time.sleep(1)
        del work_thread[:]


# socket工作的主要函数，请求拿取数据
def socket_work(ip):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((ip,C.OPSPORT))
        sock.send('serverinfo'.encode())
        data = sock.recv(100000)
        data = json.dumps(pickle.loads(data))
        ipInfo[ip] = data
    except:
        ipInfo[ip] = ''
    print (ipInfo)


# 拿取需要监控的服务器 10s 更新一下
def get_ip_list(connt):
    while True:
        with connt.cursor() as cursor:
            sql = 'select ip from opsapp_serverlist'
            cursor.execute(sql)
            result = cursor.fetchall()
            del ipList[:]
            for i in result:
                ipList.append(i[0])
        time.sleep(10)

# 获取数据库连接
def connect():
    connection = pymysql.connect(host=C.db_host,
    user=C.db_user,
    password=C.db_password,
    db=C.db_name,
    charset='utf8mb4')
    return connection


if __name__ == '__main__':
    connt = connect()
    threadList = []
    # 拿取到数据库连接，然后查询表拿取需要监控的服务器
    threading.Thread(target=get_ip_list,args=(connt,)).start()
    # t = threading.Thread(target=get_ip_list,args=(connt,))
    # print (dir(t))
    # 查询服务器状态
    threading.Thread(target=socket_Repeater,args=()).start()
    # 存储数据
    threading.Thread(target=save_info,args=(connt,)).start()
