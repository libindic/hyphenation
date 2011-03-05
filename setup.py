from setuptools import setup, find_packages

setup(
    name = "hyphenator",
    version = "0.1b1",
    url="",
    license = "LGLP 3.0",
    description = "Hyphenation module for Python",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = "",
    package = find_packages('src'),
    package_dir = {'' : 'src'},
    setup_requires = ['setuptools-git'],
    namespace_packages = ['hyphenator'],
    include_package_data = True,
    install_requires = ['setuptools'],
    zip_safe = False,
    )
