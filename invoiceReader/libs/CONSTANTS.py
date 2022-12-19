TESSERACT_EXE_ABS_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_BIN_ABS_PATH = r'C:\Program Files\poppler-0.68.0\bin'
from pathlib import Path
mod_path = Path(__file__).parent.parent
TEST_PDF_FILE = (mod_path / 'test/' / 'Tejas__Kothari.pdf').resolve()
TEST_IMG_FILE = (mod_path / 'test/' / 'test.png').resolve()