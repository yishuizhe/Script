指定目录中的多个Excel（.xlsx）文件中提取第一列的数据，并将这些数据合并到一个新的Excel文件中。

**输入示例**：

假设在目录`/Users/peiyimiao/Desktop/未命名文件夹/`下有如下两个Excel文件：

1. `file1.xlsx` 的内容：

|  A   |
| :--: |
|  1   |
|  2   |
|  3   |

1. `file2.xlsx` 的内容：

|  A   |
| :--: |
|  4   |
|  5   |
|  6   |

**输出结果示例**：

执行上述代码后，会生成一个新的Excel文件`merged_data.xlsx`，其内容如下：

```markdown
FirstColumn  
-----------  
1  
2  
3  
4  
5  
6`
```

这个新的Excel文件`merged_data.xlsx`包含了`file1.xlsx`和`file2.xlsx`两个文件的第一列数据，并且这些数据按照从原始文件中提取的顺序进行了排序。
