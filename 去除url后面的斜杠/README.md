去除excel中url后面的斜杠，列名自行修改，并去重。

**输入示例**：
假设你的`1.xlsx`文件内容如下：

| 序号 |           黑链            |
| :--: | :-----------------------: |
|  1   | http://example.com/link1/ |
|  2   | http://example.com/link2  |
|  3   | http://example.com/link3/ |
|  4   | http://example.com/link1  |
|  5   | http://example.com/link4/ |

**输出结果**：
经过你的代码处理后，生成的`output.xlsx`文件内容如下：

| 序号 |           黑链           |
| :--: | :----------------------: |
|  1   | http://example.com/link1 |
|  2   | http://example.com/link2 |
|  3   | http://example.com/link3 |
|  5   | http://example.com/link4 |

**说明**：
在这个例子中，原始的'黑链'列包含了一些URL，其中有些是重复的。代码首先去除了每个URL末尾的斜杠（如果有的话），然后去除了重复的URL，只保留了第一次出现的URL。最后，处理后的数据被保存到了新的Excel文件中。
