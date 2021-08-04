# -*- coding: utf-8 -*-
# =========================================================================
#
# Copyright (c) 2021 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera-py-sdk/app/chatopera/chatopera.py
# Author: Hai Liang Wang
# Date: 2021-08-02 20:01:43
#
# =========================================================================
from __future__ import print_function
from __future__ import division
import requests
import copy
import json
import sys

if sys.version_info[0] < 3:
    raise BaseException("Must be using Python 3")
else:
    unicode = str

BASE_PATH = "/api/v1"


class Chatopera():
    def __init__(
            self,
            access_token,
            provider="https://bot.chatopera.com"):
        self.access_token = access_token
        self.provider = provider
        self.endpoint = "%s%s" % (provider, BASE_PATH)
        self.default_headers = dict({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def command(self, method, path, payload=None):
        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = "Bearer %s" % (self.access_token)
        method = method.upper()

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

        return json.loads(resp.text)
