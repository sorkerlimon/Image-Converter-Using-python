
import os
from PIL import Image, ImageEnhance
import warnings
import re,time

warnings.filterwarnings("ignore", category=UserWarning, message=".* exceeds limit of .* pixels, could be decompression bomb DOS attack.")
warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)

print('''
                                                █████ █████ ██████   ██████ █████      
                                                 ███   ███   ██████ ██████   ███       
                                                 ███   ███   ███  ███  ███   ███                   
                                                 ███   ███   ███       ███   ███    
                                                █████ █████ █████     █████ █████
                                                            Image Converter V3.2 (System Team)                                                           
''')



def extract_number_from_filename(filename):
    match = re.search(r'Page(\d+)', filename)
    if match:
        return int(match.group(1))
    else:
        return 0

username = input("Login Username: ")
password = input("Login Password: ")




if username == 'iimi' and password == 'iimi':
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    desired_width = int(input('Enter Your Desired Quality (700 to 1000) : '))
    contrast = float(input('Enter your desired contrast (1.5 to 2.5) : '))

    if not os.path.exists(input_folder):
        print("The specified input folder does not exist.")
    else:
        os.makedirs(output_folder, exist_ok=True)

        for root, _, files in os.walk(input_folder):
            # Sort files based on the sequence in their names
            files.sort(key=lambda x: extract_number_from_filename(x))
            for image_file in files:
                if image_file.endswith('.jp2'):
                    input_path = os.path.join(root, image_file)
                    output_extension = 'jpg'
                    relative_path = os.path.relpath(input_path, input_folder)
                    output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.' + output_extension)

                    jp2_image = Image.open(input_path)

                    Image.MAX_IMAGE_PIXELS = None

                    width, height = jp2_image.size
                    new_height = int(desired_width * height / width)
                    target_size = (desired_width, new_height)
                    resized_image = jp2_image.convert('RGB').resize(target_size)
                    enhancer = ImageEnhance.Contrast(resized_image)
                    enhanced_image = enhancer.enhance(contrast)

                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    enhanced_image.save(output_path, 'JPEG')
                    print(f'Converted to {output_path}')
                    log = f"Converted to {output_path}"
                    with open('log.txt', 'a') as file:
                        file.write(log + '\n')
else:
    print('User name password wrong')
    time.sleep(2)
# pyinstaller --onefile 
# pyinstaller --onefile --icon=C:\Users\21100002\Desktop\ImageIIML\logo.ico Image-Converter-v3.py

