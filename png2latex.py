import os
import subprocess

# 指定图像文件夹路径和输出文本文件路径
image_folder = '/home/gongzhenni/nougat-latex-ocr/examples/test_data'  # 更改为你的图像文件夹路径
output_file = '/home/gongzhenni/nougat-latex-ocr/examples/test_data/1-15_extracted.txt'  # 输出文本文件名

# 获取文件夹中所有图片文件，并按文件名排序
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png') or f.endswith('.jpg')])

# 逐个处理图片并识别 LaTeX 内容
with open(output_file, 'w') as txt_output:
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        
        # 构建识别命令
        command = f'python /home/gongzhenni/nougat-latex-ocr/examples/run_latex_ocr.py --img_path "{image_path}"'
        
        # 运行命令并获取输出结果
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # 检查命令是否成功运行并写入识别内容到输出文本文件
        if result.returncode == 0:
            latex_content = result.stdout.strip()  # 获取识别的 LaTeX 内容
            print(f"{image_file.split('.')[0]}: {latex_content}")
            txt_output.write(f"{image_file.split('.')[0]}: {latex_content}\n")  # 写入文件名和 LaTeX 内容
        else:
            print(f"Error processing file: {image_file}")

print(f"识别完成")
