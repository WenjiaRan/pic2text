import os
from aip import AipOcr

# 配置百度OCR API的参数
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

# 创建百度OCR API的客户端
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 定义要识别的图片文件夹的路径
img_dir = './pic'

# 定义要保存识别结果的文本文件的路径
output_file = './result.txt'

# 遍历图片文件夹中的所有图片
for file_name in os.listdir(img_dir):
    # 判断是否为图片文件
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # 读取图片文件
        with open(os.path.join(img_dir, file_name), 'rb') as f:
            img_data = f.read()
        # 调用百度OCR API进行文字识别
        result = client.basicGeneral(img_data)
        # 提取识别结果中的文字
        text = '\n'.join([word['words'] for word in result['words_result']])
        # 将识别结果写入文本文件
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write('{}:\n{}\n\n'.format(file_name, text))