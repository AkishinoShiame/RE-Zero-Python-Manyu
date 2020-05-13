import requests
import json
import csv
import pandas as pd

raw_data = requests.get('https://api.hahow.in/api/courses?limit=1&page=0')
print(raw_data.json())

raw_data = requests.get('https://api.hahow.in/api/courses?limit=30&page=0')
print(raw_data.json()['data'][0])

#extract the wanted information.
cl_pri = raw_data.json()['data'][0]['price']
teach = raw_data.json()['data'][0]['owner']['name']
cor_tit = raw_data.json()['data'][0]['title']
cor_des = raw_data.json()['data'][0]['metaDescription']
curre = raw_data.json()['data'][0]['currencyCode']
print(cl_pri, curre, teach, cor_tit, cor_des)

with open('./raw/course_output.csv', 'w', newline='', encoding="utf-8") as out_csv:
    writer = csv.writer(out_csv)
    # we needs to put title in first line.
    title = "費用", "両替率", "先生名", "授業名", "授業説明"
    writer.writerow(title)
    for item in raw_data.json()['data']:
        cl_pri = item['price']
        teach = item['owner']['name']
        cor_tit = item['title']
        cor_des = item['metaDescription']
        curre = item['currencyCode']
        row_data = cl_pri, curre, teach, cor_tit, cor_des
        writer.writerow(row_data)


pd.read_csv('./raw/course_output.csv',encoding="utf-8")