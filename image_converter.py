import os
from PIL import Image
from tools import convert_image
from pathlib import Path


located = False
img_format = False

while not located:

    print('Input image folder path') 
    source_folder = Path(input('>'))

    if os.path.exists(source_folder):
        print('folder located')
        destination_folder = source_folder.parent / 'converted_images' # creates a new folder in the same path as the source folder
        destination_folder.mkdir(exist_ok=True)
        located = True
    else:
        print(f'folder {source_folder} not found, try again')

while not img_format:

    print('Choose format. JPEG or PNG')
    output_format = input('>')

    if output_format.upper() in ('JPEG', 'JPG'):
        output_format = 'JPEG'
        img_format = True


    elif output_format.upper() == 'PNG':
        output_format = 'PNG'
        img_format = True

    else:
        print(f'Format {output_format} not supported')


convert_image(source_folder, destination_folder, output_format)
