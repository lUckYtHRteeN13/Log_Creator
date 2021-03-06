from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
    
VERSION = '0.0.15'
DESCRIPTION = 'Log Creator Module'

# Setting up
setup(
    name="log_creator",
    version=VERSION,
    author="lUckYtHRteeN13 (Nethan Quinn Jael) ",
    author_email="<nethanquinnjael13@gmail.com>",
    description=DESCRIPTION,    
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'log', 'logs', 'log creator'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)