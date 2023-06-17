import requests
import time
#登陆
url = "https://api-takumi.mihoyo.com/event/luna/sign"

headers = {
    "Connection": "keep-alive",
    "Content-Length": "84",
    "DS": "1686718074,j08hn9,df79ba5d74ba9e7bbbf2d8304e985777",
    "x-rpc-app_version": "2.52.1",
    "x-rpc-validate": "c4ef0167fcf1bde3644e46f05cf49827",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2102J2SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 miHoYoBBS/2.52.1",
    "x-rpc-device_id": "97bcc1b8-d952-35cc-a82a-f243117cc03a",
    "x-rpc-challenge": "4da086b3bf50089d7dbbe61cbc8b4349",
    "Accept": "application/json, text/plain, */*",
    "x-rpc-seccode": "c4ef0167fcf1bde3644e46f05cf49827%7Cjordan",
    "Content-Type": "application/json;charset=UTF-8",
    "x-rpc-client_type": "5",
    "Origin": "https://webstatic.mihoyo.com",
    "X-Requested-With": "com.mihoyo.hyperion",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://webstatic.mihoyo.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "ltuid=381745225; login_ticket=2qBydKX9G5qchjkFFXlvoZlt4512uL2Wc6ZieDPx; account_id=381745225; ltoken=2lnvzx9kmBUyp1RIcnuOHoxEXcKiQKYopt12PgFl; cookie_token=zzT0IPYjg9erH46ftfzuVjYXwnMTqQWKEhsAOAGA; _MHYUUID=3775c917-cb27-4476-2a02-fc6b7937e0cc; aliyungf_tc=9149d0c348431c7d045b06fa0d927193ddc1f5bb58a45ddfb43f64f30de07825; mi18nLang=zh-cn; DEVICEFP_SEED_ID=aa0f5e5ced3b8f1c; DEVICEFP_SEED_TIME=1686469981733; DEVICEFP=38d7eed095d97; _ga=GA1.2.1804909849.1686469967; _gid=GA1.2.574023903.1686718058; _gat_gtag_UA_133007358_34=1; _ga_HB2EBLW929=GS1.1.1686718057.2.1.1686718073.0.0.0"
}

data = {"act_id":"e202304121516551","region":"prod_gf_cn","uid":"113150520","lang":"zh-cn"}

send = requests.post(url=url,headers=headers,json=data)
print(send.text)

time.sleep(3)

#签到
url = "https://api-takumi.mihoyo.com/event/luna/info?lang=zh-cn&act_id=e202304121516551&region=prod_gf_cn&uid=113150520"

headers = {
  "Accept": "application/json, text/plain, */*",
  "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2102J2SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 miHoYoBBS/2.52.1",
  "Origin": "https://webstatic.mihoyo.com",
  "X-Requested-With": "com.mihoyo.hyperion",
  "Sec-Fetch-Site": "same-site",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": "https://webstatic.mihoyo.com/",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
  "Cookie": "ltuid=381745225; login_ticket=2qBydKX9G5qchjkFFXlvoZlt4512uL2Wc6ZieDPx; account_id=381745225; ltoken=2lnvzx9kmBUyp1RIcnuOHoxEXcKiQKYopt12PgFl; cookie_token=zzT0IPYjg9erH46ftfzuVjYXwnMTqQWKEhsAOAGA; _MHYUUID=3775c917-cb27-4476-2a02-fc6b7937e0cc; aliyungf_tc=9149d0c348431c7d045b06fa0d927193ddc1f5bb58a45ddfb43f64f30de07825; mi18nLang=zh-cn; DEVICEFP_SEED_ID=aa0f5e5ced3b8f1c; DEVICEFP_SEED_TIME=1686469981733; DEVICEFP=38d7eed095d97; _ga=GA1.2.1804909849.1686469967; _gid=GA1.2.574023903.1686718058; _gat_gtag_UA_133007358_34=1; _ga_HB2EBLW929=GS1.1.1686718057.2.1.1686718075.0.0.0"
}

send = requests.get(url=url,headers=headers)
print(send.text)
