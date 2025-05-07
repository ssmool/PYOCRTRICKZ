import sys
from py_ocr import getOCR, getOCRText

file_path = sys.argv[1]
r_x = getOCR(file_path)
l_x = getOCRText(r_x)
print(f'Result Text from Image={str(r_x)}')
print(f'Result Text from Image={l_x}')

