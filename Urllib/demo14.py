"""
qq空间爬取练习

Author：binxin
Date：2023/11/24 11:08
"""
import urllib.request

url = "https://user.qzone.qq.com/2982231705"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': '_qpsvr_localtk=0.11805135449464998; uin=o2535497110; skey=@7QgtDbDo7; RK=HLktm2XcmP; ptcz=6e334893d7a38c061fffd06173ff48ba853233f9172389fcdefbed1a5349beed; p_uin=o2535497110; Loading=Yes; qz_screen=1280x720; 2535497110_todaycount=0; 2535497110_totalcount=54; pgv_pvid=4374066111; pgv_info=ssid=s9834266226; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; pt4_token=jeDHSpd1hkCABMyUEGsogc9yJjjMWNNdHtiziWpgUQM_; p_skey=2ABcbrkbZrkESmuhyEedtjf4yNS7jfQsw3TwBcnGEKA_; rv2=806C2286AD8C9E5D708CD28B9846C156265215D23289DC31A8; property20=95AACE5031ADF390C0CA061B6904EC6B0BF1152357CD5EDFC43357594778B6874D3ACB5068435D34'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('qqzone.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
