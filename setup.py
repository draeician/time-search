#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="time-search",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "python-magic",
    ],
    entry_points={
        "console_scripts": [
            "time-search=time_search.main:main",
            "minute=time_search.main:main",
            "hour=time_search.main:main",
            "day=time_search.main:main",
            "week=time_search.main:main",
            "month=time_search.main:main",
            "year=time_search.main:main",
            "minutes=time_search.main:main",
            "hours=time_search.main:main",
            "days=time_search.main:main",
            "weeks=time_search.main:main",
            "months=time_search.main:main",
            "years=time_search.main:main",
        ],
    },
) 