from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requiriments = f.read().splitlines()
    
setup(
    name="package_name",
    version="0.0.1",
    author="Pedro Paulo",
    author_email="Pedrogks17@gmail.com",
    description="Modularização de imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pdropp",
    packages=find_packages(),
    install_requires=requiriments,
    python_requires='>3.8',
    
)