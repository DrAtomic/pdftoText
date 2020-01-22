import PyPDF2
import os
from PIL import Image
import sys
import cv2
import pytesseract

currentFolderNum = sys.argv[1][::-1].find('/')
currentFolder = sys.argv[1][:-currentFolderNum]

pdf = open(str(sys.argv[1]) , 'rb')
reader = PyPDF2.PdfFileReader(pdf)

pages = reader.getNumPages()

def imagetoText(img):
    text = pytesseract.image_to_string(img)
    text_file = open(img +'.txt','w')
    n = text_file.write(text)
    text_file.close()


for i in range(pages):
    page = reader.getPage(i)
    temp = page.extractText()
    x = os.path.join(currentFolder, "sample.txt")
    with open(x, "a") as file_object:
        file_object.write(temp)
    if '/XObject' in page['/Resources'].keys():
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
                        x = os.path.join(currentFolder,obj[1:] + ".png")
                        img.save(x)
                        imagetoText(x)
                    elif xObject[obj]['/Filter'] == '/DCTDecode':
                        img = open(obj[1:] + ".jpg", "wb")
                        img.write(data)
                        img.close()
                        x = os.path.join(currentFolder,obj[1:] + ".jpg")
                        imagetoText(x)
                    elif xObject[obj]['/Filter'] == '/JPXDecode':
                        img = open(obj[1:] + ".jp2", "wb")
                        img.write(data)
                        img.close()
                        x = os.path.join(currentFolder,obj[1:] + ".jp2")
                        imagetoText(x)
                    elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                        img = open(obj[1:] + ".tiff", "wb")
                        img.write(data)
                        img.close()
                        x = os.path.join(currentFolder,obj[1:] + ".tiff")
                        imagetoText(x)
                    else:
                        img = Image.frombytes(mode, size, data)
                        img.save(obj[1:] + ".png")
                        x = os.path.join(currentFolder,obj[1:] + ".png")
                        imagetoText(x)
                else:
                    print("No image found.")
