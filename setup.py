from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hello_world',
    version='0.0.1',
    description='Say Hello',
    py_modules=["hello_world"],
    package_dir={'': 'src'},
    author="Rajnish",
    author_email="rajnishkumar307@gmail.com",
    url="https://github.com/rajnish307/hello_world",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "blessing ~= 1.7",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)
