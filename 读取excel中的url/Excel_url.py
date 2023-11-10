import pandas as pd  
from urllib.parse import urlparse  
  
# 读取Excel文件  
df = pd.read_excel('1.xlsx')  
  
# 处理第三列的URL数据，填充第一列和第二列  
for index, row in df.iterrows():  
    url = row['漏洞位置']  
    parsed_url = urlparse(url)  
      
    # 提取域名并填充到第一列  
    parts = parsed_url.netloc.split('.')  
    if len(parts) > 1:  
        domain = parts[-2] + '.' + parts[-1]  
        df.at[index, '涉及域名'] = domain  
    else:  
        print("无法从URL中提取域名:", url)  
      
    # 判断协议并填充端口到第二列  
    if parsed_url.scheme == 'http':  
        df.at[index, '端口'] = 80  
    elif parsed_url.scheme == 'https':  
        df.at[index, '端口'] = 443  
    else:  
        print("未知的协议:", parsed_url.scheme)  
  
# 保存修改后的Excel文件  
df.to_excel('你的文件名.xlsx', index=False)
