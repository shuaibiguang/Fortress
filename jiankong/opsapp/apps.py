from django.apps import AppConfig


class OpsappConfig(AppConfig):
    name = 'opsapp'
    LOCAL = 'http://112.74.35.148'
    LOCAL_PROT = 80
    OPSIP = '112.74.35.148'
    OPSPORT = 8001
    # 数据库部分
    db_engine = 'django.db.backends.mysql'
    db_name = 'jiankong'
    db_user = 'root'
    db_password = 'root'
    db_host = 'localhost'
    db_port = '3306'