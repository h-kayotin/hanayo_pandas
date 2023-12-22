"""
common - 一些常用方法

Author: hanayo
Date： 2023/12/22
"""


"""

常用的参数如下：

- `sep /delimiter`：分隔符，默认是`,`。
- `header`：表头（列索引）的位置，默认值是`infer`，用第一行的内容作为表头（列索引）。
- `index_col`：用作行索引（标签）的列。
- `usecols`：需要加载的列，可以使用序号或者列名。
- `true_values`/`false_values`：哪些值被视为布尔值`True`/`False`。
- `skiprows`：通过行号、索引或函数指定需要跳过的行。
- `skipfooter`：要跳过的末尾行数。
- `nrows`：需要读取的行数。
- `na_values`：哪些值被视为空值。

"""