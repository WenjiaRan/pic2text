import os

# 定义要处理的文本文件的路径
input_file = './result.txt'

# 定义要保存处理结果的文本文件的路径
output_file = './result_clean.txt'

# 遍历文本文件中的所有行，删除包含"微信图片_数字.png:"的行
with open(input_file, 'r', encoding='utf-8') as f1, open(output_file, 'w', encoding='utf-8') as f2:
    for line in f1:
        if '微信图片_' not in line:
            f2.write(line)