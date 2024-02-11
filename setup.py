from setuptools import setup, find_packages

setup(
    name='PyQt6-mediator-mixin',
    version="1.0.3",
    author="Capsize LLC",
    description="A PyQt6 mediator mixin",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="pyqt6, mediator, mixin",
    license="AGPL-3.0",
    author_email="contact@capsizegames.com",
    url="https://github.com/Capsize-Games/PyQt6-mediator-mixin",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.10.0",
    install_requires=[
        "PyQt6>=6.0.0",
        "PyQt6-Qt6>=6.0.0",
        "PyQt6-sip>=13.0.0",
        "PySide6>=6.0.0"
    ],
    dependency_links=[]
)
