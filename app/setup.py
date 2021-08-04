# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
Chatopera Python SDK
=====================

Chatopera 云服务，实现定制化聊天机器人服务。
https://bot.chatopera.com/

为企业聊天机器人而生。

* 支持自定义知识库语料/查询知识库
* 支持多轮对话
* 支持屏蔽/取消屏蔽用户
* 查看聊天机器人详情
* 支持技能：心理问答 API, etc.

详细文档：https://github.com/chatopera/chatopera-py-sdk

"""

setup(
    name='chatopera',
    version='2.1.0',
    description='定制化聊天机器人服务',
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
