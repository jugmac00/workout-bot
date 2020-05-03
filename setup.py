import os

from setuptools import find_packages
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def _read_file(filename):
    with open(os.path.join(HERE, filename)) as f:
        return f.read()


README = _read_file("README.md")
CHANGES = _read_file("CHANGES.md")

version = "0.0.1.dev"

setup(
    name="Workout Bot",
    version=version,
    url="https://github.com/jugmac00/workout-bot",
    project_urls={
        "Issue Tracker": "https://github.com/jugmac00/workout-bot/issues",
        "Sources": "https://github.com/jugmac00/workout-bot",
    },
    license="BSD",
    description="A Telegram bot which sends you a daily workout",
    author="Jürgen Gmach",
    author_email="juergen.gmach@googlemail.com",
    long_description="\n\n".join([README, CHANGES]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">= 3.6",
    install_requires=["beautifulsoup4", "python-telegram-bot"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["do-magic = workout_bot.main:main"]},
)
