import pandas as pd

# 读取Excel文件
file_path = '1.xlsx'  # 替换成你的Excel文件路径
df = pd.read_excel(file_path)

# 统一格式并去除重复值
df['黑链'] = df['黑链'].str.rstrip('/')  # 去除URL末尾的斜杠
df.drop_duplicates(subset=['黑链'], keep='first', inplace=True)

# 保存结果到新的Excel文件
output_file = 'output.xlsx'  # 替换成你想要保存的文件路径
df.to_excel(output_file, index=False)

print(f"已保存结果到 {output_file}")

