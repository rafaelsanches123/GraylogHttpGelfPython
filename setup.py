#!/usr/bin/env python
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gray_py_gelf',
     version='1.2.0',
     author="Rafael Francisco Viana Sanches",
     author_email="rafaelsanches123@gmail.com",
     description="This project aims to simplify log shipping to your graylog server quite simply",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/rafaelsanches123/GraylogHttpGelfPython",
     packages=["graylog_lib"],
     install_requires=["requests"],
     keywords=['graylog', 'python3.6', 'json', 'api', 'rafael sanches'],
     classifiers=[
         "Programming Language :: Python :: 3.6",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    python_requires='>=3.6',
 )
