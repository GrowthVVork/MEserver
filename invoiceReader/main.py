# Invoice Reader for CLI operation
import argparse
from multiprocessing import freeze_support
import os
from datetime import datetime
from tasks.ocrReader import ocrReader
from tasks.FileHandler import FileHandler
from pathlib import Path
import re
import logging
from libs import CONSTANTS
from libs.FileType import FileType
# Below line is to see all imported modules and their respective logger info
# logging.Logger.manager.loggerDict

argParser = argparse.ArgumentParser()
argParser.add_argument("-src", "--source", help="Directory where invoices files exist.")
argParser.add_argument("-dest", "--destination", help="Directory where final invoices should be saved.")
argParser.add_argument("-bSize", "--batchSize", help="Number of files to be processed in a batch.")
argParser.add_argument("-type", "--fileType", help="Type of file to process.")
if __name__ == '__main__':
    # testFile = r'D:\GrowthVVork\MEserver\invoiceReader\test\37bad.png'
    # print(logging.Logger.manager.loggerDict)
    parser = ocrReader()
    fileHandle = FileHandler()
    freeze_support()
    args = argParser.parse_args()
    if args.source == None:
        print("The source directory doesn't exist")
        raise SystemExit(1)
    if args.destination == None or not os.path.exists(args.destination):
        print("The destination directory doesn't exist")
        os.makedirs(args.destination)
        print("Created the destination directory {}".format(args.destination))
        # raise SystemExit(1)
    args.fileType = args.fileType.lower()
    if args.fileType not in [ext.value for ext in FileType]:
            SystemExit(1)
    validFileList = fileHandle.filesSelector(args.source, args.fileType)
    # print(validFileList)
    for file in validFileList:
        # To see input file, uncomment below line
        # print(file)
        val = parser.ocrParser(file)
        outputText = ''
        for text in val:
            if re.findall(CONSTANTS.INVOICE_MATCHING_PATTERN, text):
                outputText = 'SI' + text[2:]
                # SI/07336/19 as file name is not allowed :)
                outputText = outputText.replace('/', '_')
                fileHandle.moveFile(file, args.destination, args.fileType, outputText)

# How to run :-
# python d:/Workshiz/MEserver/invoiceReader/main.py -src D:\Workshiz\MEserver\invoiceReader\test\ -dest D:\Workshiz\MEserver\invoiceReader\output\ -type .png