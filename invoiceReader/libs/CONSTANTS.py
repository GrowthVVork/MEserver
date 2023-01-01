GTK_DLLS_ABS_PATH = r"C:\Program Files\GTK3-Runtime Win64\bin"
INVOICE_MATCHING_PATTERN = r'..+[/.-]\d+[/.-]\d+'
INVOICE_MIN_CHAR_LIMIT = 11
from pathlib import Path
mod_path = Path(__file__).parent.parent
TEST_PDF_FILE = (mod_path / 'test/' / '37bad.pdf').resolve()
TEST_IMG_FILE = (mod_path / 'test/' / 'image_1.png').resolve()
TEST_36badpng_FILE = (mod_path / 'test/' / '36bad.png').resolve()
TEST_37badpng_FILE = (mod_path / 'test/' / '37bad.png').resolve()
TEST_38badpng_FILE = (mod_path / 'test/' / '38bad.png').resolve()
TEST_37bestpng_FILE = (mod_path / 'test/' / '37best.png').resolve()
TEST_37bestpngcrop_FILE = (mod_path / 'test/' / '37bestcrop.png').resolve()
LEFT_DIVISOR_VALUE = 2
RIGHT_DIVISOR_VALUE = 3/4
TOP_DIVISOR_VALUE = 15
BOTTOM_DIVISOR_VALUE = 4