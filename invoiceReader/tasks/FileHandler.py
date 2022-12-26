import pathlib
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from libs.FileType import FileType
import logging
LOGGER = logging.getLogger(__name__)
class FileHandler:
    def __init__(self) -> None:
        pass

    def filesSelector(self, directory, extension):
        """
        Select only provided extention type of files from list of files in given directory.
        :param directory: String - Directory where files exist
        :return files : List of files having same extention.
        """
        if extension not in [ext.value for ext in FileType]:
            SystemExit(1)
        extension = '.'+ extension.lower()
        filesList = os.listdir(directory)
        filesList = [file for file in filesList if pathlib.Path(file).suffix.lower() == extension]
        return filesList

    def stringToFile(self, text, destFilePath):
        """
        Write string to given file.
        :param text: String - String value to be written to file
        :param destFilePath: String - Absolute file path
        :return None
        """
        if text != None:
            with open(destFilePath, "w") as textFile:
                textFile.write(text)
            return None
        print("None type string value found to write into file, not supported for {}.".format(destFilePath))
        return None