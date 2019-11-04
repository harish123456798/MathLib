from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="MathLib",
    version="1.0",
    description="Package containing math related formulas, functions.",
    long_description=long_description,
    author="Harishankar.G",
    author_email="harishgaddanakeri@gmail.com",
    packages=find_packages(),
    keywords=["Math", "Formulae", "Arithmetic Progressions", "Logarithms"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
