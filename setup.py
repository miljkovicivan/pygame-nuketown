from setuptools import find_packages, setup

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='MIPS simulator',
    description='An example of the vehicle movements for the MIPS project',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['mips-sim=mips.__main__:main'],
    }
)
