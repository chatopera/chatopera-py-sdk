#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/chatopera-py-sdk/app/chatopera/misc.py
# Author: Hai Liang Wang
# Date: 2020-04-01:16:54:03
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2020-04-01:16:54:03"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    #raise BaseException("Must be using Python 3")
    pass
else:
    unicode = str

"""
https://stackoverflow.com/questions/23164058/how-to-encode-text-to-base64-in-python
"""
import json
import string
import hmac
import hashlib
import time
import random
import base64
from builtins import bytes

# 常量
M_POST = "POST"
M_GET = "GET"
M_DELETE = "DELETE"
M_PUT = "PUT"
M_PATCH = "PATCH"

def to_bytes(x): return bytes(x, 'utf-8')

def b64e(s):
    return base64.b64encode(s.encode()).decode()


def b64d(s):
    return base64.b64decode(s).decode()

def generate(appId, secret, method, path):
    timestamp = str(int(time.time()))
    rnd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    msg = appId + timestamp + rnd + method + path
    h = hmac.new(to_bytes(secret), to_bytes(msg), hashlib.sha1)
    signature = h.hexdigest()
    return b64e(json.dumps({'appId': appId,
                            'timestamp': timestamp,
                            'random': rnd,
                            'signature': signature}))