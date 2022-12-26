# OCR Reader class
from multiprocessing import freeze_support
import pathlib
import os
import sys
os.environ['USE_TORCH'] = '1'
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from libs import CONSTANTS
from libs.FileType import FileType
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import re
os.add_dll_directory(CONSTANTS.GTK_DLLS_ABS_PATH)
class ocrReader:
    def __init__(self) -> None:
        pass
    def ocrParser(self, filePath):
        """
        Scan given supported file and return list of strings.
        :param filePath: String - Absolute Path of file
        :return texts : List of strings - Text version 
        """
        fileExtention = pathlib.Path(filePath).suffix.lower()
        if fileExtention == FileType.PDF.value:
            doc = DocumentFile.from_pdf(filePath)
            print("Found PDF type file {}".format(filePath))
        elif fileExtention == FileType.PNG.value:
            doc = DocumentFile.from_images([filePath])
            print("Found PNG type file {}".format(filePath))
        else:
            print("Given file is of unsuppported type.")
            return None
        return self.__stringConversion(doc)

    def __stringConversion(self, document):
        """
        Do ocr on given document and return return list of strings.
        :param document: String - Absolute Path of file
        :return texts : List of strings - Text version 
        """
        texts = []
        predictor = ocr_predictor(pretrained=True)
        result = predictor(document)
        json_export = result.export()
        # Uncomment below line to see complete document analysis
        # print(json_export)
        for page in json_export['pages']:
            for block in page['blocks']:
                for line in block['lines']:
                    for word in line['words']:
                        texts.append(word['value'])
        return texts

# To test this module please uncomment below lines and execute the file
# if __name__ == '__main__':
#     testFile = CONSTANTS.TEST_38badpng_FILE
#     freeze_support()
#     parser = ocrReader()
#     texts = parser.ocrParser(testFile)
#     for text in texts:
#         if re.findall(CONSTANTS.INVOICE_MATCHING_PATTERN, text):
#             print(text)







