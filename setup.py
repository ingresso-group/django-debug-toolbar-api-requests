#import os
from setuptools import setup

# allow setup.py to be run from any path
#os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-debug-toolbar-api-requests',
    version='0.1.0',
    packages=['djdt_api_requests', 'djdt_api_requests.panels'],
    include_package_data=True,
    description=(
        'A plugin to the Django Debug Toolbar to record stats on requests '
        'made to APIs using the requests library'
    ),
    long_description=open('README.md').read(),
    author='Ingresso',
    author_email='systems@ingresso.co.uk',
    install_requires=['django-debug-toolbar'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)

