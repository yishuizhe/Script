import os  
import sqlite3  
  
User = input("请输入你的计算机用户名:")  
# Cookie数据库文件路径（根据你的实际情况进行修改）  
cookie_db_path = os.path.join('C:\\', 'Users', User, 'AppData\\Local\\Google\\Chrome\\User Data\\Default', 'Cookies')  
  
conn = None  
try:  
    # 连接到Cookie数据库  
    conn = sqlite3.connect(cookie_db_path)  
  
    # 查询cookie信息  
    cursor = conn.execute('SELECT value FROM cookies where host_key="修改"')  
  
    # 输出查询结果  
    for row in cursor:  
        print(row)  
  
except sqlite3.Error as e:  
    print("SQLite错误:", e)  
  
finally:  
    # 关闭数据库连接  
    if conn:  
        conn.close()