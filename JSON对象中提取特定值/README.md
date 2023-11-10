从一个名为`poc.txt`的文件中读取JSON数据，然后从这些JSON对象中提取`processInstanceId`并将其写入到另一个名为`output.txt`的文件中。

以下是一个输入示例和输出结果示例：

输入示例（poc.txt 文件内容）：

```json
json复制代码

{"processInstanceId": "1234", "otherKey": "otherValue"}{"processInstanceId": "5678", "otherKey": "anotherValue"}
```

输出结果示例（output.txt 文件内容）：

```yaml
1234  
5678
```