# -*- coding:utf-8 -*-

import setuptools
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()


setuptools.setup(
    name="django-scientific",
    version="0.0.3",
    author="claydodo and his little friends (xiao huo ban)",
    author_email="claydodo@foxmail.com",
    description="Scientific extension for Django, e.g. Numpy/Pandas fields, etc.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/claydodo/django-scientific",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7 ",
        "Programming Language :: Python :: 3 ",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'knob'
    ]
)
