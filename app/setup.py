# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
Chatopera Python SDK
=====================

https://bot.chatopera.com/

Deliver Chatbots with Chatopera Platform for your business.

为企业聊天机器人而生。

Welcome
-------

"""

setup(
    name='chatopera',
    version='0.0.2',
    description='Deliver Chatbots with Chatopera Platform',
    long_description=LONGDOC,
    author='Hai Liang Wang',
    author_email='hain@chatopera.com',
    url='https://github.com/chatopera/chatopera-py-sdk',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Chat',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'],
    keywords='chatbot,machine-learning,IR',
    packages=find_packages(),
    install_requires=[
        'requests>=2.18.4'
    ],
    package_data={
        'chatopera': [
            '**/*.gz',
            '**/*.txt',
            'LICENSE']})
