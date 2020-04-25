# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# pdfToImage packages
from pdfToImage.utils import is_valid_url, download_url, get_file_name_without_extension, get_file_name
from pdfToImage.convertImages import convrt_img

# third-party packages
from PyPDF2 import PdfFileReader, PdfFileWriter
from wand.image import Image as WandImage
from wand.color import Color

# built-in package
import io
import os
from datetime import datetime


class PDFHandler(object):

    def __init__(self, filepath:str, pages:str = 'all', password:str = None):

        if is_valid_url(filepath):
            filepath = download_url(filepath)
        self.filepath = filepath

        if not filepath.lower().endswith(".pdf"):
            raise NotImplementedError("File format nor supported")
        
        if password is None:
            self.password = ""
        else:
            self.password = password

        self.pages = self._get_pages(self.filepath, pages)
        


    def _get_pages(self, filepath, pages):
        """Converts pages string to list of ints

        pages = '1', '2,5,8-all', 'all'
        """
        page_numbers = []
        
        with open(self.filepath, 'rb') as file:
            reader = PdfFileReader(file)
                    
            if reader.isEncrypted:
                reader.decrypt(self.password)
            
            num_of_pages = reader.getNumPages()
        
        if pages == "all":
            page_numbers.append({'start': 1, 'end': num_of_pages})
        else:
            for p in pages.split(','):
                if '-' in p:
                    a, b = p.split('-')

                    if b == 'all':
                        b = num_of_pages

                    page_numbers.append({'start': int(a), 'end': int(b)})

                else:
                    page_numbers.append({'start': int(p), 'end': int(p)})

        page_numbers_lst = []
        for page in page_numbers:
            page_numbers_lst.extend(range(page['start'], page['end']+1))

        return sorted(set(page_numbers_lst))   

    def info(self):
        """Get maetadata information about PDF
        """
        meta_info_data = {}

        with open(self.filepath, 'rb') as file:
            # initialize the PDF reader object
            reader = PdfFileReader(file) 

            if reader.isEncrypted:
                reader.decrypt(self.password)

            # Retrieves the PDF file's document information dictionary 
            info = reader.getDocumentInfo() 
            # Retrives XMP (Extensible Metadata Platform) data from the PDF document
            xmp = reader.getXmpMetadata()   
            # Number of pages in PDF
            num_of_pages = reader.getNumPages()

        if info is not None:
            info_key_lst = ['filepath', 'author', 'creator', 'producer', 'subject', 'title', 'number_of_pages']
            info_value_list = [self.filepath, info.author, info.creator, info.producer, info.subject, info.title, num_of_pages]

            for info_key, info_value in zip(info_key_lst, info_value_list):
                meta_info_data[info_key] = info_value

        if xmp is not None:
            xmp_key_lst = ['format', 'createDate', 'modifyDate', 'metadataDate',    'creatorTool']

            xmp_value_lst = [xmp.dc_format, xmp.xmp_createDate, xmp.xmp_modifyDate, xmp.xmp_metadataDate, xmp.xmp_creatorTool]
            
            for xmp_key, xmp_value in zip(xmp_key_lst, xmp_value_lst):
                if isinstance(xmp_value, datetime):
                    meta_info_data[xmp_key] = '{} {}'.format(xmp_value.date(), xmp_value.time())        
                else:    
                    meta_info_data[xmp_key] = xmp_value

            return meta_info_data
        
        return meta_info_data

    def convert2img(self, path_to_save_img):

        file_name = get_file_name_without_extension(self.filepath)

        if not os.path.exists(path_to_save_img):
            os.makedirs(path_to_save_img)
                
        if not os.path.exists(f'{path_to_save_img}/{file_name}'):
            os.makedirs(f'{path_to_save_img}/{file_name}')

        with open(self.filepath, 'rb') as file:
            
            # initialize the PDF reader object
            reader = PdfFileReader(file) 
            
            if reader.isEncrypted:
                reader.decrypt(self.password)

                base_file_name = get_file_name(self.filepath)
                temp_file_loc = os.path.join(path_to_save_img, file_name, base_file_name)

                with open(temp_file_loc, 'wb') as pdf_file:
                    writer = PdfFileWriter()
                    for page in range(reader.getNumPages()):
                        writer.addPage(reader.getPage(page))
                    writer.write(pdf_file)
                
                convrt_img(temp_file_loc, path_to_save_img)

                os.remove(temp_file_loc)
            
            else:
                convrt_img(self.filepath, path_to_save_img)


if __name__ == "__main__":
    # D:/Office-Project-GitHub/Policy-Declaration/Policy_Dec_Form/database/Policy_Checklist.pdf
    # https://d1.awsstatic.com/whitepapers/migrating-magento-to-aws.pdf
    p = PDFHandler(filepath="https://d1.awsstatic.com/whitepapers/migrating-magento-to-aws.pdf")
    # print(type(p.password))
    print(p.info())
    print(p.pages)
    p.convert2img('D:/Office-Project-GitHub/Policy-Declaration/Policy_Dec_Form/database/')