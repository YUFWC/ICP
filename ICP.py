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
obj = re.compile(f'<td class="align-middle" nowrap="nowrap">(?P<bei>.*?)</td>.*?'
                 f'<td class="align-middle">.*?</td>.*?'
                 f'<td class="align-middle">.*?<div>.*?<a href="/seo/(?P<s>.*?)">', re.S)
def a():
    obj_1 = obj.finditer(resp.text)
    for i in obj_1:
        bt = ("备案号：" + i.group('bei'))
        bs = "子域名：" + i.group('s')
        print(bt.replace(" ", ""), bs.replace(" ", ""))
print(a())
