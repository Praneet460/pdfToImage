# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# built-in package
import os 

def get_file_name(file_path: str):
    """
    Return base file name.
    """
    
    return os.path.basename(file_path)

def get_file_name_without_extension(file_path: str):
    """
    Return base file name without extension.
    """
    
    file_name = os.path.basename(file_path)
    return '.'.join(file_name.split('.')[:-1])

if __name__ == "__main__":
    print(get_file_name_without_extension("../../abc/ppp.pdf"))