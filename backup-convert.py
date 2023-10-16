# # # import os
# # # from PIL import Image, ImageEnhance
# # # import warnings
# # # import re,time

# # # warnings.filterwarnings("ignore", category=UserWarning, message=".* exceeds limit of .* pixels, could be decompression bomb DOS attack.")
# # # warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)

# # # print('''
# # #                                                 █████ █████ ██████   ██████ █████      
# # #                                                  ███   ███   ██████ ██████   ███       
# # #                                                  ███   ███   ███  ███  ███   ███                   
# # #                                                  ███   ███   ███       ███   ███    
# # #                                                 █████ █████ █████     █████ █████
# # #                                                             Image Converter V3.0 (System Team)                                                           
# # # ''')



# # # def extract_number_from_filename(filename):
# # #     match = re.search(r'Page(\d+)', filename)
# # #     if match:
# # #         return int(match.group(1))
# # #     else:
# # #         return 0

# # # username = input("Login Username: ")
# # # password = input("Login Password: ")

# # # if username == 'iimi' and password == 'iimi':
# # #     input_folder = input("Enter the input folder path: ")
# # #     output_folder = input("Enter the output folder path: ")
# # #     desired_width = int(input('Enter Your Desired Quality (700 to 1000) : '))

# # #     if not os.path.exists(input_folder):
# # #         print("The specified input folder does not exist.")
# # #     else:
# # #         os.makedirs(output_folder, exist_ok=True)

# # #         for root, _, files in os.walk(input_folder):
# # #             # Sort files based on the sequence in their names
# # #             files.sort(key=lambda x: extract_number_from_filename(x))
# # #             for image_file in files:
# # #                 if image_file.endswith('.jp2'):
# # #                     input_path = os.path.join(root, image_file)
# # #                     output_extension = 'png'
# # #                     relative_path = os.path.relpath(input_path, input_folder)
# # #                     output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.' + output_extension)

# # #                     jp2_image = Image.open(input_path)

# # #                     Image.MAX_IMAGE_PIXELS = None

# # #                     width, height = jp2_image.size
# # #                     new_height = int(desired_width * height / width)
# # #                     target_size = (desired_width, new_height)
# # #                     resized_image = jp2_image.convert('RGB').resize(target_size)
# # #                     enhancer = ImageEnhance.Contrast(resized_image)
# # #                     enhanced_image = enhancer.enhance(1.5)

# # #                     os.makedirs(os.path.dirname(output_path), exist_ok=True)
# # #                     enhanced_image.save(output_path, 'PNG')
# # #                     print(f'Converted to {output_path}')
# # #                     log = f"Converted to {output_path}"
# # #                     with open('log.txt', 'a') as file:
# # #                         file.write(log + '\n')
# # # else:
# # #     print('User name password wrong')
# # #     time.sleep(5)
# # # #pyinstaller --onefile 
# # # #pyinstaller --onefile --icon=C:\Users\21100002\Desktop\ImageIIML\logo.ico Image-Converter-v3.py


# # # # import os
# # # # from PIL import Image

# # # # # # Input and output folder paths
# # # # input_folder = r'C:\Users\21100002\Desktop\ImageIIML\F_Images'
# # # # output_folder = r'C:\Users\21100002\Desktop\ImageIIML\C_Images'

# # # # # os.makedirs(output_folder, exist_ok=True)

# # # # # image_files = [f for f in os.listdir(input_folder) if f.endswith('.jp2')]
# # # # # print(len(image_files))

# # # # # for image_file in image_files:
# # # # #     input_path = os.path.join(input_folder, image_file)
# # # # #     output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.jpg')
    
# # # # #     jp2_image = Image.open(input_path)
# # # # #     jp2_image.convert('RGB').save(output_path, 'JPEG')
# # # # #     print(f"Converted {input_path} to {output_path}")


# # # # import os
# # # # # from PIL import Image, ImageEnhance

# # # # # os.makedirs(output_folder, exist_ok=True)

# # # # # image_files = [f for f in os.listdir(input_folder) if f.endswith('.jp2')]
# # # # # print(len(image_files))

# # # # # for image_file in image_files:
# # # # #     input_path = os.path.join(input_folder, image_file)
# # # # #     output_extension = 'png'  # Save all images in PNG format
# # # # #     output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.' + output_extension)
    
# # # # #     # Open the JP2 image
# # # # #     jp2_image = Image.open(input_path)
    
# # # # #     # Resize the image (optional)
# # # # #     target_size = (800, 600)
# # # # #     resized_image = jp2_image.convert('RGB').resize(target_size)
    
# # # # #     # Apply contrast enhancement (optional)
# # # # #     enhancer = ImageEnhance.Contrast(resized_image)
# # # # #     enhanced_image = enhancer.enhance(1.5)  # Adjust contrast (1.0 means no change)
    
# # # # #     # Save the image in PNG format
# # # # #     enhanced_image.save(output_path, 'PNG')
    
# # # # #     print(f"Converted {input_path} to {output_path}")



# # # # os.makedirs(output_folder, exist_ok=True)

# # # # image_files = [f for f in os.listdir(input_folder) if f.endswith('.jp2')]
# # # # print(len(image_files))

# # # # # Set the desired width for resizing (e.g., 1000 pixels)
# # # # desired_width = 850

# # # # for image_file in image_files:
# # # #     input_path = os.path.join(input_folder, image_file)
# # # #     output_extension = 'png'  # Save all images in PNG format
# # # #     output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.' + output_extension)
    
# # # #     # Open the JP2 image
# # # #     jp2_image = Image.open(input_path)
    
# # # #     # Calculate the new height while maintaining the aspect ratio
# # # #     width, height = jp2_image.size
# # # #     new_height = int(desired_width * height / width)
    
# # # #     # Resize the image to the desired width while maintaining aspect ratio
# # # #     target_size = (desired_width, new_height)
# # # #     resized_image = jp2_image.convert('RGB').resize(target_size)
    
# # # #     # Apply contrast enhancement (optional)
# # # #     enhancer = ImageEnhance.Contrast(resized_image)
# # # #     enhanced_image = enhancer.enhance(1.5)  # Adjust contrast (1.0 means no change)
    
# # # #     # Save the image in PNG format
# # # #     enhanced_image.save(output_path, 'PNG')
    
# # # #     print(f"Converted {input_path} to {output_path}")


# # # import os
# # # from PIL import Image, ImageEnhance
# # # import warnings

# # # warnings.filterwarnings("ignore", category=UserWarning, message=".* exceeds limit of .* pixels, could be decompression bomb DOS attack.")

# # # input_folder = r'C:\Users\21100002\Desktop\ImageIIML\F_Images'
# # # output_folder = r'C:\Users\21100002\Desktop\ImageIIML\C_Images'
# # # print('Image Converter V2.0')

# # # if not os.path.exists(input_folder):
# # #     print("The specified input folder does not exist.")
# # # else:
# # #     os.makedirs(output_folder, exist_ok=True)

# # #     for root, _, files in os.walk(input_folder):
# # #         for image_file in files:
# # #             if image_file.endswith('.jp2'):
# # #                 input_path = os.path.join(root, image_file)
# # #                 output_extension = 'png' 
# # #                 relative_path = os.path.relpath(input_path, input_folder)
# # #                 output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.' + output_extension)

# # #                 jp2_image = Image.open(input_path)

# # #                 desired_width = 850
# # #                 Image.MAX_IMAGE_PIXELS = None

# # #                 width, height = jp2_image.size
# # #                 new_height = int(desired_width * height / width)
# # #                 target_size = (desired_width, new_height)
# # #                 resized_image = jp2_image.convert('RGB').resize(target_size)
# # #                 enhancer = ImageEnhance.Contrast(resized_image)
# # #                 enhanced_image = enhancer.enhance(1.5)

# # #                 os.makedirs(os.path.dirname(output_path), exist_ok=True)
# # #                 enhanced_image.save(output_path, 'PNG')
# # #                 print(f'Converted to {output_path}')
# # #                 log = f"Converted to {output_path}"
# # #                 with open('log.txt', 'a') as file:
# # #                     file.write(log + '\n')

# # import os
# # from PIL import Image, ImageEnhance
# # import warnings

# # # Ignore the DecompressionBombWarning
# # warnings.filterwarnings("ignore", category=UserWarning, message=".* exceeds limit of .* pixels, could be decompression bomb DOS attack.")

# # input_folder = r'C:\Users\21100002\Desktop\ImageIIML\F_Images'
# # output_folder = r'C:\Users\21100002\Desktop\ImageIIML\C_Images'
# # print('Image Converter V2.0')
# # # input_folder = input("Enter the input folder path: ")
# # # output_folder = input("Enter the output folder path: ")

# # # Check if the input folder exists
# # # if not os.path.exists(input_folder):
# # #     print("The specified input folder does not exist.")
# # # else:
# # #     os.makedirs(output_folder, exist_ok=True)

# # #     image_files = [f for f in os.listdir(input_folder) if f.endswith('.jp2')]
# # #     print(f'Totall Image Length {len(image_files)}')
# # #     desired_width = 850
# # #     # desired_width = int(input('Enter Your Desired Quality (700 to 1000) : '))
# # #     Image.MAX_IMAGE_PIXELS = None

# # #     for image_file in image_files:
# # #         input_path = os.path.join(input_folder, image_file)
# # #         output_extension = 'png' 
# # #         output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.' + output_extension)

# # #         jp2_image = Image.open(input_path)
        
# # #         width, height = jp2_image.size
# # #         new_height = int(desired_width * height / width)
# # #         target_size = (desired_width, new_height)
# # #         resized_image = jp2_image.convert('RGB').resize(target_size)
# # #         enhancer = ImageEnhance.Contrast(resized_image)
# # #         enhanced_image = enhancer.enhance(1.5)  
        
# # #         enhanced_image.save(output_path, 'PNG')
# # #         print(f'Converted to {output_path}')
# # #         log = f"Converted to {output_path}"
# # #         with open('log.txt', 'a') as file:
# # #             file.write(log + '\n')

# # if not os.path.exists(input_folder):
# #     print("The specified input folder does not exist.")
# # else:
# #     os.makedirs(output_folder, exist_ok=True)

# #     for root, _, files in os.walk(input_folder):
# #         for image_file in files:
# #             if image_file.endswith('.jp2'):
# #                 input_path = os.path.join(root, image_file)
# #                 output_extension = 'png' 
# #                 relative_path = os.path.relpath(input_path, input_folder)
# #                 output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.' + output_extension)

# #                 jp2_image = Image.open(input_path)

# #                 desired_width = 850
# #                 Image.MAX_IMAGE_PIXELS = None

# #                 width, height = jp2_image.size
# #                 new_height = int(desired_width * height / width)
# #                 target_size = (desired_width, new_height)
# #                 resized_image = jp2_image.convert('RGB').resize(target_size)
# #                 enhancer = ImageEnhance.Contrast(resized_image)
# #                 enhanced_image = enhancer.enhance(1.5)

# #                 os.makedirs(os.path.dirname(output_path), exist_ok=True)
# #                 enhanced_image.save(output_path, 'PNG')
# #                 print(f'Converted to {output_path}')
# #                 log = f"Converted to {output_path}"
# #                 with open('log.txt', 'a') as file:
# #                     file.write(log + '\n')
# import pytesseract
# from PIL import Image
# import cv2

# # Set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Open an image using Pillow (PIL)
# image_path = r'C:\Users\21100002\Desktop\ImageIIML\tesserectimage.jpg'  # Replace with the path to your image
# # image_path = r'C:\Users\21100002\Desktop\ImageIIML\C_Images\3380-15=3380-15_01_JA==Page490.jpg'  # Replace with the path to your image

# img = cv2.imread(image_path)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
 
# dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
#                                                  cv2.CHAIN_APPROX_NONE)
 
# im2 = img.copy()
 
# # A text file is created and flushed
# file = open("recognized.txt", "w+")
# file.write("")
# file.close()
 
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     cropped = im2[y:y + h, x:x + w]
#     file = open("recognized.txt", "a")
#     text = pytesseract.image_to_string(cropped)
#     file.write(text)
#     file.write("\n")
#     file.close



# Working code 

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
    time.sleep(5)
# pyinstaller --onefile 
# pyinstaller --onefile --icon=C:\Users\21100002\Desktop\ImageIIML\logo.ico Image-Converter-v3.py





import os
from PIL import Image, ImageEnhance
import warnings
import re
import time

# Filter out warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".* exceeds limit of .* pixels, could be decompression bomb DOS attack.")
warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)

def extract_number_from_filename(filename):
    match = re.search(r'Page(\d+)', filename)
    if match:
        return int(match.group(1))
    else:
        return 0

def process_image(input_path, output_path, desired_width, contrast):
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
            files.sort(key=lambda x: extract_number_from_filename(x))
            for image_file in files:
                if image_file.endswith('.jp2'):
                    input_path = os.path.join(root, image_file)
                    output_extension = 'jpg'
                    relative_path = os.path.relpath(input_path, input_folder)
                    output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.' + output_extension)

                    process_image(input_path, output_path, desired_width, contrast)
else:
    print('User name password wrong')
    time.sleep(5)
