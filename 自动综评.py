import requests
import json

def POST(token):
    #调取API，获得一句随机诗词
    HTTPGET = requests.get('https://v1.hitokoto.cn/?c=i')
    data = json.loads(HTTPGET.text)
    body = data['hitokoto']
    from_who = data['from']
    minyan = f"{body} -- {from_who}"


    #调用综合评价系统API，发布自评
    authinheader = f'Bearer {token}'
    header = {"Host": "manage.zyzp.compevt.com","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0","Accept": "application/json, text/plain, */*","Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Accept-Encoding": "gzip, deflate","Content-Type": "application/x-www-form-urlencoded","Authorization": authinheader ,"Content-Length": "241","Origin": "http://student.zyzp.compevt.com","Connection": "keep-alive","Referer": "http://student.zyzp.compevt.com/"}
    data = {"categoryId":"2","recordTemplate":"210","title":"每日诗词","content":minyan,"type":"0","eventTimeType":"1"}
    HTTPPOST = requests.post('http://manage.zyzp.compevt.com/record/publish', headers=header, data=data)
    if json.loads(HTTPPOST.text)['code'] == 'success':
        print('发布成功，可喜可贺')
    else:
        print(json.loads(HTTPPOST.text)['message'])

print('遵义市综合评价系统自动评价，@学猫叫')
token = input('请输入用户token')
number = int(input('您需要发布多少条记录？'))
#token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0OTkyMzUiLCJpc3MiOiJNSFFDX1RFQ0hfQVBQX1NFOnN0dWRlbnQiLCJpYXQiOjE1ODc1NDY5MjYsImV4cCI6MTU4ODE1MTcyNn0.EMm_RnvX83LVP_Va_MtjlBhODjMI_YwslL2wKMqyqKD0tpCwKHCk2Kl18Iy5CkO-5AfqpEadjI8M-XgtVyTAow'
for i in range(number):
    POST(token)
