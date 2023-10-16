import os
from PIL import Image, ImageEnhance
import warnings
import re
import time
from multiprocessing import Pool

warnings.filterwarnings("ignore", category=UserWarning, message=".* exceeds limit of .* pixels, could be a decompression bomb DOS attack.")
warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)

def extract_number_from_filename(filename):
    match = re.search(r'Page(\d+)', filename)
    if match:
        return int(match.group(1))
    else:
        return 0

def load_processed_images(log_file):
    processed_images = set()
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            for line in file:
                if line.startswith("Converted to"):
                    parts = line.split('to ')
                    if len(parts) >= 2:
                        processed_images.add(parts[1].strip())
    return processed_images

def process_image(input_path, output_path, desired_width, contrast, processed_images, log_file):
    if output_path in processed_images:
        print(f'Skipped {output_path} (already processed)')
        return

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
    with open(log_file, 'a') as file:
        file.write(log + '\n')

def process_images_in_pool(args):
    input_path, output_path, desired_width, contrast, processed_images, log_file = args
    process_image(input_path, output_path, desired_width, contrast, processed_images, log_file)

input_folder = input("Enter the input folder path: ")
output_folder = input("Enter the output folder path: ")
desired_width = int(input('Enter Your Desired Quality (700 to 1000): '))
contrast = float(input('Enter your desired contrast (1.5 to 2.5): '))

log_file = 'log.txt'
processed_images = load_processed_images(log_file)

if not os.path.exists(input_folder):
    print("The specified input folder does not exist.")
else:
    os.makedirs(output_folder, exist_ok=True)
    pool = Pool(processes=4)  # Adjust the number of processes as needed

args_list = []
for root, _, files in os.walk(input_folder):
    files.sort(key=lambda x: extract_number_from_filename(x))
    for image_file in files:
        if image_file.endswith('.jp2'):
            input_path = os.path.join(root, image_file)
            output_extension = 'jpg'
            relative_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.' + output_extension)

            args_list.append((input_path, output_path, desired_width, contrast, processed_images, log_file))

    pool.map(process_images_in_pool, args_list)
    pool.close()
    pool.join()

input("Press Enter to close the terminal...")
