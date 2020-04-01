# -*- coding: utf-8 -*-
#=========================================================================
#
# Copyright (c) 2018 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera-py-sdk/app/chatopera/chatbot.py
# Author: Hai Liang Wang
# Date: 2019-03-11:20:01:43
#
#=========================================================================

"""

"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2018 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2019-03-11:20:01:43"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise "Must be using Python 3"
else:
    unicode = str

import requests
import copy
import json
from .misc import generate, M_POST, M_GET

S_BASE_PATH = "/api/v1/chatbot"

class Chatbot():

    def __init__(
            self,
            app_id,
            app_secret=None,
            provider="https://bot.chatopera.com"):
        self.provider = provider
        self.app_id = app_id
        self.app_secret = app_secret
        self.endpoint = "%s%s/%s" % (provider, S_BASE_PATH, app_id)
        # signature path param
        self.sxpath = lambda x: S_BASE_PATH + "/" + self.app_id + x
        self.default_headers = dict({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def faq(self, user_id, text_message):
        '''
        Call FAQ API
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/faq/query"
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_POST, self.sxpath(p))

        body = dict({
                    "fromUserId": user_id,
                    "query": text_message
                    })
        resp = requests.post(
            self.endpoint + p,
            headers=headers,
            data=json.dumps(
                body,
                ensure_ascii=False).encode('utf-8'))
        return json.loads(resp.text, encoding="utf-8")

    def conversation(
            self,
            user_id,
            text_message,
            branch="master",
            is_debug=False):
        '''
        Call conversation API
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/conversation/query"
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_POST, self.sxpath(p))

        body = dict({
                    "fromUserId": user_id,
                    "textMessage": text_message,
                    "branch": branch,
                    "isDebug": is_debug
                    })
        resp = requests.post(
            self.endpoint + p,
            headers=headers,
            data=json.dumps(
                body,
                ensure_ascii=False).encode('utf-8'))
        return json.loads(resp.text, encoding="utf-8")

    def mute(self, user_id):
        '''
        Mute a USER
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/users/%s/mute" % user_id
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_POST, self.sxpath(p))

        resp = requests.post(self.endpoint + p, headers=headers)
        return json.loads(resp.text, encoding="utf-8")

    def unmute(self, user_id):
        '''
        Unmute a USER
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/users/%s/unmute" % user_id
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_POST, self.sxpath(p))

        resp = requests.post(self.endpoint + p, headers=headers)
        return json.loads(resp.text, encoding="utf-8")

    def ismute(self, user_id):
        '''
        Unmute a USER
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/users/%s/ismute" % user_id
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_POST, self.sxpath(p))

        resp = json.loads(
            requests.post(
                self.endpoint + p, headers=headers).text,
            encoding="utf-8")
        if resp["rc"] == 0:
            return resp["data"]["mute"]
        else:
            print("[warn] chatbot.ismute: %s" % resp)
            return None

    def profile(self, user_id):
        '''
        Get user profile
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/users/%s/profile" % user_id
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_GET, self.sxpath(p))

        resp = json.loads(
            requests.get(
                self.endpoint + p,
                headers=headers).text,
            encoding="utf-8")
        if resp["rc"] == 0:
            return resp["data"]
        else:
            print("[warn] chatbot.profile: %s" % resp)
            return None

    def chats(self, user_id, limit=20, page=1, sortby="-lasttime"):
        '''
        Get chats history
        '''
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)
        p = "/users/%s/chats?limit=%d&page=%d&sortby=%s" % (
            user_id, limit, page, sortby)
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, M_GET, self.sxpath(p))

        resp = json.loads(
            requests.get(
                self.endpoint + p,
                headers=headers).text,
            encoding="utf-8")
        return resp
