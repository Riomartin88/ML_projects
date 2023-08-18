from setuptools import find_packages,setup
from typing import List
# it's like a meta data info of the whole project

HYPEN_E_DOT='-e .'

# this func will return a list
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        
        # replacing /n with blank 
        
        requirements=[req.replace("\n","")for req in requirements]
        # give -e . in requirement.txt so that it'll trigger the setup.py 
        
        if HYPEN_E_DOT in requirements:
            # just remove it 
            requirements.remove(HYPEN_E_DOT)
            
    return requirements        

setup(
name='mlproject',
version='0.0.1',
author_email='rishikesh19988@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')   
)

