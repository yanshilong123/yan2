from PIL import Image, ImageDraw, ImageFont
import random
import os
import subprocess

# 背景图路径
bg_path = "E:/pythondemo/img/game/bg/bg.png"

# 头像文件夹路径
avatar_folder = "E:/pythondemo/img/game/head"

# ImageMagick路径
magick_path = r"C:\Progra~1\ImageMagick-7.1.1-Q16\magick.exe"

# 加载背景图
bg_img = Image.open(bg_path)

# 设置画笔
draw = ImageDraw.Draw(bg_img) 

# 加载头像文件夹中的所有图片并排序
avatar_files = os.listdir(avatar_folder) 
avatar_files.sort()
avatars = [Image.open(os.path.join(avatar_folder, f)) for f in avatar_files]

# 创建多帧GIF图像列表
frames = []
avatar_width, avatar_height = 150, 150

# 老虎机开始转动
iterations = 10  # 老虎机旋转的轮数
frames_per_iteration = 20  # 每轮的帧数
output_folder = "output"  # 转动结果输出目录
os.makedirs(output_folder, exist_ok=True)

for iteration in range(iterations):
     for frame_number in range(frames_per_iteration):
        # 描绘老虎机框架和背景
        bg_with_frame = bg_img.copy()
        draw = ImageDraw.Draw(bg_with_frame)
        draw.rectangle((0, 0, bg_img.width, bg_img.height), fill=(211,211,211))
        draw.rectangle((100, 100, bg_img.width - 50, bg_img.height - 50), outline=(255, 255, 255), width=10)
        
        # 将头像放入老虎机的格子中
        # 将头像放入老虎机的格子中
        for i in range(3):
          for j in range(3):
         # 随机选择一个头像
           avatar_data = {
            'image': random.choice(avatars),
            'position': (100 + j * (avatar_width + 10), 100 + i * (avatar_height + 10)),
            'angle': 0,
            'rotate_speed': random.uniform(-10, 10) / 5,  # 修改旋转速度范围
            'rotate_counter': 0,
            }
        # 将头像添加到老虎机中
           bg_with_frame.paste(avatar_data['image'], box=avatar_data['position'])

# 老虎机开始转动
        for i in range(9):
          avatar_data = {
          'image': avatars[i % 3],
          'position': (100 + (i % 3) * (avatar_width + 10), 100 + (i // 3) * (avatar_height + 10)),
          'angle': 0,
          'rotate_speed': random.uniform(-10, 10) / 5,
          'rotate_counter': 0,
            }
          avatar_data_list.append(avatar_data)

        for i in range(len(avatar_data_list)):
          avatar_data = avatar_data_list[i]
          avatar_data['rotate_counter'] += avatar_data['rotate_speed']
          avatar_data['angle'] = avatar_data['rotate_counter'] * 360 / 5
          # 将头像旋转到指定的角度
          avatar = avatar_data['image'].rotate(avatar_data['angle'], resample=Image.BICUBIC, expand=True)
          # 将头像放在对应格子中，并将其旋转到指定角度
          bg_with_frame.paste(avatar, box=avatar_data['position'])

        # 输出当前帧
        output_path = os.path.join(output_folder, f"frame_{frame_number + iteration * frames_per_iteration}.jpg")
        bg_with_frame.save(output_path)

# 使用ImageMagick将所有输出的帧合成为GIF图像
subprocess.call([magick_path, "-delay", "10", os.path.join(output_folder, "frame_*.jpg"), os.path.join(output_folder, "output.gif")])