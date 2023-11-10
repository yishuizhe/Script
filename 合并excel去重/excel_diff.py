import pandas as pd

# 从第一个Excel文件读取数据
df1 = pd.read_excel('8.17-9.12.xlsx')

# 从第二个Excel文件读取数据
df2 = pd.read_excel('8.9-8.17xlsx')

# 获取两个DataFrame的第一列数据
col1_df1 = df1.iloc[:, 0]
col1_df2 = df2.iloc[:, 0]

# 合并两个列，并去重
combined_col = pd.concat([col1_df1, col1_df2], ignore_index=True)
deduplicated_col = combined_col.drop_duplicates()

# 创建新的DataFrame，包含去重的第一列数据，并保留原始数据的其余部分
result_df = pd.DataFrame(columns=[df1.columns[0]])

for value in deduplicated_col:
    rows = df1[df1[df1.columns[0]] == value]
    result_df = pd.concat([result_df, rows], ignore_index=True)

# 将结果写入新的Excel文件
result_df.to_excel('output.xlsx', index=False)

print("合并去重后的数据已写入Excel文件 'output.xlsx'")
