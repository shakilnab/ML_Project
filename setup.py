from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''

setup(
    name = 'ML_Project',
    version = '0.0.1',
    author = 'Shakil',
    author_email = 'shakilnab21@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirement.txt')
)