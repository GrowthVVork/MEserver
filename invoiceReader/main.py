# Invoice Reader for CLI operation
import argparse
from multiprocessing import freeze_support
import os
from datetime import datetime
from tasks.ocrReader import ocrReader
from tasks.FileHandler import FileHandler
from pathlib import Path
import logging
# Below line is to see all imported modules and their respective logger info
# logging.Logger.manager.loggerDict

argParser = argparse.ArgumentParser()
argParser.add_argument("-src", "--source", help="Directory where invoices files exist.")
argParser.add_argument("-dest", "--destination", help="Directory where final invoices should be saved.")
argParser.add_argument("-b", "--batchSize", help="Number of files to be processed in a batch.")

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
    if args.destination == None:
        print("The destination directory doesn't exist")
        raise SystemExit(1)
    for file in os.listdir(args.source):
        completeFilePath = os.path.join(args.source, file)
        destinationFile = os.path.splitext(completeFilePath)[0]
        destinationFile += ".txt"
        # To see input file, uncomment below line
        # print(file)
        val = parser.ocrParser(completeFilePath)
        if val is not None:
            val = ''.join([item for item in val])
        fileHandle.stringToFile(val, destinationFile)

# How to run :-
# python  d:/GrowthVVork/MEserver/invoiceReader/main.py -src D:\GrowthVVork\MEserver\invoiceReader\test\ -dest D:\GrowthVVork\MEserver\invoiceReader\test\