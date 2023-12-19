"""
下载

Author：binxin
Date：2023/11/20 20:19
"""
import urllib.request

# 下载网页
# url_page = "https://ssr1.scrape.center/"

# url代表下载路径 filename文件名
# urllib.request.urlretrieve(url_page, 'scrape.html')

# 下载图片
# url_img = 'https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c'

# urllib.request.urlretrieve(url_img,'scrape.png')

# 下载视频
url_video = 'https://vd2.bdstatic.com/mda-pkjg3j1629re4z2h/720p/h264/1700480141426778560/mda-pkjg3j1629re4z2h.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1700494480-0-0-98fb46f2a2d69b62592d1344d6ee60b0&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=2080435259&vid=15565599946852966896&klogid=2080435259&abtest='

urllib.request.urlretrieve(url_video,'bilibili.mp4')
