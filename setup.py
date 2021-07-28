import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md"), encoding="utf8") as fid:
    README = fid.read()

setup(
    name="mongoblack",
    version="1.0.0",
    description="MongoDB handlers to streamline application interfaces",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BlackburnHax/mongoblack",
    author="Brandon Blackburn",
    author_email="contact@bhax.net",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["mongoblack"],
    include_package_data=True,
    install_requires=["pymongo"],
)
