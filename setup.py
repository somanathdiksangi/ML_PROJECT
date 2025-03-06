from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requriment(file_path:str)->List[str]:
    requriment=[]

    with open(file_path) as file_obj:
        requriment=file_obj.readlines()
        requriment=[req.replace('\n',"") for req in requriment]
        if HYPEN_E_DOT in requriment:
            requriment.remove(HYPEN_E_DOT)

    return requriment    





setup(
    name="mlproject",
    version='0.0.1',
    author='somanath',
    author_email='somanathdiksangi@gmail.com',
    packages=find_packages(),
    install_requrires=get_requriment('requriment.txt')
)