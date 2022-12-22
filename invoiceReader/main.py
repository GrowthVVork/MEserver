# Invoice Reader for CLI operation
import argparse
import logging
import logging.config
import os
from datetime import datetime
# from dotenv import find_dotenv, load_dotenv

# find .env file in parent directory
# env_file = find_dotenv()
# load_dotenv()

CONFIG_DIR = "./config"
LOG_DIR = "./logs"

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

def setup_logging():
    """Load logging configuration"""
    log_configs = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}
    config = log_configs.get(os.environ["ENV"], "logging.dev.ini")
    config_path = "/".join([CONFIG_DIR, config])

    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )

