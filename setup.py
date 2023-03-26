from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="manasa",
      author_email="mnsj0824@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )