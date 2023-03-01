import requests
import re
b = input("备案号/域名：")
url = f"https://www.beianx.cn/search/{b}"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"
}
resp = requests.get(url, headers=header)
# print(resp.text)
resp_text = resp.text
obj = re.compile(f'<td class="align-middle" nowrap="nowrap">(?P<bei>.*?)</td>', re.S)
odj = re.compile(f'<a href="/seo/(?P<web>.*?)">', re.S)
obj_1 = obj.finditer(resp.text)
for i in obj_1:
    bt = (i.group('bei'))
    # print("备案号：", bt.replace(" ", ""))
    odj_1 = odj.finditer(resp_text)
    for it in odj_1:
        bs = (it.group('web'))
        print("备案号：", bt.replace(" ", "") + "子公司域名：", bs)
        with open('ICP.txt', 'a') as file:
            print("备案号：", bt.replace(" ", "") + "子公司域名：", bs, file=file)
        break
