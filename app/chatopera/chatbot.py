# -*- coding: utf-8 -*-
# =========================================================================
#
# Copyright (c) 2018 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera-py-sdk/app/chatopera/chatbot.py
# Author: Hai Liang Wang
# Date: 2019-03-11:20:01:43
#
# =========================================================================

"""
聊天机器人即服务
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
    raise BaseException("Must be using Python 3")
else:
    unicode = str

from .misc import generate, M_POST, M_GET
import json
import copy
import requests

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

    def command(self, method, path, payload=None):
        headers = copy.deepcopy(self.default_headers)

        method = method.upper()

        if "?" in path:
            path = path+"&sdklang=python"
        else:
            path = path+"?sdklang=python"

        headers["Authorization"] = generate(
            self.app_id, self.app_secret, method, self.sxpath(path))

        data = None
        if(payload != None):
            data = json.dumps(
                payload,
                ensure_ascii=False).encode('utf-8')

        resp = requests.request(method,
                                self.endpoint + path,
                                headers=headers,
                                data=data
                                )

        return json.loads(resp.text, encoding="utf-8")

    def detail(self):
        """
        获得聊天机器人详情
        """
        return self.command(M_GET, "/")

    def faq(self, user_id, text_message):
        """
        查询机器人知识库
        """
        return self.command(M_POST, "/faq/query", dict({
            "fromUserId": user_id,
            "query": text_message
        }))

    def conversation(
            self,
            user_id,
            text_message,
            branch="master",
            is_debug=False):
        """
        查询机器人多轮对话
        """
        return self.command(M_POST, "/conversation/query", dict({
            "fromUserId": user_id,
            "textMessage": text_message,
            "branch": branch,
            "isDebug": is_debug
        }))

    def mute(self, user_id):
        """
        屏蔽一个用户
        """
        return self.command(M_POST, "/users/%s/mute" % user_id)

    def unmute(self, user_id):
        """
        取消屏蔽一个用户
        """
        return self.command(M_POST, "/users/%s/unmute" % user_id)

    def ismute(self, user_id):
        """
        查看一个用户是否被屏蔽
        """
        resp = self.command(M_POST, "/users/%s/ismute" % user_id)

        if resp["rc"] == 0:
            return resp["data"]["mute"]
        else:
            print("[warn] chatbot.ismute: %s" % resp)
            return None

    def profile(self, user_id):
        """
        查看用户画像
        """
        resp = self.command(M_GET, "/users/%s/profile" % user_id)
        # add auth into headers
        headers = copy.deepcopy(self.default_headers)

        if resp["rc"] == 0:
            return resp["data"]
        else:
            print("[warn] chatbot.profile: %s" % resp)
            return None

    def chats(self, user_id, limit=20, page=1, sortby="-lasttime"):
        """
        获得聊天历史
        """
        return self.command(M_GET, "/users/%s/chats?limit=%d&page=%d&sortby=%s" % (
            user_id, limit, page, sortby))

    def psychSearch(self, query, threshold=0.2):
        """
        技能：心理咨询查询接口
        文档：[链接](https://docs.chatopera.com/products/psych-assistant/api.html#api-%E6%8E%A5%E5%8F%A3%E5%AE%9A%E4%B9%89)
        """
        resp = self.command(M_POST, "/skills/psych/search")

        if "rc" in resp and resp["rc"] == 0:
            return resp["data"]
        if "rc" in resp and resp["rc"] == 2:
            del resp["rc"]
            return resp
        else:
            raise RuntimeError(
                "Invalid response, error %s" % (resp["error"] if "error" in resp else None))

    def psychChat(self, channel, channel_id, user_id, text_message):
        """
        技能：心理咨询聊天接口
        文档：[链接](https://docs.chatopera.com/products/psych-assistant/api.html#api-%E6%8E%A5%E5%8F%A3%E5%AE%9A%E4%B9%89)
        """
        resp = self.command(M_POST, "/skills/psych/chat", dict({
            "channel": channel,
            "channelId": channel_id,
            "userId": user_id,
            "textMessage": text_message
        }))

        if "rc" in resp and resp["rc"] == 0:
            return resp["data"]
        else:
            raise RuntimeError(
                "Invalid response, error %s" % (resp["error"] if "error" in resp else None))
