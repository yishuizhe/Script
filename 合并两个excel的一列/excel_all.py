import os  
import pandas as pd  
  
# 指定包含xlsx文件的目录  
directory = '/Users/peiyimiao/Desktop/未命名文件夹/'  
  
# 获取目录下所有xlsx文件的文件名  
xlsx_files = [filename for filename in os.listdir(directory) if filename.endswith('.xlsx')]  
  
# 如果没有xlsx文件，输出错误信息  
if not xlsx_files:  
    print("目录中没有xlsx文件。")  
    exit()  
  
# 创建一个空的DataFrame来存储合并后的数据  
merged_data = pd.DataFrame()  
  
# 循环读取每个xlsx文件的第一列数据并合并  
for xlsx_file in xlsx_files:  
    file_path = os.path.join(directory, xlsx_file)  
    data = pd.read_excel(file_path, usecols=[0])  # 读取第一列数据  
    merged_data = pd.concat([merged_data, data], ignore_index=True)  
  
# 重命名列名  
merged_data.columns = ['FirstColumn']  
  
# 将合并后的数据保存到新的xlsx文件  
merged_data.to_excel('merged_data.xlsx', index=False)  
print("合并完成。")