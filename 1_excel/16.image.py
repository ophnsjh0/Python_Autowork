from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img2.png")

# C3 위치에 test.png 이미지 삽입
ws.add_image(img, "A4")

wb.save("sample_image.xlsx")
