# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2018 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera-py-sdk/app/chatopera/chatbot.py
# Author: Hai Liang Wang
# Date: 2019-03-11:20:01:43
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2018 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2019-03-11:20:01:43"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    # raise "Must be using Python 3"
    pass
else:
    unicode = str

# Get ENV
ENVIRON = os.environ.copy()

import requests
import json

class Chatbot():

    def __init__(self, host, port, chatbot_id):
        self.host = host
        self.port = port
        self.chatbot_id = chatbot_id        
        self.endpoint = "http://%s:%d/api/v1/chatbot/%s" % (host, port, chatbot_id)
        self.default_headers = dict({
                       "Content-Type": "application/json",
                       "Accept": "application/json"
                       })

    def faq(self, user_id, text_message):
        '''
        Call FAQ API
        '''
        body = dict({
                    "fromUserId": user_id,
                    "query": text_message
                    })
        resp = requests.post(self.endpoint + "/faq/query", headers = self.default_headers, data = json.dumps(body, ensure_ascii=False))
        return json.loads(resp.text, encoding = "utf-8")

    def conversation(self, user_id, text_message, branch = "master", is_debug = False):
        '''
        Call conversation API
        '''
        body = dict({
                    "fromUserId": user_id,
                    "textMessage": text_message,
                    "branch": branch,
                    "isDebug": is_debug
                    })
        resp = requests.post(self.endpoint + "/conversation/query", headers = self.default_headers, data = json.dumps(body, ensure_ascii=False))
        return json.loads(resp.text, encoding = "utf-8")


    def mute(self, user_id):
        '''
        Mute a USER
        '''
        resp = requests.post(self.endpoint + "/users/%s/mute" % user_id)
        return json.loads(resp.text, encoding = "utf-8")

    def unmute(self, user_id):
        '''
        Unmute a USER
        '''
        resp = requests.post(self.endpoint + "/users/%s/unmute" % user_id)
        return json.loads(resp.text, encoding = "utf-8")


    def ismute(self, user_id):
        '''
        Unmute a USER
        '''
        resp = json.loads(requests.post(self.endpoint + "/users/%s/ismute" % user_id).text, encoding = "utf-8")
        if resp["rc"] == 0:
            return resp["data"]["mute"]
        else:
            print("[warn] chatbot.ismute: %s" % resp)
            return None

    def profile(self, user_id):
        '''
        Get user profile
        '''
        resp = json.loads(requests.get(self.endpoint + "/users/%s/profile" % user_id, \
                                headers = self.default_headers).text, \
                                encoding = "utf-8")
        if resp["rc"] == 0:
            return resp["data"]
        else:
            print("[warn] chatbot.profile: %s" % resp)
            return None

    def chats(self, user_id, limit = 20, page = 1, sortby = "-lasttime"):
        '''
        Get chats history
        '''
        resp = json.loads(requests.get(self.endpoint + "/users/%s/chats?limit=%d&page=%d&sortby=%s" % (user_id, limit, page, sortby), \
                                headers = self.default_headers).text, \
                                encoding = "utf-8")
        return resp
