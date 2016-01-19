from setuptools import setup, find_packages

version = '0.1'

setup(
    name='MachineHypermediaToolkit',
    version=version,
    description="Reference implementation of CoRE Interfaces Hypermedia Collection and W3C WoT Interaction Model",
    long_description=open('README.md').read(),

    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='IoT',
    author='Michael J Koster',
    url='',
    license='Apache2',
    py_modules= ['../MachineHypermediaToolkit'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
    install_requires=[
    ],
    dependency_links=[
    ]
)
