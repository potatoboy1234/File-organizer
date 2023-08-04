# IMPORTING MODULES
import os
import shutil
import json as json
import sys


# PARSING JSON INTO A DICTIONARY AND SETTING THE TARGET DIRECTORY

if __name__ == '__main__':
    file_formats = dict()
    target_directory = '/filepath' # NEED TO CHANGE
    

with open('file_formats.json', 'r') as file:
    file_formats = json.load(file) 


# DEFINING A FUNCTION THAT TAKES THE JSON DICTIONART AND THE PATH TO THE FOLDER

def clean_folder(file_formats: dict, target_directory: str):
    print(f"Cleaning {target_directory} folder...")

    dir_content = os.listdir(target_directory)
    # FOR EACH ITEM IN THE DIRECTORY WE MAKE SURE THAT IT'S NOT A FOLDER
    for d_file in dir_content:
        try:
            if os.path.isdir(d_file):
                continue # CHECKS IF IT'S A DIRECTORY AND SKIPS TO CONTINUE THE LOOP

            file_name, file_extension = os.path.splitext(d_file)
            if not file_extension.lower() in file_formats:
                continue # CHECKING IF THE EXTENSION IS NOT IN OUR JSON FILE

            target_path = f'{target_directory}/{file_formats[file_extension.lower()]}'
            if not os.path.isdir(target_path):
                os.mkdir(target_path) 
                # LOOKS FOR THE FOLDER WE WANT TO PUT THE FILE. IF IT DOESN't EXIST - CREATE IT


            # MOVES THE FILES INTO THE TARGET PATH FROM THEIR ORIGINAL FOLDERS
            src_path = f'{target_directory}/{d_file}'
            dst_path = f'{target_path}/{d_file}'

            shutil.copyfile(src=src_path, dst=dst_path)

            os.remove(src_path)

        except:
            print(f'Failed to move {d_file}')
    print(f'Successfully finished cleaning {target_directory}')            


if len(file_formats) == 0:
    print('Failed to clean - missing file formats.')    
else:
    clean_folder(file_formats=file_formats, target_directory=target_directory)   
