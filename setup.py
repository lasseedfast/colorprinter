from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="colorprinter",
    version="0.1.0",
    author="Lasse Edfast",
    author_email="lasse@edfast.se",
    description="A simple utility for printing text in various colors to the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lasseedfast/colorprinter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)