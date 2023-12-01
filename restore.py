from time import sleep
import requests
import json
import os

# 打开并读取文件

routes_backup_file = os.getenv("ROUTES_BACKUP_FILE")
apisix_admin_url = os.getenv("APISIX_ADMIN_URL")

with open(routes_backup_file) as f:
    data = json.load(f)


# 从 chrome dev tools 复制
headers = {}


# 获取并打印 rows 对象
rows = data['data']['rows']
for i, row in enumerate(rows):
    del row["create_time"]
    del row["update_time"]
    # print(row)
    # payload = row
    response = requests.request("POST", apisix_admin_url, headers=headers, json=row)
    print(response.text)
    sleep(1)
    # print(f'Row {i+1}: {row}')