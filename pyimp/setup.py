from setuptools import setup, find_packages

setup(
    name="importcheck",
    version="0.1.0",
    packages=find_packages(),
    author="Cheng",
    description="Used for check if an library is available or not and supports auto install",
    install_requires=[], 
    python_requires=">=3.6",
)