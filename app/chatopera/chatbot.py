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
import requests
import copy
import json
from six import PY2
from .misc import generate, M_POST, M_GET

__copyright__ = "Copyright (c) 2018 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2019-03-11:20:01:43"

import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    #raise BaseException("Must be using Python 3")
    pass
else:
    unicode = str


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
            "Accept": "application/json"
        })

    def arsRecognize(self, path, headers, payload):
        body = {
            'type': payload['type'],
            'nbest': payload.get('nbest', 5),
            'pos': payload.get('pos', "0"),
            'fromUserId': payload['fromUserId']
        }

        resp = None

        if(payload['type'] == 'base64'):
            body['data'] = payload['data']
            headers["Content-Type"] = "application/json"
            data = json.dumps(
                body,
                ensure_ascii=False).encode('utf-8')
            resp = requests.request('POST',
                                    self.endpoint + path,
                                    headers=headers,
                                    data=data
                                    )
        else:
            resp = requests.request('POST',
                                    self.endpoint + path,
                                    headers=headers,
                                    data=body,
                                    files=[('file', open(payload['filepath'], 'rb'))])

        print(resp.text)

        return json.loads(resp.text, encoding="utf-8")

    def command(self, method, path, payload=None):
        """
        核心接口，详细介绍，https://docs.chatopera.com/products/chatbot-platform/integration.html
            Parameters:
                method (string): HTTP Action, delete, put, post, get, etc.
                path (string): URL 路径

            Returns:
                    response (dict): JSON格式 dict 数据结构
        """
        headers = copy.deepcopy(self.default_headers)

        method = method.upper()

        orginPath = path

        if "?" in path:
            path = path+"&sdklang=python"
        else:
            path = path+"?sdklang=python"

        headers["Content-Type"] = "application/json"
        headers["Authorization"] = generate(
            self.app_id, self.app_secret, method, self.sxpath(path))

        data = None

        if(method == 'POST' and orginPath == '/asr/recognize'):
            return self.arsRecognize(path, headers, payload)

        if(payload != None):
            if PY2:
                data = json.dumps(
                payload,
                ensure_ascii=False)
            else:
                data = json.dumps(
                payload,
                ensure_ascii=False).encode('utf-8')

        resp = requests.request(method,
                                self.endpoint + path,
                                headers=headers,
                                data=data
                                )

        return json.loads(resp.text)
