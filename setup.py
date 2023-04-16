from setuptools import setup, find_packages

setup(
    name="Census-Income",
    version = "0.0.1",
    author="Abhishek",
    author_email="abhishekmohan540@gmail.com",
    packages=find_packages(),
    install_requires = ["pandas","numpy","flask"]
)