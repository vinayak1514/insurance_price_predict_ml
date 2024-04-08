from setuptools import find_packages,setup
from typing import List

# HYPEN_E_DOT='-e .'
# def get_requirement(filePath:str)->List[str]:
#     requirements = []
#     with open(filePath) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace('/n',"") for req in requirements]

#     if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements


setup(
    name = "InsuracePredictor",
    version = '0.0.1',
    author= 'Vinayak',
    author_email= "jangirvinayak0001@gmail.com",
    packages= find_packages(),
    install_requires = ["scikit-learn","pandas","numpy"]
)