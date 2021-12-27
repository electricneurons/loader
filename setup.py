import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'sqlalchemy',
    'geoalchemy2',
    'psycopg2-binary',
    'boltons',
    'parse',
    'python-dateutil',
    'neuro.utils',
    'pandas',
]

extras_require = dict(
    dev=[],
)


setup(
    name='neuro.loader',
    version='0.0.1',
    description='Brain Cells, man',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
    author="Rebekka Purcell",
    author_email="rebekkapurcell5@gmail.com",
    dependency_links=[
        'git+https://github.com/electricneurons/utils.git#egg=neuron.utils-0.0.1',
    ],
    license="MIT https://en.wikipedia.org/wiki/MIT_License",
    url='http://github.com/electricneurons',
    keywords='neurons, KTaR',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require=extras_require,
    tests_require=requires,
    test_suite="neuro.loader.tests",
    entry_points="""
        [console_scripts]
        loader = neuro.loader.control.loader:main
    """,
)
