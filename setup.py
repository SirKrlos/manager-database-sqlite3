# -*- coding: utf-8 -*-

import os
import setuptools


dirname = os.path.abspath (
    os.path.split ( __file__ ) [ 0 ]
)
readme_path = os.path.join (
    dirname, "readme.md"
)

with open (readme_path, "r" ) as file:
    long_description = file.read ()

setuptools.setup (
    name = "manager_database_sqlite3",
    version = "0.1.0",
    author = "JoseCarlosSkar",
    author_email = "josecarlosskar@gmail.com",
    description = "Gerenciador de Banco de Dados sqlite3.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/JoseCarlosSkar/manager-database-sqlite3",
    packages = setuptools.find_packages (),
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
)
