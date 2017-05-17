文件介绍

Workflow
===========
kuaidi20170105.wflow -  iOS App Workflow 快递查询工具，支持剪切板，请访问 [Matrix 精选 | Workflow + 快递 100 原来快递既能这么查，还能这么显示](http://sspai.com/36871) 了解。

![截图](/bkP/workflow.jpg)

Python
===========
Kuaidi_IFTTT.py 基于 IFTTT Maker 的快递实时推送工具，无公布计划。

![截图](/bkP/kuaidi.jpg)

IFTTT_Signal.py 通过 signal 向 Kuaidi_IFTTT.py 增添快递单的工具。

RetailID.py - 用于本地库执行的 Apple 零售店图片快速下载和整理工具。

RetailID_IFTTT.py - 基于 IFTTT Maker 的 Apple Store 零售店图片更新推送工具。

![截图](/bkP/retailid.jpg)

Event_IFTTT.py - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today_IFTTT.py 替代。

![截图](/bkP/event.jpg)

Today_IFTTT.py - 基于 IFTTT Maker 获取中国 Apple Store 零售店特邀嘉宾活动的推送工具，你可以在 Telegram Follow [果铺知道 Channel](https://t.me/ars_teller) 直接体验本 Python 运行结果。

![截图](/bkP/todayatapple.jpg)

* 请注意，私人 IFTTT Maker Key 在源代码中有明文保存，请不要恶意使用，[IFTTT Maker](https://maker.ifttt.com) 是 IFTTT 提供的服务。

Markdown
===========
README.md - 本文件

name.md - Apple 零售店编号和对应名称

future.md - Apple 零售店未来计划

url.md - Today_IFTTT.py 依赖的下载文件列表，Apple 在存储零售店活动信息时，即使文件不同，但每个城市所有零售店使用文件的内容完全一致。如中国重庆有三家零售店，Apple 解放碑和 Apple 重庆北城天街使用的文件分别为 .../jiefangbei.json 和 .../paradisewalkchongqing.json 但实则完全相同，本列表选择了所有有 Apple Store 城市中的其中一架店作为下载文件

./Previous
==========
kuaidi20161210.wflow - 旧版本，请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60) 了解。

KuaidiUpdater - 上述文件的自动更新旗标文件。

kuaidi.py - Python 快递查询源代码，请访问 [可能是最小的跨平台查快递工具](http://matrix.sspai.com/p/d006b320 ) 了解，已经删除。

flask-kuaidi.py - rss-kuaidi.py 的前身，通过 Pip Flask 将物流输出为更美观的 JSON 形式。

rss-kuaidi.py - 通过 Pip Flask 结合 RSS 实现自动推送物流信息 请访问 [利用 Flask 和 VPS 搭建物流更新自动推送 RSS](http://matrix.sspai.com/p/da505de0) 了解。

联系
=======
专注于 Workflow 和 Python 开发

Twitter: [@Junyi_Lou](https://twitter.com/Junyi_Lou "@Junyi_Lou") 

Sina Weibo: [@Junyi_Lou_](https://weibo.com/n/Junyi_Lou_ "@Junyi_Lou_")

Matrix: [Junyi Lou](http://matrix.sspai.com/p/da7b1760 "Junyi Lou - Matrix")
