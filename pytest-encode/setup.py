from setuptools import setup

setup(
    name="pytest_encode",
    url='https://github.com/pytest-dev/pytest-forked',
    version='1.0',
    description='set your encoding',
    author='AJ',
    author_email='850259582@qq.com',
    platforms=['linux', 'osx'],
    packages=['pytest_encode'],
    entry_points={
        'pytest11': [
            'pytest_encode = pytest_encode',
        ]
    },
    zip_safe=False,
    install_requires=['pytest'])
