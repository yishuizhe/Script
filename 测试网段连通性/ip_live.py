import os  
import random  
  
def read_subnets(filename):  
    """从文件中读取网段"""  
    with open(filename, 'r') as file:  
        subnets = [line.strip() for line in file]  
    return subnets  
  
def is_ip_alive(ip):  
    """检查IP是否存活"""  
    response = os.system(f"ping -c 1 {ip} > /dev/null")  
    return response == 0  
  
def ping_test(subnet):  
    """使用ping测试网段的连通性"""  
    # 从网段中随机选择5个IP进行ping测试  
    base_ip = '.'.join(subnet.split('.')[:3])  # 获取网段的前三段  
  
    for i in range(1, 6):  # 测试5次  
        random_ip = f"{base_ip}.{random.randint(1, 254)}"  
        if is_ip_alive(random_ip):  
            return f"网段 {subnet} 是连通的 (至少 {random_ip} 是可达的)"  
      
    # 如果都没有响应，则认为该网段不通  
    return f"网段 {subnet} 是不通的"  
  
# 其他部分保持不变...
  
# 从文件中读取网段  
subnets = read_subnets('subnets.txt')  
total_subnets = len(subnets)  
  
# 将ping测试结果写入文件  
with open('ping_results.txt', 'w') as file:  
    for i, subnet in enumerate(subnets):  
        result = ping_test(subnet)  
        file.write(result + '\n')  
          
        # 输出进度  
        progress = (i + 1) / total_subnets * 100  
        print(f"进度: {progress:.2f}% - 正在测试网段: {subnet}")