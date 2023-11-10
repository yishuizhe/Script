读取Excel文件中的URL，然后解析这些URL以提取域名和判断协议来填充端口。

输入Excel示例：

| 序号 |                   漏洞位置                   |
| :--: | :------------------------------------------: |
|  1   |      http://example.com/vulnerability1       |
|  2   | https://subdomain.example.com/vulnerability2 |
|  3   |       http://anotherdomain.com/issue3        |
|  4   |                 invalid_url                  |
|  5   |      https://example.org/security_hole       |

输出结果示例：

| 序号 |                   漏洞位置                   |      涉及域名       |    端口     |
| :--: | :------------------------------------------: | :-----------------: | :---------: |
|  1   |      http://example.com/vulnerability1       |     example.com     |     80      |
|  2   | https://subdomain.example.com/vulnerability2 |     example.com     |     443     |
|  3   |       http://anotherdomain.com/issue3        |  anotherdomain.com  |     80      |
|  4   |                 invalid_url                  | 无法从URL中提取域名 | 未知的协议: |
|  5   |      https://example.org/security_hole       |     example.org     |     443     |