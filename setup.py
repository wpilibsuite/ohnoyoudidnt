import re

from setuptools import setup

setup(
    name="sphinx-lynx",
    version="0.1",
    packages=["sphinx-lynx"],
    entry_points={
        "doc8.extension.check": [
            f"{s.lower()} = sphinx-lynx.checks:{s}"
            for s in re.findall(
                r"\nclass (.*?)\(", open("./sphinx-lynx/checks.py", "r").read()
            )
        ]
    },
    install_requires=[
        "more_itertools>=8.6.0",
        "doc8>=0.8.1",
        "docutils>=0.16",
    ],
)
