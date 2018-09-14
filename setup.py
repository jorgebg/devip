from setuptools import setup


setup(
    name='dev-ip',
    description='Find a suitable IP host to access local network-based applications.',
    version='0.1.0',
    packages=['devip'],
    install_requires=[
        'click==6.7',
        'netifaces==0.10.7',
    ],
    url='https://github.com/jorgebg/devip',
    author="Jorge Barata",
    author_email="jorge.barata.gonzalez@gmail.com",
    license='MIT',
    keywords=['ip'],
    entry_points={
        'console_scripts': [
            'devip = devip.main:devip',
        ]
    },
)
