import PyPDF2
import os
from PIL import Image
import sys
import cv2
import pytesseract

pdf = open(str(sys.argv[1]) , 'rb')
reader = PyPDF2.PdfFileReader(pdf)

pages = reader.getNumPages()

for i in range(1,pages-1):
    page = reader.getPage(i)
    temp = page.extractText()
    with open("sample.txt", "a") as file_object:
        file_object.write(temp)
    xObject = page['/Resources']['/XObject'].getObject()

    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj].getData()
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"
            if '/Filter' in xObject[obj]:
                if xObject[obj]['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode,size,data)
                    img.save(obj[1:] + ".png")
                elif xObject[obj]['/Filter'] == '/DCTDecode':
                    img = open(obj[1:] + ".jpg", "wb")
                    img.write(data)
                    img.close()
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    img = open(obj[1:] + ".jp2", "wb")
                    img.write(data)
                    img.close()
                elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                    img = open(obj[1:] + ".tiff", "wb")
                    img.write(data)
                    img.close()
                else:
                    img = Image.frombytes(mode, size, data)
                    img.save(obj[1:] + ".png")
            else:
                print("No image found.")


folder = os.getcwd()
element = os.listdir(folder)


for i in element:
    img = cv2.imread(os.path.join(folder,i))
    if img is not None:
        text = pytesseract.image_to_string(img)
        text_file = open(str(i)+'.m','w')
        n = text_file.write(text)
        text_file.close()

