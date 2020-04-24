# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# built-in package
import sys
import os

# pdfToImage module
from pdfToImage.convertImages import convrt_img
from pdfToImage.handler import PDFHandler
from pdfToImage.utils import remove_file 

print("Running...")
def main():
    
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    
    if args:
        path_to_pdf = args[0]
        path_to_img = args[1]

        p = PDFHandler(filepath = path_to_pdf)
        convrt_img(p.filepath, path_to_img)
        
        if os.path.dirname(p.filepath).endswith("Temp"):
            remove_file(p.filepath)

    else:
        print("Please specify the path-to-pdf-file and path-to-store-images")


if __name__ == "__main__":
    main()
