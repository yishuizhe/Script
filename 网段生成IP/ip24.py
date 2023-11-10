import ipaddress  
  
# 读取网段文件  
with open('ip24.txt', 'r') as f:  
    networks = f.read().splitlines()  
  
# 用于保存IP地址的列表  
ips = []  
  
# 遍历每个网段  
for network in networks:  
    # 创建IPv4网络对象  
    net = ipaddress.IPv4Network(network)  
  
    # 遍历网络中的每个主机IP  
    for ip in net.hosts():  
        # 添加到IP地址列表  
        ips.append(str(ip))  
  
# 写入到新的文件  
with open('output.txt', 'w') as f:  
    for ip in ips:  
        f.write(ip + '\n')
