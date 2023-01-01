import pathlib
import sys
import os
import shutil
from PIL import Image
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
            print("Unsupported type found!")
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
    
    def moveFile(self, srcFilePath, destinationPath, fileTypeValue, customName = None, overrideFlag = False):
        """
        Move given file to destination.
        :param srcFilePath: String - Source file path
        :param destinationPath: String - Destination file path
        :param fileTypeValue: FileType value
        :param customName: String - Custom file name
        :param overrideFlag: Boolean - Flag to override destination file if exists already
        :return None
        """
        if customName is not None:
            destinationFile = destinationPath + customName + fileTypeValue
        else:
            destinationFile = destinationPath +  srcFilePath.rpartition('\\')[-1]
        # Check if file already exist is destination
        fileExists = os.path.exists(destinationFile)
        if fileExists and overrideFlag:
            print("{} file exists, overriding.".format(destinationFile))
        elif fileExists and overrideFlag == False:
            originalDestFile = destinationFile
            i = 1
            while fileExists:
                print("{} file exists, appending number {} at file end.".format(destinationFile, i))
                destinationFile = originalDestFile.split('.')[0] + '_' + str(i) + '.' + originalDestFile.split('.')[1]
                fileExists = os.path.exists(destinationFile)
                i+=1
        # Moving the file
        shutil.move(srcFilePath, destinationFile)
        return
        
    def cropFile(self, srcFilePath ):
        # Opens image
        image = Image.open(srcFilePath)
        width, height = image.size

        # Setting the points for cropped image
        left = width/2
        top = height/15
        right = width * 3/4
        bottom = height/4
        
        # Crop image of above dimension
        cropImage = image.crop((left, top, right, bottom))
        
        # im1.show() Shows the image in image viewer
        return cropImage
        
