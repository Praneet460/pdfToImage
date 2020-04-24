# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# pdfToImage packages
from pdfToImage.utils import is_valid_url, download_url

class PDFHandler(object):

    def __init__(self, filepath):

        if is_valid_url(filepath):
            filepath = download_url(filepath)
        self.filepath = filepath

        if not filepath.lower().endswith(".pdf"):
            raise NotImplementedError("File format nor supported")

