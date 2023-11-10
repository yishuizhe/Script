import pandas as pd

# 读取两个Excel文件
file1 = '2023-09-20.xlsx'  # 替换成你的文件路径
file2 = '2023-09-12.xlsx'  # 替换成你的文件路径

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# 将2的第一列数据存储为集合，以便快速查找
set_of_col2 = set(df2.iloc[:, 0])

# 过滤掉1中包含在2中的数据
filtered_df1 = df1[~df1.iloc[:, 0].isin(set_of_col2)]

# 保存结果到新的Excel文件
output_file = 'output.xlsx'  # 替换成你想要保存的文件路径
filtered_df1.to_excel(output_file, index=False)

print(f"已保存结果到 {output_file}")

