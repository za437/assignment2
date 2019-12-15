from setuptools import find_packages, setup
setup(
    name='my-tox-tested-package',
    version='0.0.1',
    packages=find_packages(exclude=['tests'],include=['app']),  # Include all the python modules except `tests`.
    description='My custom package tested with tox',
    long_description='A long description of my custom package tested with tox',
    install_requires=[
        'FLASK>=1.1.0',
        # Additional requirements, or parse the requirements file and add it here
    ],
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        'pytest11': [
            'tox_tested_package = tox_tested_package.fixtures'
        ]
    },
)
