from setuptools import setup, find_packages

setup(
    name="shivam-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "python-dotenv",
        "prompt_toolkit",
    ],
    entry_points={
        "console_scripts": [
            "shivam=shivam_cli.main:main",
        ],
    },
    author="Shivam",
    description="Ultra Instinct AI Agent CLI for building everything.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rocksky1-dev/shivam-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
