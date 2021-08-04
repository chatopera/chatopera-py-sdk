#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (c) 2018 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera-py-sdk/test.py
# Author: Hai Liang Wang
# Date: 2019-03-11:20:03:56
#
# ===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2018 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2019-03-11:20:03:56"
__version__ = "0.0.3"

import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir + '/app')

if sys.version_info[0] < 3:
    # raise "Must be using Python 3"
    pass
else:
    unicode = str

from chatopera import Chatopera, Chatbot
import time
import logging

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL)

import unittest

BOT_PROVIDER = os.environ.get("BOT_PROVIDER", "https://bot.chatopera.com")
BOT_APP_ID = os.environ.get("BOT_APP_ID", None)
BOT_APP_SECRET = os.environ.get("BOT_APP_SECRET", None)
BOT_ACCESS_TOKEN = os.environ.get("BOT_ACCESS_TOKEN", None)


# run testcase: python /Users/hain/chatopera/chatopera-py-sdk/test.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''

    def setUp(self):
        self.bot = Chatbot(BOT_APP_ID, BOT_APP_SECRET, BOT_PROVIDER)
        self.admin = Chatopera(BOT_ACCESS_TOKEN, BOT_PROVIDER)

    def tearDown(self):
        pass

    def test_conversation(self):
        logging.info("test_conversation")
        resp = self.bot.command("POST", "/conversation/query", dict({
            "fromUserId": "py001",
            "textMessage": "今天北京天气怎么样"
        }))
        logging.info("rc: %s", resp["rc"])
        logging.info("conversation: service provider [%s], logic_is_unexpected %s, logic_is_fallback %s", \
                     resp["data"]["service"]["provider"], \
                     resp["data"]["logic_is_unexpected"], \
                     resp["data"]["logic_is_fallback"])

        assert resp["data"]["service"]["provider"] == "mute"
        assert resp["data"]["logic_is_unexpected"] == False

        logging.info(resp["data"]["string"])

        logging.info("faq: %d", len(resp["data"]["faq"]))
        if resp["rc"] == 0:
            for x in resp["data"]["faq"]:
                logging.info("%f match: %s, reply: %s", x["score"], x["post"], x["reply"])

    def test_detail(self):
        logging.info("test_detail")

        resp = self.bot.command("GET", "/")
        logging.info("rc: %s \n\t%s", resp["rc"], resp)

    def test_faq(self):
        logging.info("test_faq")

        resp = self.bot.command("POST", "/faq/query", dict({
            "fromUserId": "py001",
            "query": "你好"
        }))
        logging.info("rc: %s \n\t%s", resp["rc"], resp)
        if resp["rc"] == 0:
            for x in resp["data"]:
                logging.info("%f match: %s, reply: %s", x["score"], x["post"], x["reply"])

    def test_mute(self):
        logging.info("test_mute")
        resp = self.bot.command("POST", "/users/%s/mute" % "py001")
        logging.info("response: %s", resp)

    def test_getchatbots(self):
        logging.info("test_getchatbots")
        resp = self.admin.command("GET", "/chatbot")
        logging.info("response: %s", resp)

    def test_createchatbot(self):
        logging.info("test_createchatbot")
        bot_name = "TestPy" + str(time.time_ns() // 1000)
        payload = dict({
            "name": bot_name,
            "description": "Hello",
            "primaryLanguage": "zh_CN",
            "trans_zhCN_ZhTw2ZhCn": False
        })
        logging.info("create bot %s >> %s ...", bot_name, payload)
        resp = self.admin.command("POST", "/chatbot", payload)
        logging.info("response: %s", resp)


def test():
    suite = unittest.TestSuite()
    # suite.addTest(Test("test_detail"))
    # suite.addTest(Test("test_conversation"))
    # suite.addTest(Test("test_faq"))
    # suite.addTest(Test("test_mute"))
    # suite.addTest(Test("test_getchatbots"))
    suite.addTest(Test("test_createchatbot"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


def main():
    test()


if __name__ == '__main__':
    main()
