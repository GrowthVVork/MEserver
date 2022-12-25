GTK_DLLS_ABS_PATH = r"C:\Program Files\GTK3-Runtime Win64\bin"
# INVOICE_MATCHING_PATTERN = 
from pathlib import Path
mod_path = Path(__file__).parent.parent
TEST_PDF_FILE = (mod_path / 'test/' / '37bad.pdf').resolve()
TEST_IMG_FILE = (mod_path / 'test/' / 'image_1.png').resolve()
TEST_37badpng_FILE = (mod_path / 'test/' / '37bad.png').resolve()
TEST_37bestpng_FILE = (mod_path / 'test/' / '37best.png').resolve()
TEST_37bestpngcrop_FILE = (mod_path / 'test/' / '37bestcrop.png').resolve()