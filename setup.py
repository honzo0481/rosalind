from setuptools import setup

setup(
    name='rosalind',
    version='0.1',
    py_modules=['rosalind'],
    install_requires=[
        'requests',
        'click',
    ],
    entry_points='''
        [console_scripts]
        rosalind=rosalind:solve
    ''',
)
