import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md"), encoding="utf8") as fid:
    README = fid.read()

setup(
    name="mongoblack",
    version="1.0.2",
    description="MongoDB handlers to streamline application interfaces",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BlackburnHax/mongoblack",
    author="Brandon Blackburn",
    author_email="contact@bhax.net",
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
        "Topic :: Text Processing :: Markup :: reStructuredText",
        "Topic :: Database :: Database Engines/Servers",
    ],
    packages=["mongoblack"],
    include_package_data=True,
    install_requires=["pymongo"],
)
