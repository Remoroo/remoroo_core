from setuptools import setup, find_packages

setup(
    name="remoroo-core",
    version="0.1.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pydantic>=2.0.0",
    ],
)
