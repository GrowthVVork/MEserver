import pathlib
import sys
import os
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