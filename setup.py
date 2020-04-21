# setup.py

##########################
# AUTHOR : PRANEET NIGAM
##########################

# built-in packages
import pathlib
from setuptools import setup

# directory containing this file
HERE = pathlib.Path(__file__).parent

# text of the README file
README = (HERE / "README.md").read_text()

# call setup()
setup(
    name = "pdfToImage",
    version = "1.0.0",
    description = "PDF file to Images conversion",
    long_description = README,
    long_description_content_type = "text/markdown",
    author = "Praneet Nigam",
    author_email = "nigampraneet460@gmail.com",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ], 
    packages = ["pdfToImage"],
    install_requires = ["Wand"],
    entry_points = {
        "console_scripts": [
            "pdfToImage = pdfToImage.__main__:main"
        ]
    }

)