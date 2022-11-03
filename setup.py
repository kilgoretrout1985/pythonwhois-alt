import os
import setuptools

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='pythonwhois-alt',
    version='2.4.6',
    packages=['pythonwhois'],
    package_dir={"pythonwhois":"pythonwhois"},
    package_data={"pythonwhois":["*.dat"]},
    install_requires=['argparse'],
    provides=['pythonwhois'],
    scripts=["pwhois"],

    license="WTFPL",
    description='Module for retrieving and parsing the WHOIS data for a domain. Supports most domains. No dependencies.',
    long_description=README,
    long_description_content_type="text/markdown",
    keywords='whois nic domain',

    author='Yuriy Zemskov',
    author_email='zemskyura@gmail.com',
    url='https://github.com/kilgoretrout1985/pythonwhois-alt',

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: Name Service (DNS)',
    ],
)
