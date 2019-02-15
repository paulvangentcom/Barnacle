import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barnacle",
    version="0.8",
    author="Paul van Gent",
    author_email="info@paulvangent.com",
    description="Flexible and Fun Progress Bars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=["barnacle"],
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)