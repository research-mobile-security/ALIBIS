import os
import shutil
import zipfile

def unzip_and_move_files(source_dir, destination_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(root)
                    print(f"Successfully extracted {file}")
                    shutil.move(zip_path, os.path.join(destination_dir, file))
                except Exception as e:
                    print(f"Error extracting {file}: {e}")
                    continue

source_directory = r'.\decompile-code'
destination_directory = r'.\done'

unzip_and_move_files(source_directory, destination_directory)
