import os
import shutil

# 文件分类字典，可以根据需要修改或扩展
file_types = {
    '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    '文档': ['.pdf', '.docx', '.txt', '.ppt', '.xlsx'],
    '视频': ['.mp4', '.mkv', '.avi', '.mov'],
    '音频': ['.mp3', '.wav', '.aac'],
    '压缩文件': ['.zip', '.rar', '.tar', '.7z'],
    '代码': ['.py', '.java', '.cpp', '.html', '.js']
}

# 定义文件夹分类
def classify_files(src_folder):
    # 遍历文件夹
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()  # 获取文件后缀名并转换为小写
            moved = False
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    category_folder = os.path.join(src_folder, category)
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)  # 如果分类文件夹不存在就创建
                    shutil.move(file_path, os.path.join(category_folder, filename))  # 移动文件
                    moved = True
                    print(f"移动文件 {filename} 到 {category_folder}")
                    break

            if not moved:
                # 对于没有匹配到的文件，放入一个 '其他' 文件夹
                other_folder = os.path.join(src_folder, '其他')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"移动文件 {filename} 到 {other_folder}")

if __name__ == "__main__":
    # 设置源文件夹路径
    source_folder = r"C:\Users\Lk9\Downloads"  # 修改为你要整理的文件夹路径
    classify_files(source_folder)
