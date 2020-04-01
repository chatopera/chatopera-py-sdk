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
    version='1.0.1',
    description='Deliver chatbot with Chatopera platform for Enterprises.',
    long_description=LONGDOC,
    author='Hai Liang Wang',
    author_email='hain@chatopera.com',
    url='https://github.com/chatopera/chatopera-py-sdk',
    license="Apache Software License",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'],
    keywords='chatbot,machine-learning,IR',
    packages=find_packages(),
    install_requires=[
        'requests>=2.20.0'
    ],
    package_data={
        'chatopera': [
            '**/*.gz',
            '**/*.txt',
            'LICENSE']})
