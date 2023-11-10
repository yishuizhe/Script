import sqlite3  
import os  
  
# 获取用户输入  
User = input("请输入你的计算机用户名:")  
  
# 构造Cookie数据库文件路径  
cookie_db_path = os.path.join('C:\\Users\\', User, '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies')  
  
try:  
    # 验证文件路径是否存在  
    if not os.path.exists(cookie_db_path):  
        print("数据库文件路径不存在。")  
        exit()  
  
    # 连接到Cookie数据库  
    conn = sqlite3.connect(cookie_db_path)  
  
    # 查询cookie信息（此处仍为SQLITE_MASTER，如需cookie信息，请做相应修改）  
    cursor = conn.execute('SELECT * FROM SQLITE_MASTER')  
  
    # 输出查询结果  
    for row in cursor:  
        print(row)  
except sqlite3.Error as e:  
    print("SQLite错误:", e)  
finally:  
    # 关闭数据库连接  
    if conn:  
        conn.close()