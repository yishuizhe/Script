合并两个excel的列，然后去重。

**输入示例**：

假设我们有两个Excel文件：

- `8.17-9.12.xlsx` 的内容如下：

```css
A    B  
1    apple    10  
2    banana   20  
3    cherry   30
```

- `8.9-8.17xlsx` 的内容如下：

```css
A    B  
1    apple    100  
2    dragonfruit   200
```

**输出结果**：
基于上述代码，`output.xlsx` 的内容将会是：

```css
A         B  
1    apple     10  
2    banana    20  
3    cherry    30  
4    dragonfruit   200
```

在这个例子中，我们合并了两个文件中的第一列，并去除了重复项。对于重复的“apple”条目，我们只选择了`8.17-9.12.xlsx`文件中的那一个，因为其是第一个出现的。
