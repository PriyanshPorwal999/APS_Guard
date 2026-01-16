from setuptools import find_packages, setup
from typing import List

# def get_requirements()->List[str]:
#     requirements_list: list[str] = []

#     return requirements_list

# def get_requirements() -> List[str]:
#     requirements_list: List[str] = []

#     with open("requirements.txt") as file:
#         requirements_list = file.read().splitlines()

#     return requirements_list


def get_requirements() -> List[str]:
    requirements = []
    with open("requirements.txt") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("-e"):
                requirements.append(line)
    return requirements

setup (
    name='sensor',
    version='0.0.1',
    author='Priyansh',
    # author_email='your_email@example.com',
    author_email='priyanshporwal2004@gmail.com',
    packages=find_packages(),
    # install_requires=["pymongo"],
    install_requires=get_requirements(),
)