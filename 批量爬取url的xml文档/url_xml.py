import pandas as pd  
import re  
  
try:  
    # 读取txt文件  
    with open('input.txt', 'r') as file:  
        lines = file.readlines()  
  
    # 匹配并提取目标格式的URL  
    urls = []  
    pattern = r'\./xm/(\d+\.xml)'  
    for line in lines:  
        match = re.search(pattern, line)  
        if match:  
            xml_file = match.group(1)  
            url = f"https://www.test.com/xm/{xml_file}"  
            urls.append(url)  
  
    # 如果没有找到任何匹配的URL，可以抛出一个异常  
    if not urls:  
        raise ValueError("No matching URLs found")  
  
    # 创建DataFrame并保存到xlsx文件  
    df = pd.DataFrame(urls, columns=["URL"])  
    df.to_excel('output.xlsx', index=False)  
      
except FileNotFoundError:  
    print("The specified input file was not found")  
except ValueError as ve:  
    print(ve)  
except Exception as e:  
    print(f"An unexpected error occurred: {e}")