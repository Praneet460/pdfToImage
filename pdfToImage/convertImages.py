# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

try:
    # third-party package
    from wand.image import Image as WandImage
    from wand.exceptions import WandException
    from tqdm import tqdm 
except ModuleNotFoundError:
    raise ModuleNotFoundError(
    """
    Wand is not installed. Do 'pip install Wand' and make sure you have GhostScript(64-bit) and ImageMagick(64-bit) installed ImageMagick-6.9.10-78-Q16-x64-dll(http://docs.wand-py.org/en/0.4.2/guide/install.html)
    """
    )
else:
    # built-in package
    import os
    import concurrent.futures

    # pdfToImage module
    from pdfToImage.utils import get_file_name_without_extension



def convrt_img(path_to_pdf_file:str, path_to_img_files:str, resolution:int = 300):
    
    pdf_name = get_file_name_without_extension(path_to_pdf_file)

    if not os.path.exists(path_to_img_files):
        os.makedirs(path_to_img_files)
                
    if not os.path.exists(f'{path_to_img_files}/{pdf_name}'):
        os.makedirs(f'{path_to_img_files}/{pdf_name}')

    try:
        with WandImage(filename = path_to_pdf_file, resolution = resolution) as pdf:

            for index, image in enumerate(tqdm(pdf.sequence)):
                jpeg_image = WandImage(image = image).convert('jpeg')

                if not index <= 9:
                    jpeg_image.save(filename = f"{path_to_img_files}/{pdf_name}/{index}_{pdf_name}.jpeg")
                else:
                    jpeg_image.save(filename = f"{path_to_img_files}/{pdf_name}/0{index}_{pdf_name}.jpeg")
    
    except WandException as exe:
        print(exe)