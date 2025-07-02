import os
from PIL import Image

def convert_image(source, destination, output_format):
    
    for filename in os.listdir(source):
        input_path = os.path.join(source, filename)
        base_filename = os.path.splitext(filename)[0]
        output_filename = f'{base_filename}.{output_format}'
        output_path = os.path.join(destination, output_filename)

        try:
            with Image.open(input_path) as img:
                img.save(output_path, format=output_format)
            print(f'Converted {filename} to {output_filename}')
        except Exception as e:
            print(f'Error converting {filename}: {e}')

    print('Image conversion completed.')