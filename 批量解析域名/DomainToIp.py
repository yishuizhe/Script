from socket import gethostbyname  
  
DOMAIN = "DomainName.txt"  
RESULT_FILE = "result.txt"  
ERROR_FILE = "error.txt"  
  
num = 0  
count = 0  
with open(DOMAIN, 'r') as f:  # 统计文件中域名总数  
    count = len(f.readlines())  
  
print("共计：" + str(count) + "域名，开始解析.......")  
  
with open(RESULT_FILE, 'a+') as result, open(ERROR_FILE, 'a+') as error:  
    with open(DOMAIN, 'r') as f:  
        for line in f.readlines():  
            num += 1  
            if num % 100 == 0:  # 每完成100个域名解析就输出一次进度  
                print("已完成：" + str(num) + "/" + str(count))  # 计算输出完成进度  
            try:  
                host = gethostbyname(line.strip('\n'))  # 域名反解析得到的IP  
                result.write(line.strip('\n') + '    ')  # 显示有ip绑定的域名，用空格隔开  
                result.write(host + '\n')  
            except OSError:  # 捕获特定的异常  
                error.write(line.strip() + "    " + "notFind" + "\n")