from setuptools import setup, find_packages

setup(
    name='Tip Calculator',
    version='1.0',
    packages=find_packages(),
    author='Amlan Mishra',
    author_email='amxaverian@gmail.com',
    description='A simple tip calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mishramlan/Tip_Calculator',
    install_requires=[
        'flask>=2.0.0', 'argparse==1.4.0'  # dependencies 
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Users',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='tip calculator',
    entry_points={
        'console_scripts': [
            'tip_calculator=tip_calculator:main',
        ],
    },
)