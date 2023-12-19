"""
jsonpath 解析淘票票

Author：binxin
Date：2023/11/27 15:26
"""
import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1701070258998_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1701071322520_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Bx-V': '2.5.5',
    'Cookie': '_m_h5_tk=5e975e3548c9d6e5d6463f91db59a4d9_1700975872462; _m_h5_tk_enc=7710ed77e01a9cbbd33dbdb7d9c6360e; v=0; _samesite_flag_=true; cookie2=1ad7f9fcf9cdcd8634cb10379c879543; t=27f6a6a05aebe181481642298dfaec21; _tb_token_=5d73533e7793; tfstk=dYHvnyfjjUYDU8BxYZdkbqWZ76Kktxn2mqoCIP4c143-8qK4sscm6NU-AnzD_IutwVgzirMtbOEsfV-4SnRo0myaCeYnWpmq01lw-ef7E98uQRTH-_X_gpeZJAmVTGKRNQYkutMjLoOLunMot1oYDSUOIz6tQY63Mys0PO6_PoBwWvDdhvb3JlfX23CN_SZyCgciV; l=fBEg8NVPPJmjWMJhBO5IFurza779nIRb4PVzaNbMiIEGa6I5tFGDCNCT2DwkSdtjgTCxVeKyMAhYGdLHR3AgCc0c07kqm0S-3xvtaQtJe; isg=BJ-foZ6wBjK0UgIolxPukyW5LvMpBPOmsIAYtDHsuc6VwL9CONQn9iWeglC-3cse',
    'Referer': 'https://dianying.taobao.com/',
    'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('demo5.json', 'w', encoding='utf-8') as fp:
    fp.write(content)


obj=json.load(open('demo5.json','r',encoding='utf-8'))

city_list=jsonpath.jsonpath(obj,'$..regionName')

print(city_list)