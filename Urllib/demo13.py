"""
cooking登录
在数据采集需要绕过登录

Author：binxin
Date：2023/11/23 20:51
"""
import urllib.request

url = "https://m.weibo.cn/profile/7844546355"

headers = {
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': 'WEIBOCN_FROM=1110006030; SUB=_2A25IWztpDeRhGeFG71YU9CjPzjmIHXVrGTKhrDV6PUJbkdANLUHckW1NeW0UMmSkDnXteuMWZ6_P3Hrnm486Vsys; MLOGIN=1; _T_WM=60448710269; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174; XSRF-TOKEN=fd466d; mweibo_short_token=5c3125a1a8',
    'Mweibo-Pwa': '1',
    'Referer': 'https://m.weibo.cn/profile/7844546355',
    'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
