import pathlib
import sys
import os
import shutil
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from libs.FileType import FileType
import logging
LOGGER = logging.getLogger(__name__)
from libs import CONSTANTS
class FileHandler:
    def __init__(self) -> None:
        pass

    def filesSelector(self, directory, extension):
        """
        Select only provided extention type of files from list of files in given directory.
        :param directory: String - Directory where files exist
        :return files : List of files having same extention.
        """
        print("Source directory {}".format(directory))
        if extension not in [ext.value for ext in FileType]:
            SystemExit(1)
        filesList = os.listdir(directory)
        print("RAW file list {}".format(filesList))
        print("Extention to check is {}".format(extension))
        filesList = [os.path.join(directory, file) for file in filesList if pathlib.Path(file).suffix.lower() == extension]
        return filesList

    def stringToFile(self, text, destFilePath):
        """
        Write string to given file.
        :param text: String - String value to be written to file
        :param destFilePath: String - Absolute file path
        :return None
        """
        # Uncomment below line to see o/p to be written into file
        # print(text)
        if text != None and len(text) == CONSTANTS.INVOICE_MIN_CHAR_LIMIT:
            with open(destFilePath, "w") as textFile:
                textFile.write(text)
            return None
        print("Invalid string value found to write into file, file creation failed for {}.".format(destFilePath))
        return None
    def copyFiles(self, srcFilePath, destFilePath):
       
        # source and destination folder path
        src_path = 'D:\Code\Test\source'
        dest_path = 'D:\Code\Test\Target'

        # invoice name
        inv_num = 'Test'
        extension = '.txt'
        cpy_num = ''
        i=0
        inv_name = inv_num + cpy_num + extension

        # building source and destination paths
        src_path_file_name = os.path.join(src_path, inv_name)
        dest_path_file_name = os.path.join(dest_path, inv_name)

        # check if file already exist is destination
        isExisting = os.path.exists(dest_path_file_name)

        while isExisting == True:
            i = i + 1
            cpy_num = f'({i})'
            inv_name = inv_num + cpy_num + extension
            dest_path_file_name = os.path.join(dest_path, inv_name)
            isExisting = os.path.exists(dest_path_file_name)


        # moving the file
        shutil.move(src_path_file_name, dest_path_file_name)
