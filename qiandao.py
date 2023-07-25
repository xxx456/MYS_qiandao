import requests
import time

print("大号签到")
#登陆
url1 = "https://api-takumi.mihoyo.com/event/luna/sign"

headers = {
    "Connection": "keep-alive",
    "Content-Length": "84",
    "DS": "1690287736,9n7o4i,b544c2ed81d39178badc5288814d4f8c",
    "x-rpc-app_version": "2.53.1",
    "x-rpc-validate": "c4ef0167fcf1bde3644e46f05cf49827",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2102J2SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 miHoYoBBS/2.52.1",
    "x-rpc-device_id": "97bcc1b8-d952-35cc-a82a-f243117cc03a",
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
    "Cookie": "ltuid=381745225; login_ticket=2qBydKX9G5qchjkFFXlvoZlt4512uL2Wc6ZieDPx; account_id=381745225; ltoken=2lnvzx9kmBUyp1RIcnuOHoxEXcKiQKYopt12PgFl; _MHYUUID=3775c917-cb27-4476-2a02-fc6b7937e0cc; aliyungf_tc=9149d0c348431c7d045b06fa0d927193ddc1f5bb58a45ddfb43f64f30de07825; mi18nLang=zh-cn; DEVICEFP_SEED_ID=aa0f5e5ced3b8f1c; DEVICEFP_SEED_TIME=1686469981733; cookie_token=x5t4Z3E1T6wCgq4Y18Tmhi6IMloH7Mj5bHUoFPoU; DEVICEFP=38d7ef749e255; _ga=GA1.1.1804909849.1686469967; _ga_HB2EBLW929=GS1.1.1690287726.2.0.1690287731.0.0.0; _ga_J1K3VE5FNG=GS1.1.1690287730.1.0.1690287731.0.0.0"
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
  "Cookie": "ltuid=381745225; login_ticket=2qBydKX9G5qchjkFFXlvoZlt4512uL2Wc6ZieDPx; account_id=381745225; ltoken=2lnvzx9kmBUyp1RIcnuOHoxEXcKiQKYopt12PgFl; _MHYUUID=3775c917-cb27-4476-2a02-fc6b7937e0cc; aliyungf_tc=9149d0c348431c7d045b06fa0d927193ddc1f5bb58a45ddfb43f64f30de07825; mi18nLang=zh-cn; DEVICEFP_SEED_ID=aa0f5e5ced3b8f1c; DEVICEFP_SEED_TIME=1686469981733; cookie_token=x5t4Z3E1T6wCgq4Y18Tmhi6IMloH7Mj5bHUoFPoU; DEVICEFP=38d7ef749e255; _ga=GA1.1.1804909849.1686469967; _ga_HB2EBLW929=GS1.1.1690287726.2.0.1690287737.0.0.0; _ga_J1K3VE5FNG=GS1.1.1690287730.1.0.1690287737.0.0.0"
}

send = requests.get(url=url2,headers=headers)
print(send.text)

time.sleep(1)
print("小号签到")
url1 = "https://api-takumi.mihoyo.com/event/luna/sign"

headers = {
    "Connection": "keep-alive",
    "Content-Length": "84",
    "Accept": "application/json, text/plain, */*",
    "DS": "1690206919,h3nmkb,e93a1026765f29ca6ba087f8741f3712",
    "x-rpc-app_version": "2.53.1",
    "x-rpc-device_id": "cae9f681-7cea-3919-9b69-7c3b591a5432",
    "x-rpc-challenge": "8e1dfebe8db718025ee4f750434dd5c2",
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
    "Cookie": "_MHYUUID=962f885e-5ec7-4402-0bea-d1e5983e5f04; aliyungf_tc=fdca691bfa05dc33a7a6a509724e0c19e5e04ca2562ab820cf30d2360f75fbbe; ltuid=380394775; login_ticket=QiiKRJHkMJYStVdOl5QXEjbUzOV6Uavkfb7ViFze; account_id=380394775; ltoken=VBav86KT3Y58JKVOpEMlqherL0CesL71VABBW5eP; cookie_token=iRqGFkD8rQ8CqhT4QYQM2X3WevGRMFEfCwJnznzV; mi18nLang=zh-cn; DEVICEFP_SEED_ID=f5977ec4c7cf40bf; DEVICEFP_SEED_TIME=1690206903741; DEVICEFP=38d7ef717004b; _ga=GA1.2.1052220470.1687140204; _gid=GA1.2.2007679422.1690206905; _gat_gtag_UA_133007358_34=1; _ga_J1K3VE5FNG=GS1.1.1690206905.1.0.1690206913.0.0.0; _ga_HB2EBLW929=GS1.1.1690206904.1.0.1690206918.0.0.0"    
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
    "Cookie": "_MHYUUID=962f885e-5ec7-4402-0bea-d1e5983e5f04; aliyungf_tc=fdca691bfa05dc33a7a6a509724e0c19e5e04ca2562ab820cf30d2360f75fbbe; ltuid=380394775; login_ticket=QiiKRJHkMJYStVdOl5QXEjbUzOV6Uavkfb7ViFze; account_id=380394775; ltoken=VBav86KT3Y58JKVOpEMlqherL0CesL71VABBW5eP; cookie_token=iRqGFkD8rQ8CqhT4QYQM2X3WevGRMFEfCwJnznzV; mi18nLang=zh-cn; DEVICEFP_SEED_ID=f5977ec4c7cf40bf; DEVICEFP_SEED_TIME=1690206903741; DEVICEFP=38d7ef717004b; _ga=GA1.2.1052220470.1687140204; _gid=GA1.2.2007679422.1690206905; _gat_gtag_UA_133007358_34=1; _ga_HB2EBLW929=GS1.1.1690206904.1.1.1690206920.0.0.0; _ga_J1K3VE5FNG=GS1.1.1690206905.1.1.1690206920.0.0.0"    
}

send = requests.get(url=url2,headers=headers)
print(send.text)

