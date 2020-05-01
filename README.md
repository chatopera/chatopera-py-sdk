# Chatopera Python SDK

[Chatopera 云服务](https://bot.chatopera.com/) 实现定制化聊天机器人服务。

为企业聊天机器人而生。

* 支持自定义知识库语料/查询知识库
* 支持多轮对话
* 支持屏蔽/取消屏蔽用户
* 查看聊天机器人详情
* 支持技能：心理问答 API, etc.

## 安装

```
pip install chatopera
```

## 使用说明

该SDK的详细使用说明[文档](https://docs.chatopera.com/products/chatbot-platform/index.html).

- 注册账号

```
https://bot.chatopera.com
```

- 集成

```
from chatopera import Chatbot
bot = Chatbot(BOT_APP_ID, BOT_APP_SECRET)
response = bot.faq("py", "你好")
```

Check out [demo](./demo.py) for details.


## APIs

聊天机器人即服务


## Chatbot
```python
Chatbot(app_id,
        app_secret=None,
        provider='https://bot.chatopera.com')
```


### detail
```python
Chatbot.detail()
```

获得聊天机器人详情


### faq
```python
Chatbot.faq(user_id, text_message)
```

查询机器人知识库


### conversation
```python
Chatbot.conversation(user_id,
                     text_message,
                     branch='master',
                     is_debug=False)
```

查询机器人多轮对话


### mute
```python
Chatbot.mute(user_id)
```

屏蔽一个用户


### unmute
```python
Chatbot.unmute(user_id)
```

取消屏蔽一个用户


### ismute
```python
Chatbot.ismute(user_id)
```

查看一个用户是否被屏蔽


### profile
```python
Chatbot.profile(user_id)
```

查看用户画像


### chats
```python
Chatbot.chats(user_id, limit=20, page=1, sortby='-lasttime')
```

获得聊天历史


### psychSearch
```python
Chatbot.psychSearch(query, threshold=0.2)
```

技能：心理咨询查询接口
文档：[链接](https://docs.chatopera.com/products/psych-assistant/api.html#api-%E6%8E%A5%E5%8F%A3%E5%AE%9A%E4%B9%89)


### psychChat
```python
Chatbot.psychChat(channel, channel_id, user_id, text_message)
```

技能：心理咨询聊天接口
文档：[链接](https://docs.chatopera.com/products/psych-assistant/api.html#api-%E6%8E%A5%E5%8F%A3%E5%AE%9A%E4%B9%89)


## 开源许可协议

Copyright (2018) [北京华夏春松科技有限公司](https://www.chatopera.com/)

[Apache License Version 2.0](./LICENSE)

Copyright 2017-2018, [北京华夏春松科技有限公司](https://www.chatopera.com/). All rights reserved. This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

[![chatoper banner][co-banner-image]][co-url]

[co-banner-image]: https://user-images.githubusercontent.com/3538629/42383104-da925942-8168-11e8-8195-868d5fcec170.png
[co-url]: https://www.chatopera.com
