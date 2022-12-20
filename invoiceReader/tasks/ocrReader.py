# OCR Reader class
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from PIL import Image
import numpy
import pytesseract
from invoiceReader.libs import CONSTANTS
from invoiceReader.libs.FileType import FileType
from pdf2image import convert_from_path
import pathlib

# PyTesseract process
pytesseract.pytesseract.tesseract_cmd = CONSTANTS.TESSERACT_EXE_ABS_PATH

# filePath = CONSTANTS.TEST_PDF_FILE
class ocrReader:
    def __init__(self) -> None:
        pass
    def ocrParser(self, filePath):
        """
        Scan given supported file and return list of strings.
        :param filePath: String - Absolute Path of file
        :return texts : List of strings - Text version 
        """
        doc = convert_from_path(filePath, 300, poppler_path=CONSTANTS.POPPLER_BIN_ABS_PATH)
        texts = []
        fileExtention = pathlib.Path(doc).suffix.lower()
        if fileExtention == FileType.PDF:
            for pageNumber, pageData in enumerate(doc):
                pageData = numpy.array(pageData)
                txt = pytesseract.image_to_string(Image.fromarray(pageData))
                texts.append(txt)
        elif fileExtention == FileType.PNG:
            txt = pytesseract.image_to_string(Image.fromarray(numpy.array(doc)))
            texts.append(txt)
        else:
            print("Given file is of unsuppported type.")
            return None
        return texts