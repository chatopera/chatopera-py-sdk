# Chatopera Node.js SDK

---

https://bot.chatopera.com

低代码或无代码方式定制智能对话机器人！

[Chatopera](https://www.chatopera.com/) 提供聊天机器人开发者平台，Chatopera SDK 用于在 Python 应用中集成[聊天机器人服务](https://bot.chatopera.com/)。

## 安装

```
pip install chatopera
```

实例化机器人

```python
from chatopera import Chatopera, Chatbot
bot = Chatbot(app_id="机器人设置页面获取",
        app_secret="机器人设置页面获取",
        provider='https://bot.chatopera.com')
admin = Chatopera(access_token="机器人平台访问设置页面获取",
    provider='https://bot.chatopera.com')
```

## 使用说明

快速开始，类接口定义和实例化文档等，参考 [文档中心](https://docs.chatopera.com/products/chatbot-platform/integration.html)：

[https://docs.chatopera.com/products/chatbot-platform/integration.html](https://docs.chatopera.com/products/chatbot-platform/integration.html)

## 贡献代码

```
cp sample.env .env # modify .env file
./admin/test.sh
```

## 开源许可协议

Copyright (2018-2021) [北京华夏春松科技有限公司](https://www.chatopera.com/)

[Apache License Version 2.0](./LICENSE)

Copyright 2018-2021, [北京华夏春松科技有限公司](https://www.chatopera.com/). All rights reserved. This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

[![chatoper banner][co-banner-image]][co-url]

[co-banner-image]: https://user-images.githubusercontent.com/3538629/42383104-da925942-8168-11e8-8195-868d5fcec170.png
[co-url]: https://www.chatopera.com
