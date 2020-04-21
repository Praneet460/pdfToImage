# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# built-in package
import sys

# pdfToImage module
from pdfToImage.convertImages import convrt_img

def main():
    
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    
    if args:
        path_to_pdf = args[0]
        path_to_img = args[1]

        convrt_img(path_to_pdf, path_to_img)
    else:
        print("Please specify the path-to-pdf-file and path-to-store-images")


if __name__ == "__main__":
    main()
