from time import sleep
import requests
import json
import os

# 打开并读取文件

routes_backup_file = "upstreams.json"
apisix_admin_url = "http://localhost:9000/apisix/admin/upstreams"

with open(routes_backup_file) as f:
    data = json.load(f)


# 从 chrome dev tools 复制
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA4NzQxMTIsImlhdCI6MTcxMDg3MDUxMiwic3ViIjoiZXAtc3JlIn0.6NyMoosUwbifhkBkRHow8sZSnMkgpgXd_662_eGuVtg',
    'Connection': 'keep-alive',
    'Referer': 'http://localhost:9000/upstream/list',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


# 获取并打印 rows 对象
rows = data['data']['rows']
for i, row in enumerate(rows):
    del row["create_time"]
    del row["update_time"]
    print(row)
    # payload = row
    response = requests.request("POST", apisix_admin_url, headers=headers, json=row)
    print(response.text)
    sleep(1)
    # print(f'Row {i+1}: {row}')