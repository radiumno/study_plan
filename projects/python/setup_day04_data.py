"""Day 04 练习用数据: 生成板块 CSV 文件"""
import csv

stocks = {
    'white_wine.csv': ['名称', '代码'],
    'white_wine_data': [
        ['茅台', '600519'],
        ['五粮液', '000858'],
        ['泸州老窖', '000568'],
        ['洋河股份', '002304'],
    ],
    'finance.csv': ['名称', '代码'],
    'finance_data': [
        ['招行', '600036'],
        ['平安', '601318'],
        ['兴业', '601166'],
        ['茅台', '600519'],
    ],
    'tech.csv': ['名称', '代码'],
    'tech_data': [
        ['腾讯', '00700'],
        ['阿里', '09988'],
        ['海康威视', '002415'],
        ['中兴通讯', '000063'],
    ],
}

for fname in ['white_wine.csv', 'finance.csv', 'tech.csv']:
    with open(fname, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(stocks[fname])
        w.writerows(stocks[f'{fname[:-4]}_data'])

print('CSV 数据文件已创建: white_wine.csv, finance.csv, tech.csv')
