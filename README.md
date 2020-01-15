# pdftoText
Somewhere in free America a statistics teacher tried to make me copy code by hand.
* Dependencies
** python modules
PyPDF2
pytesseract
openCV
#+BEGIN_SRC 
pip install PyPDF2 pytesseract opencv --user
#+END_SRC
** general dependencies
tesseract
https://github.com/tesseract-ocr/tesseract/wiki/Downloads

* Usage
Make a folder, place the pdf you are working with inside that folder. Copy the code and place it into the same folder and call it "pdfRead.py".

run this command in the terminal
#+BEGIN_SRC 
python pdfRead.py <name of pdf>
#+END_SRC

once that is complete it will make a few images and then things with the ".m" extension this is the copied text that can be run using matlab. you will have to edit the .m files a little bit but its better than nothing.
