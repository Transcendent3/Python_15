import logging
import os
from collections import namedtuple
import argparse

my_format = '{msg}'
logging.basicConfig(filename='info.txt', filemode='a', encoding='utf-8',
                    level=logging.INFO, style='{', format=my_format)
logger = logging.getLogger(__name__)

PATH = r"C:\Users\Nikolay\GB\Seminar15\task6v2.py"


def get_info_about_dirs_and_files(path: str):
    DirClass = namedtuple('DirClass', ['name', 'is_directory', 'parent_directory'])
    FileClass = namedtuple('FileClass', ['name', 'extension', 'is_directory', 'parent_directory'])
    for root, dirs, files in os.walk(path):
        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)
            dir_obj = DirClass(dir_, f'{os.path.isdir(dir_path)}',
                               dir_path.split('\\')[-2].split('/')[-1])
            logger.info(msg=f'{dir_obj}')

        for file in files:
            file_path = os.path.join(root, file)
            file_obj = FileClass(file.split('.')[0], file.split('.')[1], f'{os.path.isdir(file_path)}',
                                 file_path.split('\\')[-2].split('/')[-1])
            logger.info(msg=f'{file_obj}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Information about directories and files')
    parser.add_argument('-path', metavar='path', type=str,
                        help='enter path for get_info_about_dirs_and_files()',
                        default=os.getcwd())
    args = parser.parse_args()
    get_info_about_dirs_and_files(args.path)