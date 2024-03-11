from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine learning project"
VERSION= "0.0.1"
DESCRIPTION="MACHINE LEARNING PROJECT IN MODULAR CODING"
AUTHOR_NAME="Sanju Guntur"
AUTHOR_EMAILID="Sanjaysweety.97@gmail.com"


requirments_file_name ='requirments.txt'

# requirments.txt open
# read
#
HYPEN_E_DOT = '-e .'

def get_requirments_lists()->List[str]:
    with open(requirments_file_name) as requirment_file:
        requirment_list = requirment_file.readlines()
        requirment_list = [requirment_name.replace('\n','') for requirment_name in requirment_list]

        if HYPEN_E_DOT in requirment_list:
            requirment_list.remove(HYPEN_E_DOT)

        return requirment_list    





setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAILID,
      packages=find_packages(),
      install_requires=get_requirments_lists()
     )