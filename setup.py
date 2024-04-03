from io import open
from setuptools import (setup, find_packages)
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
def read(f):
    with open(f, 'r', encoding='utf-8') as file:
        return file.read()
    
setup(
    name='djangosaml',
    version='1.0.3',
    description='Django SAML2 Authentication Made Easy. Easily integrate with SAML2 SSO identity providers like Okta',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',

    url='https://djangosaml.readthedocs.io/en/latest/',

    author='Fang Li',
    author_email='lorenzo.gil.sanchez@gmail.com',

    license='Apache 2.0',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',        
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='Django SAML2 Authentication Made Easy, integrate with SAML2 SSO such as Okta easily',
    packages=find_packages(),
    install_requires=['pysaml2>=4.5.0',],
    include_package_data=True,
)
