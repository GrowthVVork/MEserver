# Invoice Reader for CLI operation
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-src", "--source", help="Directory where invoices files exist.")
argParser.add_argument("-dest", "--destination", help="Directory where final invoices should be saved.")
argParser.add_argument("-b", "--batchSize", help="Number of files to be processed in a batch.")

args = argParser.parse_args()


src_dir = (args.source)
dest_dir = (args.destination)

if not src_dir.exists():
    print("The source directory doesn't exist")
    raise SystemExit(1)

