#!/usr/bin/env python

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='rankhub',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/alvarob96/rankhub',
    download_url='https://github.com/alvarob96/rankhub/archive/0.0.1.tar.gz',
    license='MIT License',
    author='Alvaro Bartolome',
    author_email='alvarob96@usal.es',
    description='rankhub - is a Python package to generate GitHub users rankings',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests==2.22.0',
        'setuptools==41.2.0',
        'pandas==0.25.1'
    ],
    data_files=[
        ('user_agents', [
            'rankhub/resources/user_agent_list.txt'
        ])
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords='github-api, github-ranking, salamanca-github',
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/alvarob96/rankhub/issues',
        'Source': 'https://github.com/alvarob96/rankhub',
    },
)
