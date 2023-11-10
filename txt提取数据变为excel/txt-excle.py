import pandas as pd
import re

# 从TXT文件中读取文本数据
with open('heilian2023-08-09——2023-08-17.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化空的数据列表
data = []

# 正则表达式模式用于匹配黑链和黑词
pattern = r'黑链：\[\'(.*?)\'\]，黑词：(.*?)\n'

# 遍历文本行并解析数据
for line in lines:
    match = re.match(pattern, line)
    if match:
        blacklink = match.group(1)
        blackword = match.group(2)
        data.append({'黑链': blacklink, '黑词': blackword})

# 创建DataFrame对象
df = pd.DataFrame(data)

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', index=False)

print("数据已写入Excel文件 'output.xlsx'")

