# OCR Reader class
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from PIL import Image
import numpy
import pytesseract
from invoiceReader.libs import CONSTANTS
from pdf2image import convert_from_path
import pathlib
# PyTesseract process
pytesseract.pytesseract.tesseract_cmd = CONSTANTS.TESSERACT_EXE_ABS_PATH

# filePath = CONSTANTS.TEST_PDF_FILE

def fileToString(filePath):
    """
    Scan given PDF/IMG file and return list of strings.
    :param filePath: String - Absolute Path of file
    :return texts : List of strings - Text version 
    """
    doc = convert_from_path(filePath, 300, poppler_path=CONSTANTS.POPPLER_BIN_ABS_PATH)
    texts = []
    for pageNumber, pageData in enumerate(doc):
        pageData = numpy.array(pageData)
        txt = pytesseract.image_to_string(Image.fromarray(pageData))
        texts.append(txt)
    return texts

def PdfFiles(directory):
    """
    Select only PDFs from list of files in given directory.
    :param directory: String - Directory where files exist
    :return files : List of validated files.
    """
    filesList = os.listdir(directory)
    filesList = [file for file in filesList if pathlib.Path(file).suffix.lower() == '.pdf']
    return filesList

