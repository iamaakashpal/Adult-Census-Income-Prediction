from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "adult-census-predictor"

VERSION = "0.0.1"

AUTHOR = "Aakash Pal"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."



def get_requirements_list() -> List[str]:

    """
    Description : This function is going to return the list of requirements mentioned in the requirements.txt file.
    Input : file_name
    Output : List of requirements.txt i.e. ['pandas','numpy',...'seaborn']
    Name : Aakash Pal
    Date : 01-Nov-2023    
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:

        requirement_list = requirement_file.readlines()
        
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESRCIPTION,
packages = find_packages(), 
install_requires = get_requirements_list()
)
