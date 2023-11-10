读取一个包含域名的文件，然后尝试通过`gethostbyname`方法解析每个域名的IP地址。如果解析成功，它将域名和对应的IP写入'result.txt'文件，如果解析失败，则将域名和错误信息"notFind"写入'result.txt'文件。

输入Excel示例（DomainName.txt）：

```
example1.com  
example2.org  
invalid_domain  
example3.net
```

输出结果示例（result.txt）：

```php
example1.com    93.184.216.34  
example2.org    192.0.43.10  
invalid_domain  notFind  
example3.net    172.217.6.174
```