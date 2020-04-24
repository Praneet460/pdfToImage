# setup.py

##########################
# AUTHOR : PRANEET NIGAM
##########################

"""
python setup.py --help install # to know how to customize the install procedure
python setup.py --help-commands
python setup.py clean # clean all trash (*.pyc and stuff)
python setup.py test  # run the complete test suite
python setup.py bench # run the complete benchmark suite
python setup.py audit # run pyflakes checker on source code
"""

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
    version = "1.1.2",
    description = "PDF file to Images conversion",
    long_description = README,
    long_description_content_type = "text/markdown",
    author = "Praneet Nigam",
    url = "https://github.com/Praneet460/pdfToImage",
    author_email = "nigampraneet460@gmail.com",
    include_package_data = True,
    python_requires = ">=3.5",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ], 
    packages = ["pdfToImage"],
    install_requires = ["Wand", "tqdm"],
    entry_points = {
        "console_scripts": [
            "pdfToImage = pdfToImage.__main__:main"
        ]
    }
)