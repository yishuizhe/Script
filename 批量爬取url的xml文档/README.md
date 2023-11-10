读取一个名为'input.txt'的文本文件，然后从中提取匹配特定模式的URL，并将这些URL保存到一个Excel文件'output.xlsx'中。

**输入示例**

假设`input.txt`文件内容如下：

```arduino
This is a sample text with a URL ./xm/12345.xml inside.  
There can be multiple lines in this text.  
Another URL found here ./xm/67890.xml.
```

**输出结果**

经过代码处理，生成的`output.xlsx`文件内容如下：

|                URL                |
| :-------------------------------: |
| https://www.test.com/xm/12345.xml |
| https://www.test.com/xm/67890.xml |