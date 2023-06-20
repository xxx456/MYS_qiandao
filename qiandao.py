import requests
import time

print("大号签到")
#登陆
url1 = "https://api-takumi.mihoyo.com/event/luna/sign"

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

send = requests.post(url=url1,headers=headers,json=data)
print(send.text)

time.sleep(1)

#签到
url2 = "https://api-takumi.mihoyo.com/event/luna/info?lang=zh-cn&act_id=e202304121516551&region=prod_gf_cn&uid=113150520"

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

send = requests.get(url=url2,headers=headers)
print(send.text)


print("小号签到")
url1 = "https://api-takumi.mihoyo.com/event/luna/sign"

headers = {
    "Connection": "keep-alive",
    "Content-Length": "84",
    "Accept": "application/json, text/plain, */*",
    "DS": "1687161443,l1c1gc,89fecb92b4404e90f7c7648fa7d3838b",
    "x-rpc-app_version": "2.52.1",
    "x-rpc-device_id": "cae9f681-7cea-3919-9b69-7c3b591a5432",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2102J2SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 miHoYoBBS/2.52.1",
    "x-rpc-client_type": "5",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://webstatic.mihoyo.com",
    "X-Requested-With": "com.mihoyo.hyperion",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://webstatic.mihoyo.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "ltuid=380394775; login_ticket=MmJ58X4hSFkFSi1ZBJX5itdL3uzzmZKGyBZryVhv; account_id=380394775; ltoken=VBav86KT3Y58JKVOpEMlqherL0CesL71VABBW5eP; cookie_token=iRqGFkD8rQ8CqhT4QYQM2X3WevGRMFEfCwJnznzV; _MHYUUID=94db06d5-7978-4406-3bc6-5a6596a03bc2; _gid=GA1.2.1791211285.1687140300; aliyungf_tc=6e530556a3cc4244721ca1fc12c77278687ad73151013e7fb5c5d827de46f8c9; mi18nLang=zh-cn; DEVICEFP_SEED_ID=04efbbb92a282b2d; DEVICEFP_SEED_TIME=1687161441002; _ga_HB2EBLW929=GS1.1.1687161441.1.0.1687161441.0.0.0; DEVICEFP=38d7eeebe6dd8; _ga=GA1.2.1589657760.1687140300; _gat_gtag_UA_133007358_34=1"
    }

data = {"act_id":"e202304121516551","region":"prod_gf_cn","uid":"101889632","lang":"zh-cn"}

send = requests.post(url=url1,headers=headers,json=data)
print(send.text)

time.sleep(1)

#签到
url2 = "https://api-takumi.mihoyo.com/event/luna/info?lang=zh-cn&act_id=e202304121516551&region=prod_gf_cn&uid=101889632"

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
    "Cookie": "ltuid=380394775; login_ticket=MmJ58X4hSFkFSi1ZBJX5itdL3uzzmZKGyBZryVhv; account_id=380394775; ltoken=VBav86KT3Y58JKVOpEMlqherL0CesL71VABBW5eP; cookie_token=iRqGFkD8rQ8CqhT4QYQM2X3WevGRMFEfCwJnznzV; _MHYUUID=94db06d5-7978-4406-3bc6-5a6596a03bc2; _gid=GA1.2.1791211285.1687140300; aliyungf_tc=6e530556a3cc4244721ca1fc12c77278687ad73151013e7fb5c5d827de46f8c9; mi18nLang=zh-cn; DEVICEFP_SEED_ID=04efbbb92a282b2d; DEVICEFP_SEED_TIME=1687161441002; DEVICEFP=38d7eeebe6dd8; _ga=GA1.2.1589657760.1687140300; _gat_gtag_UA_133007358_34=1; _ga_HB2EBLW929=GS1.1.1687161441.1.0.1687161444.0.0.0"
    }

send = requests.get(url=url2,headers=headers)
print(send.text)

