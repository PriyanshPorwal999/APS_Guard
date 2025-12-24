from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirements_list: list[str] = []

    return requirements_list

setup (
    name='sensor',
    version='0.0.1',
    author='Priyansh',
    # author_email='your_email@example.com',
    author_email='priyanshporwal2004@gmail.com',
    packages=find_packages(),
    install_requires=["pymongo"],
    install_requires=get_requirements(),
)