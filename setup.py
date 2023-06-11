from setuptools import setup, find_packages


setup(
    name='pyoppleio-legacy',
    version='1.0.8',
    keywords=['opple', 'iot'],
    description='Python library for interfacing with old models of opple lights with wifi control.',
    long_description=open('README.md', 'rt').read(),
    long_description_content_type='text/markdown',
    author='tinysnake',
    author_email='tff.assist@live.com',
    url='https://github.com/tinysnake/python-oppleio-legacy',
    license='MIT',
    install_requires=[
        'pycrc16==0.1.2'
    ],
    packages=find_packages(),
    platforms='any',
    python_requires='>=3.10',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'oppleio=pyoppleio.__main__:main',
        ]
    },
)
