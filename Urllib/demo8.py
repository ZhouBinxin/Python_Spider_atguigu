"""
百度详细翻译

Author：binxin
Date：2023/11/21 16:40
"""
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': '*/*',

    # 该行必须注释
    # 'Accept-Encoding': 'gzip, deflate, br',

    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Acs-Token': '1700554896797_1700555095251_haVFbhHVYodef+ABK34At5fE26z1GIBgK/5G/9f1yFzBA9YZ1QBKmV3/5uvNRmnNbLoH37UeOdciaPkcXzg5nmb1SdilOIoDEuDPRQ2slMYnAf3HxoiAcNv87L9UmtSu32wpt1gf6xcHChw9O+cWpCvdMwz7i/VaxfVqHVw48APnJ3YDedj4kLU2Jb2zKS82NpTXClm9oWXH0KQKQCjFl/91IfozQPxc6FWDsbnlmYi53NwunPzGIbuKLED+FcoLVE5yHDnClCH4SpyoC1oy03PPeEPUPxjP4ZBnaIro9NVDwqkcbWs1zuaMjwtXtQjXfKBDQtFoH3+a1KQgm2Z1BskaL1D85Z8FmrQvl+p8fjm9FZc/TM49BFjN3vrgzy+orf1Bk5PtTZFpYqMQ/qyEkLFNF5NV/BTdOzXhYB5If++Zth5IdGEiewM8xmLbikmnHuQG/2MFze06MR2wTNLM1ddbsHGXduBL1SZT1BH3Nhs=',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '153',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1690027568; ZFY=hJHsAJcm:BzM1AXD9a0vLfFZGJrzgW2kpVMqv0v6Ps1o:C; H_WISE_SIDS=234020_216844_213353_214793_110085_244716_257731_257015_260234_253022_259300_261715_236312_256419_265302_265881_266361_265776_267288_267371_266846_267421_265615_267405_265986_256302_266188_267898_259033_266713_268406_268593_268030_268842_259643_269232_269388_268766_188333_269730_269832_269904_269803_269049_267066_256739_270460_270534_267528_270625_270664_270548_270922_270966_271039_268874_270793_271169_271175_271193_268728_269771_267782_268987_269034_271229_269621_267659_271319_265032_269892_266027_270482_269609_270102_271608_270876_270443_269785_270157_271671_271985_271813_271957_271954_271943_256151_269211_234295_234207_266324_271187_272225_270055_272279_263618_267596_272055_272366_272008_272337_267559_272460_271145_8000076_8000108_8000124_8000136_8000159_8000164_8000168_8000177_8000179_8000186_8000203; BAIDU_WISE_UID=wapp_1692517164729_638; __bid_n=18a11e266418064ed3a010; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1692497260,1692755924,1693024343,1693128438; H_WISE_SIDS_BFESS=234020_216844_213353_214793_110085_244716_257731_257015_260234_253022_259300_261715_236312_256419_265302_265881_266361_265776_267288_267371_266846_267421_265615_267405_265986_256302_266188_267898_259033_266713_268406_268593_268030_268842_259643_269232_269388_268766_188333_269730_269832_269904_269803_269049_267066_256739_270460_270534_267528_270625_270664_270548_270922_270966_271039_268874_270793_271169_271175_271193_268728_269771_267782_268987_269034_271229_269621_267659_271319_265032_269892_266027_270482_269609_270102_271608_270876_270443_269785_270157_271671_271985_271813_271957_271954_271943_256151_269211_234295_234207_266324_271187_272225_270055_272279_263618_267596_272055_272366_272008_272337_267559_272460_271145_8000076_8000108_8000124_8000136_8000159_8000164_8000168_8000177_8000179_8000186_8000203; APPGUIDE_10_6_5=1; APPGUIDE_10_6_6=1; BAIDUID_BFESS=EBC2B0F02DE54CA945DEC2A522C58DC0:FG=1; APPGUIDE_10_6_7=1; APPGUIDE_10_6_9=1; BDUSS=VBqWS16dlBxNHBaQjA4c04yM2Z3S1hJVEp2MGY4YWpCenZ0flZMVnZwSlZobjFsRVFBQUFBJCQAAAAAAQAAAAEAAAA1wVhn1r3Uwsz9xM~J-QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFX5VWVV-VVlU; BDUSS_BFESS=VBqWS16dlBxNHBaQjA4c04yM2Z3S1hJVEp2MGY4YWpCenZ0flZMVnZwSlZobjFsRVFBQUFBJCQAAAAAAQAAAAEAAAA1wVhn1r3Uwsz9xM~J-QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFX5VWVV-VVlU; BIDUPSID=EBC2B0F02DE54CA945DEC2A522C58DC0; H_PS_PSSID=39669_39663_39676_39678_39710_39713_39749_39674_39785_39703_39793_39682; BA_HECTOR=248l252k80ak00240l2080051ilmkii1r; RT="z=1&dm=baidu.com&si=82643ae1-aaab-49e1-b3e4-a3c61e4bb037&ss=lp6w2pjo&sl=1&tt=1s7&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2ui&ul=smo&hd=sn6"; ab_sr=1.0.1_YTNiYWUxNWM0YmU5MWRlMDdjNWY2MThlOTA0NDEzNmEwM2FhNTFkNzRiYzVkMjI4YTdjNjI5MTU5OWZlNzk4ZDU3NmViNmMzMjhlNTk2ZTI0ZDUzMTQzMTQzZTJiYWNiODBmOTVkYzVkOGQ1NWY1MGY2NDNlNTBmYzk4Njg1OWU5Y2IyZTA2OWRmYjQ4MjRhYWM2MWFiN2FkYTRhYjM5Y2NjMmE1NmYwMzFiMTgxNGQ1YjdjMGEwYzczZWU2NWMy',
    # 'Dnt': '1',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    # 'Sec-Ch-Ua-Mobile': '?0',
    # 'Sec-Ch-Ua-Platform': 'Windows',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    # 'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'ae16933c30637316aa2381165ae3e29a',
    'domain': 'common',
    'ts': '1700555095216'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

import json

obj = json.loads(content)
print(obj)
