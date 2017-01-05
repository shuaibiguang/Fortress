import json
from django.http import HttpResponse
# ajax 返回数据
def apiReturn(code,massage,info):
    data = json.dumps([code,massage,info])
    response = HttpResponse(data,content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
