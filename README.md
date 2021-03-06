## PDFTOIMAGE

### About
PdfToImage package will help you convert the PDF files into Images.

### How to setup?
Run
```
cd pdfToImage
python setup.py install
```
This will install the library in the default location.

### How to use?
Run
```
pdfToImage '/path/to/your/pdf-file.pdf' '/path/to/your/convert/images'
```

### Example
Run
- <b>Example 1</b>
```
pdfToImage "D:\Office-Project-GitHub\Policy-Declaration\Policy_Dec_Form\database\Policy_Checklist.pdf" "D:\Office-Project-GitHub\Policy-Declaration\Policy_Dec_Form\database"
```

- <b>Example 2</b>
```
pdfToImage "https://d1.awsstatic.com/whitepapers/migrating-magento-to-aws.pdf" "D:\Office-Project-GitHub\Policy-Declaration\Policy_Dec_Form\database"
```

### How to Test locally?
Run
```
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -e .
```