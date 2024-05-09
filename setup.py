from setuptools import setup

setup(
    name='division2calc',
    version='0.1.0',
    description='division2calc - a calculator for division 2',
    url='https://github.com/quantumsnowball/division2calc',
    author='Quantum Snowball',
    author_email='quantum.snowball@gmail.com',
    license='MIT',
    packages=['division2calc'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'division2calc=division2calc:division2calc',
        ]
    }
)
