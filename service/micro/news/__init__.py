#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service.micro.utils.customerized_data_type import enum

# 人民日报
PEOPLE = [
    'http://politics.people.com.cn/',  # 时政
    'http://world.people.com.cn/',  # 国际
    'http://finance.people.com.cn/',  # 财经
    'http://tw.people.com.cn/',  # 台湾
    'http://military.people.com.cn/',  # 军事
    'http://opinion.people.com.cn/',  # 观点
    'http://leaders.people.com.cn/',  # 领导
    'http://renshi.people.com.cn/',  # 人事
    'http://theory.people.com.cn/',  # 理论
    'http://legal.people.com.cn/',  # 法治
    'http://society.people.com.cn/',  # 社会
    'http://industry.people.com.cn/',  # 产经
    'http://edu.people.com.cn/',  # 教育
    'http://kpzg.people.com.cn/',  # 科普
    'http://sports.people.com.cn/',  # 体育
    'http://culture.people.com.cn/',  # 文化
    'http://art.people.com.cn/',  # 书画
    'http://house.people.com.cn/',  # 房产
    'http://auto.people.com.cn/',  # 汽车
    'http://health.people.com.cn/',  # 健康
    'http://scitech.people.com.cn/',  # 科技
    'http://dangjian.people.com.cn/',  # 党建
    'http://dangshi.people.com.cn/',  # 党史
    'http://fanfu.people.com.cn/',  # 反腐
    'http://hm.people.com.cn/',  # 港澳
    'http://media.people.com.cn/',  # 传媒
    'http://book.people.com.cn/',  # 读书
    'http://rmfp.people.com.cn/',  # 扶贫
    'http://ccnews.people.com.cn/',  # 央企
    'http://fangtan.people.com.cn/',  # 访谈
    'http://tc.people.com.cn/',  # 通信
    'http://homea.people.com.cn/',  # 家电
    'http://it.people.com.cn/',  # I　T
    'http://capital.people.com.cn/',  # 创投
    'http://yuqing.people.com.cn/',  # 舆情
    'http://mooc.people.com.cn/',  # 慕课
    'http://blockchain.people.com.cn/',  # 区块链
    'http://ydyl.people.com.cn/',  # 一带一路
    'http://money.people.com.cn/',  # 金融
    'http://money.people.com.cn/stock/',  # 股票
    'http://energy.people.com.cn/',  # 能源
    'http://gongyi.people.com.cn/',  # 公益
    'http://env.people.com.cn/',  # 环保
    'http://ai.people.com.cn/',  # A　I
    'http://jiaju.people.com.cn/',  # 家居
    'http://dengshi.people.com.cn/',  # 灯饰
    'http://shipin.people.com.cn/',  # 食品
    'http://jiu.people.cn/',  # 酒业
    'http://fashion.people.com.cn/',  # 时尚
    'http://ent.people.com.cn/',  # 娱乐
    'http://www.people78.cn/',  # 棋牌
    'http://game.people.com.cn/',  # 游戏
    'http://caipiao.people.com.cn/',  # 彩票
    'http://travel.people.com.cn/',  # 旅游
    'http://country.people.com.cn/',  # 美丽乡村
    'http://ip.people.com.cn/',  # 知识产权
    'http://xiaofei.people.com.cn/',  # 消费
    'http://yunying.people.cn/GB/index.html'  # 运营
]

# 中国青年网(中青网)
YOUTH_NEWS = [
    "http://news.youth.cn/",  # 时政
    "http://pinglun.youth.cn/",  # 理论
    "http://finance.youth.cn/",  # 财经
    "http://qnzs.youth.cn/",  # 新闻库
    "http://wenhua.youth.cn/",  # 文化
    "http://df.youth.cn/",  # 地方
    "http://gy.youth.cn/",  # 公益
    "http://cunguan.youth.cn/",  # 村官
    "http://edu.youth.cn/",  # 教育
    "http://fun.youth.cn/",  # 娱乐
    "http://sxx.youth.cn/",  # 三下乡
    "http://auto.youth.cn/",  # 汽车
    "http://youxi.youth.cn/",  # 游戏
    "http://tour.youth.cn/",  # 旅游
    "http://agzy.youth.cn/",  # 爱国主义
]

# 中国新闻网
CHINA_NEWS = [
    'www.chinanews.com/mil/',  # 时政
    'www.chinanews.com/sh/',  # 社会
    'www.chinanews.com/gn/',  # 国内
    'www.chinanews.com/gj/',  # 国际
    'www.chinanews.com/cj/',  # 财经
    'www.chinanews.com/ty/',  # 体育
    'www.chinanews.com/ga/',  # 港澳
    'www.chinanews.com/hr/',  # 华人
    'www.chinanews.com/jk/',  # 健康
    'www.chinanews.com/yl/',  # 娱乐
    'www.chinanews.com/cul/',  # 文化
    'www.chinanews.com/auto/',  # 汽车
    'www.chinanews.com/fortune/',  # 金融
    'www.chinanews.com/business/'  # 产经
]

# 新华网
XINHUA = [
    'http://www.xinhuanet.com/politics/',  # 时政，人事，理论
    'http://www.xinhuanet.com/local/',  # 地方
    'http://www.xinhuanet.com/legal/',  # 法制
    'http://www.xinhuanet.com/world/',  # 国际
    'http://www.xinhuanet.com/mil/',  # 军事
    'http://www.xinhuanet.com/talking/',  # 访谈
    'http://www.xinhuanet.com/fortune/',  # 财经
    'http://www.xinhuanet.com/auto/',  # 汽车
    'http://www.xinhuanet.com/house/',  # 房产
    'http://www.xinhuanet.com/comments/',  # 网评
    'http://www.xinhuanet.com/ent/',  # 娱乐
    'http://www.xinhuanet.com/money/',  # 金融
    'http://forum.home.news.cn/',  # 论坛
    'http://sike.news.cn/',  # 思客
    'http://sports.xinhuanet.com/',  # 体育
    'http://www.xinhuanet.com/info/',  # 信息化
    'http://www.xinhuanet.com/datanews/',  # 数据
    'http://www.xinhuanet.com/yuqing/',  # 舆情
    'http://www.xinhuanet.com/vr',  # VR AR
    'http://www.xinhuanet.com/politics/leaders/',  # 高层
    'http://www.xinhuanet.com/gangao/',  # 港澳
    'http://www.xinhuanet.com/tw/',  # 台湾
    'http://www.xinhuanet.com/overseas/',  # 华人
    'http://education.news.cn/',  # 教育
    'http://www.xinhuanet.com/tech/',  # 科技
    'http://www.xinhuanet.com/energy/',  # 能源
    'http://www.xinhuanet.com/caipiao/',  # 彩票
    'http://www.xinhuanet.com/food/',  # 食品
    'http://www.xinhuanet.com/travel/',  # 旅游
    'http://www.xinhuanet.com/health',  # 健康
    'http://www.xinhuanet.com/gongyi/',  # 公益
    'http://uav.xinhuanet.com/',  # 无人机
    'http://www.xinhuanet.com/silkroad/',  # 一带一路
    'http://www.xinhuanet.com/lianzheng/',  # 反腐
    'http://www.xinhuanet.com/fashion/',  # 时尚
    'http://www.xinhuanet.com/xhsd/',  # 新华深度
    'http://www.xinhuanet.com/asia/',  # 亚太网
    'http://www.xinhuanet.com/finance/',  # 证券
    'http://news.cn/finance/tjjd/',  # 投教基地
    'http://www.xinhuanet.com/expo/',  # 会展
    'http://www.xinhuanet.com/jiaju/',  # 家居
    'http://www.xinhuanet.com/jiadian/',  # 家电
    'http://www.xinhuanet.com/shuhua/',  # 书画
    'http://www.xinhuanet.com/air/',  # 航空
    'http://www.xinhuanet.com/abroad',  # 出国
    'http://www.xinhuanet.com/city/',  # 城市
    'http://www.xinhuanet.com/culture',  # 文化
    'http://www.xinhuanet.com/power/',  # 电力
]

# 中国网
CHINA = [
    'http://news.china.com.cn/',  # 新闻,
    'http://military.china.com.cn/',  # 军事,
    'http://legal.china.com.cn/',  # 法治,
    'http://cppcc.china.com.cn/',  # 政协,
    'http://fangtan.china.com.cn',  # 访谈,
    'http://www.china.com.cn/opinion/theory/',  # 理论,
    'http://finance.china.com.cn/',  # 财经,
    'http://finance.china.com.cn/money/',  # 理财,
    'http://finance.china.com.cn/stock/',  # 证券,
    'http://finance.china.com.cn/consume/',  # 消费,
    'http://finance.china.com.cn/industry/',  # 产经,
    'http://finance.china.com.cn/ca/',  # 民航,
    'http://finance.china.com.cn/news/',  # 宏观,
    'http://business.china.com.cn/',  # 商务,
    'http://iot.china.com.cn/',  # 物联,
    'http://auto.china.com.cn/',  # 汽车,
    'http://tech.china.com.cn/',  # 科技,
    'http://house.china.com.cn/',  # 地产,
    'http://shanghui.china.com.cn/',  # 商会,
    'http://chuangkr.china.com.cn/',  # 创氪,
    'http://guoqing.china.com.cn/',  # 国情,
    'http://aj.china.com.cn/',  # 应急,
    'http://mz.china.com.cn/',  # 民族,
    'http://union.china.com.cn/',  # 联盟,
    'http://opinion.china.com.cn/',  # 观点,
    'http://vr.china.com.cn/',  # VR,
    'http://ocean.china.com.cn/',  # 海洋,
    'http://sczg.china.com.cn/',  # 双创,
    'http://travel.china.com.cn/',  # 旅游,
    'http://cul.china.com.cn/',  # 文化,
    'http://art.china.cn/',  # 艺术,
    'http://canjiren.china.com.cn/',  # 助残,
    'http://edu.china.com.cn/',  # 教育,
    'http://ent.china.com.cn/',  # 娱乐,
    'http://music.china.com.cn/',  # 音乐,
    'http://sports.china.com.cn/',  # 体育,
    'http://life.china.com.cn/',  # 生活,
    'http://stzg.china.com.cn/',  # 生态,
    'http://grassland.china.com.cn/',  # 草原,
    'http://sl.china.com.cn/',  # 丝路,
    'http://health.china.com.cn/',  # 健康,
    'http://food.china.com.cn/',  # 食品,
    'http://med.china.com.cn/',  # 医疗,
    'http://zy.china.com.cn/',  # 中医
    'http://f.china.com.cn/',  # 扶贫
    'http://ydyl.china.com.cn/',  # 一带一路
]

# 中国日报网
CHINA_DAILY = [
    "//china.chinadaily.com.cn/a/",
    "//cn.chinadaily.com.cn/a/",
    "//cnews.chinadaily.com.cn/a/"
]

#  中国经济网
CHINA_ECONOMY = [
    'http://www.ce.cn/xwzx/gnsz/gdxw/',  # 国内时政
    'http://cen.ce.cn/more/',  # 中经视频滚动新闻
    'http://finance.ce.cn/',  # 金融证券
    'http://www.ce.cn/cysc/',  # 产业市场
    'http://www.ce.cn/xwzx/',  # 时政社会
    'http://finance.ce.cn/stock/',  # 股市
    'http://finance.ce.cn/jjpd/',  # 基金
    'http://finance.ce.cn/futures/',  # 期货
    'http://finance.ce.cn/bank/',  # 银行
    'http://www.ce.cn/cysc/sp/',  # 食品
    'http://www.ce.cn/cysc/fdc/',  # 房产
    'http://www.ce.cn/cysc/fdc/fc/',  # 房产资讯
    'http://www.ce.cn/cysc/ny/',  # 能源
    'http://www.ce.cn/cysc/stwm/',  # 生态
    'http://intl.ce.cn/',  # 国际
    'http://district.ce.cn',  # 地方
    'http://finance.ce.cn/insurance/',  # 保险
    'http://finance.ce.cn/money/',  # 理财
    'http://views.ce.cn/',  # 评论理论
    'http://tuopin.ce.cn/',  # 脱贫攻坚
    'http://fangtan.ce.cn/',  # 访谈
    'http://www.ce.cn/cysc/yq/',  # 央企
    'http://auto.ce.cn/',  # 汽车
    'http://www.ce.cn/newmain/right/feature/',  # 专稿
    'http://www.ce.cn/zt/',  # 专题
    'http://www.ce.cn/culture/',  # 文化
    'http://district.ce.cn/zt/rwk/',  # 人事
    'http://expo.ce.cn/',  # 会展
    'http://shuhua.ce.cn/',  # 书画
    'http://book.ce.cn/',  # 读书
    'http://city.ce.cn',  # 城市
    'http://fashion.ce.cn/',  # 时尚
    'http://health.ce.cn/',  # 健康
    'http://gongyi.ce.cn/',  # 公益
    'http://tech.ce.cn',  # 科技
    'http://travel.ce.cn/',  # 旅游
    'http://ent.ce.cn/',  # 娱乐
    'http://foodsafety.ce.cn/',  # 食安网
    'http://vr.ce.cn/',  # VR频道
    'http://cv.ce.cn/',  # 商用车
    'http://www.ce.cn/cysc/tech/',  # IT业
    'http://12365.ce.cn/',  # 质量
    'http://www.ce.cn/uav/',  # 航空
    'http://www.ce.cn/cysc/yy/',  # 医药
    'http://www.ce.cn/cysc/jtys',  # 交通
    'http://www.ce.cn/cysc/zgjd/',  # 家电
    'http://fashion.ce.cn/news/',  # 资讯
]

#  中国台湾网
CHINA_TAIWAN = [
    'http://www.taiwan.cn/taiwan/',  # 台湾
    'http://www.taiwan.cn/xwzx/PoliticsNews/',  # 时事
    'http://www.taiwan.cn/taiwan/jsxw/',  # 时事
    'http://www.taiwan.cn/taiwan/pu/',  # 台湾包袱铺
    'http://www.taiwan.cn/plzhx/',  # 评论
    'http://www.taiwan.cn/plzhx/plyzl/ ',  # 两岸快评
    'http://www.taiwan.cn/plzhx/hxshp/',  # 海峡时评
    'http://www.taiwan.cn/plzhx/xxhla/',  # 萧萧话两岸
    'http://www.taiwan.cn/plzhx/zhjzhl/zhjlw/',  # 两岸智库
    'http://www.taiwan.cn/plzhx/wyrt/',  # 网友快言
    'http://www.taiwan.cn/plzhx/dlgc/',  # 大陆观察
    'http://www.taiwan.cn/plzhx/zhjzhl/tyzhj/',  # 专家专栏
    'http://www.taiwan.cn/plzhx/zuopinji/',  # 网友专栏
    'http://www.taiwan.cn/plzhx/mtshy/tw/',  # 媒体声音
    'http://www.taiwan.cn/lilunpindao/',  # 理论
    'http://www.taiwan.cn/xwzx/la/',  # 两岸
    'http://y.taiwan.cn/',  # 青年
    'http://www.taiwan.cn/31t/',  # 31条
    'http://www.taiwan.cn/xwzx/',  # 时事
    'http://v.taiwan.cn/',  # 视听
    'http://www.taiwan.cn/tp/',  # 图库
    'http://www.taiwan.cn/tp/rw/',  # 热图
    'http://edu.special.taiwan.cn/2016/gydgs/',  # 光阴的故事
    'http://edu.special.taiwan.cn/2017/ydylkgs/',  # 镜观两岸
    'http://econ.taiwan.cn/',  # 经贸
    'http://taishang.taiwan.cn/',  # 台商
    'http://culture.taiwan.cn/',  # 文化
    'http://travel.taiwan.cn/',  # 旅游
    'http://www.taiwan.cn/local/',  # 地方
    'http://www.taiwan.cn/local/dfkx/',  # 地方快讯
    'http://depts.taiwan.cn/',  # 部委
    'http://depts.taiwan.cn/news/',  # 部委快讯
    'http://agri.taiwan.cn/',  # 农业
    'http://haiyi.taiwan.cn/',  # 医药
]

#  光明网
GMW_NEWS = [
    'http://news.gmw.cn/',  # 新闻
    'http://politics.gmw.cn/',  # 时政
    'http://world.gmw.cn/',  # 国际
    'http://difang.gmw.cn/',  # 地方
    'http://mil.gmw.cn/',  # 军事
    'http://legal.gmw.cn/',  # 法治
    'http://photo.gmw.cn/',  # 读图
    'http://topics.gmw.cn/',  # 专题
    'http://guancha.gmw.cn/',  # 时评
    'http://theory.gmw.cn/',  # 理论
    'http://dangjian.gmw.cn/',  # 党建
    'http://www.gmw.cn/xueshu/',  # 学术
    'http://feiyi.gmw.cn/',  # 非遗
    'http://zhongyi.gmw.cn/',  # 中医
    'http://culture.gmw.cn/',  # 文化
    'http://tech.gmw.cn/',  # 科技
    'http://edu.gmw.cn/',  # 教育
    'http://health.gmw.cn/',  # 卫生
    'http://kepu.gmw.cn/',  # 科普
    'http://v.gmw.cn/',  # 电视
    'http://economy.gmw.cn/',  # 经济
    'http://life.gmw.cn/',  # 生活
    'http://travel.gmw.cn/',  # 旅游
    'http://lady.gmw.cn/',  # 女人
    'http://e.gmw.cn/',  # 文娱
    'http://sports.gmw.cn/',  # 体育
    'http://yangsheng.gmw.cn/',  # 养生
    'http://reader.gmw.cn/',  # 阅读
    'http://gongyi.gmw.cn/',  # 公益
    'http://shipin.gmw.cn/',  # 食品
    'http://run.gmw.cn/',  # 乐跑
    'http://shuhua.gmw.cn/',  # 书画
    'http://meiwen.gmw.cn/',  # 文荟
    'http://yp.gmw.cn/',  # 药品
    'http://wenyi.gmw.cn/',  # 文艺评论
    'http://qp.gmw.cn/index/',  # 棋牌
    'http://liuxue.gmw.cn/',  # 留学
    'http://cb.gmw.cn/',  # 学术出版
    'http://www.gmw.cn/guoxue/',  # 国学
    'http://www.gmwuf.com/',  # 律师
    'http://museum.gmw.cn/',  # 博物馆
    'http://kepu.gmw.cn/astro/',  # 天文
    'http://www.guangminggame.com/',  # 游戏
]

# 未来网
K618_NEWS = [
    "http://politics.k618.cn/",  # 时政
    "http://news.k618.cn/",  # 燃新闻
    "http://view.k618.cn/",  # 评论
    "http://college.k618.cn/",  # 高校
    "http://zgsxd.k618.cn/",  # 先锋队
    "http://guoxue.k618.cn/",  # 少年国学
    "http://jiafeng.k618.cn/",  # 少儿编程
    "http://51-ck.k618.cn/",  # 创新教育
    "http://edu.k618.cn/",  # 培训
    "http://wei.k618.cn/",  # 微未网
    "http://edu.news.k618.cn/",  # 教育
    "http://xjzhd.k618.cn/",  # 小记者
    "http://ent.k618.cn/",  # 文艺
    "http://baby.k618.cn/",  # 幼儿
    "http://kids.k618.cn/xiaoyuan/",  # 校园
    "http://kids.k618.cn/",  # 中小学
    "http://sun.k618.cn/",  # 生命阳光
    "http://club.k618.cn/",  # 未来社团
    "http://xiao.k618.cn/",  # 孝行天下
    "http://caizhi.k618.cn/",  # 财智教育
    "http://arts.k618.cn/",  # 美育未来
    "http://yxsj.k618.cn/",  # 研学旅行
    "http://jjh.k618.cn/",  # 队闻联播
]

# 消费日报
XFRB_NEWS = [
    "http://www.xfrb.com.cn/html/"
]

# 参考消息网
CKXX_NEWS = [
    "http://column.cankaoxiaoxi.com/",  # 观点
    "http://column.cankaoxiaoxi.com/g/",  # 智库
    "http://www.cankaoxiaoxi.com/china/",  # 时政要闻 中国
    "http://www.cankaoxiaoxi.com/world/",  # 时政要闻 国际
    "http://www.cankaoxiaoxi.com/mil/",  # 军事
    "http://www.cankaoxiaoxi.com/finance/",  # 财经
    "http://ihl.cankaoxiaoxi.com/",  # 观察
    "http://www.cankaoxiaoxi.com/culture/",  # 文化
    "http://www.cankaoxiaoxi.com/sports/",  # 体育
    "http://www.cankaoxiaoxi.com/science/",  # 科技
]

# 央广网
CNR_NEWS = [
    ("http://www.cnr.cn/ygzq/", "ygzq.cnr.cn"),  # 央广动态
    ("http://www.cnr.cn/zgxc/market/", "country.cnr.cn"),  # 市场
    ("http://www.cnr.cn/zgxc/focus/", "country.cnr.cn"),  # 焦点
    ("http://www.cnr.cn/zgxc/mantan/", "country.cnr.cn"),  # 漫谈
    ("http://www.cnr.cn/gongyi/news/", "gongyi.cnr.cn"),  # 公益
    ("http://www.cnr.cn/lvyou/list/", "travel.cnr.cn"),  # 旅游
    ("http://www.cnr.cn/2013qcpd/gdzx/", "auto.cnr.cn"),  # 汽车
    ("http://www.cnr.cn/2014jkpd/jkgdxw/", "health.cnr.cn"),  # 健康
    ("http://www.cnr.cn/jy/list/", "edu.cnr.cn"),  # 教育
    ("http://www.cnr.cn/tech/techgd/", "tech.cnr.cn"),  # 科技
    ("http://www.cnr.cn/chanjing/gundong/", "www.cnr.cn"),  # 产经
    ("http://www.cnr.cn/newscenter/tyxw/news/", "sports.cnr.cn"),  # 体育
    ("http://www.cnr.cn/jingji/gundong/", "finance.cnr.cn"),  # 财经
    ("http://www.cnr.cn/ent/zx/", "ent.cnr.cn"),  # 文娱
    ("http://www.cnr.cn/js2014/ycdj/", "military.cnr.cn"),  # 军事
    ("http://news.cnr.cn/native/gd/", "news.cnr.cn"),  # 理论
    ("http://china.cnr.cn/news/", "news.cnr.cn"),  # 要闻
    ("http://news.cnr.cn/gjxw/gnews/", "news.cnr.cn"),  # 央广网国际
]

# 环球网
HUANQIU_NEWS = [
    "http://world.huanqiu.com/",  # 国际
    "http://china.huanqiu.com/",  # 国内
    "http://mil.huanqiu.com/",  # 军事
    "http://taiwan.huanqiu.com/",  # 台湾
    "http://opinion.huanqiu.com/",  # 评论
    "http://finance.huanqiu.com/",  # 财经
    "http://tech.huanqiu.com/",  # 科技
    "http://auto.huanqiu.com/",  # 汽车
    "http://art.huanqiu.com/",  # 艺术
    "http://go.huanqiu.com/",  # 旅游
    "http://health.huanqiu.com/",  # 健康
    "http://sports.huanqiu.com/",  # 体育
    "http://quality.huanqiu.com/",  # 质量
    "http://bigdata.huanqiu.com/",  # 大数据
    "http://look.huanqiu.com/",  # 博览
    "http://chamber.huanqiu.com/",  # 商协会
    "http://biz.huanqiu.com/",  # 商业
    "http://fashion.huanqiu.com/",  # 时尚
    "http://ent.huanqiu.com/",  # 娱乐
    "http://city.huanqiu.com/",  # 城市
    "http://lx.huanqiu.com/",  # 教育
    "http://hope.huanqiu.com/",  # 公益
    "http://society.huanqiu.com/",  # 社会
    "http://smart.huanqiu.com/",  # 智能
    "http://run.huanqiu.com/",  # 跑步
    "http://ski.huanqiu.com/",  # 滑雪
    "http://uav.huanqiu.com/",  # 无人机
    "http://oversea.huanqiu.com/",  # 海外看中国
    "http://cul.huanqiu.com/",  # 文化
    "https://capital.huanqiu.com/",  # 创投
]

# 国际在线网
CRI_NEWS = [
    "//news.cri.cn/",  # 时政新闻
    "//ent.cri.cn/",  # 文娱动态
    "//city.cri.cn/",  # 城市动态
    "//cj.cri.cn/",  # 城建频道
    "//county.cri.cn/",  # 县域经济
    "//ich.cri.cn/",  # 非遗频道
    "//ge.cri.cn/",  # 环球创业
    "//ce.cri.cn/",  # 企业频道
    "//jq.cri.cn/",  # 景区频道
    "//it.cri.cn/",  # it频道
    "//if.cri.cn/",  # 互联网金融
    "//cx.cri.cn/",  # 创新频道
    "//money.cri.cn/",  # 理财频道
    "//gr.cri.cn/",  # 环球财智
    "//arts.cri.cn/",  # 书画频道
    "//sports.cri.cn/",  # 体育频道
    "//jiaoxue.cri.cn/",  # 热点
    "//talk.cri.cn/",  # 媒体
]

# 党建网
DANG_JIAN = [
    '/djw2016sy/djw2016yw/',  # 要闻
    '/djw2016sy/djw2016syyw/',  # 党建发布
    '/djw2016sy/djw2016syyw/',  # 理论强党
    '/djw2016sy/baiqiang/',  # 百强马院
    '/djw2016sy/rsrm1/',  # 人事
    '/djw2016sy/djw2016djlt/',  # 论坛
    '/djw2016sy/djwjggz/',  # 机关
    '/djw2016sy/djw2016fwcl/',  # 警钟
    '/djw2016sy/djw2016xxdj/ ',  # 学习大军
    '/djw2016sy/djw2016dsgs/',  # 党史
    '/djw2016sy/djw2016whdg/',  # 文化
    '/djw2016sy/djw2016gjgc/',  # 国际
    '/djw2016sy/djw2016dyzyz/',  # 志愿者
    '/djw2016sy/djw2016qunz/',  # 群众
    '/djw2016sy/djw2016wkztl/wkztl2016djzzwk/',  # 征文
]

# 法制网
LEGAL_DAILY = [
    'http://www.legaldaily.com.cn/index/content/',
    'http://www.legaldaily.com.cn/index_article/content/'
]

# 海外网

HAI_WAI_NET = [
    'http://opinion.haiwainet.cn/',  # 评论
    'http://news.haiwainet.cn/',  # 资讯
    'http://theory.haiwainet.cn/',  # 理论
    'http://huaren.haiwainet.cn/',  # 华人
    'http://tw.haiwainet.cn/',  # 台湾
    'http://hk.haiwainet.cn/',  # 香港
    'http://mac.haiwainet.cn/',  # 澳门
    'http://www.nanhainet.cn/',  # 南海
    'http://huamei.haiwainet.cn/',  # 华媒
    'http://www.haiwainet.cn/liuxue/',  # 留学
    'http://haiketravel.haiwainet.cn/',  # 旅行
    'http://www.haiwainet.cn/roll/',  # 滚动
    'http://singapore.haiwainet.cn/',  # 新加坡
    'http://japan.haiwainet.cn/',  # 日本
    'http://chaoxian.haiwainet.cn/',  # 朝鲜
    'http://korea.haiwainet.cn/',  # 韩国
    'http://helan.haiwainet.cn/',  # 荷兰
    'http://de.haiwainet.cn/',  # 德国
    'http://spain.haiwainet.cn/',  # 西班牙
    'http://fr.haiwainet.cn/',  # 法国
    'http://nz.haiwainet.cn/',  # 新西兰
    'http://australia.haiwainet.cn/',  # 澳大利亚
    'http://africa.haiwainet.cn/',  # 非洲
    'http://us.haiwainet.cn/',  # 美国
    'http://canada.haiwainet.cn/',  # 加拿大
    'http://pt.haiwainet.cn/',  # 葡萄牙
    'http://italy.haiwainet.cn/',  # 意大利
    'http://silu.haiwainet.cn/',  # 丝路
    'http://culture.haiwainet.cn/',  # 文化
    'http://minsheng.haiwainet.cn/',  # 民生
    'http://blockchain.haiwainet.cn/',  # 区块链
    'http://shengtai.haiwainet.cn/',  # 生态
    'http://sannong.haiwainet.cn/',  # 三农
    'http://chuangxin.haiwainet.cn/',  # 创新
    'http://travel.haiwainet.cn/',  # 旅游
    'http://huashang.haiwainet.cn/',  # 华商
    'http://renwen.haiwainet.cn/',  # 人文
    'http://chengjian.haiwainet.cn/',  # 城建
    'http://quyu.haiwainet.cn/',  # 区域
    'http://shangjie.haiwainet.cn/',  # 商界
    'http://ziyuan.haiwainet.cn/',  # 资源
    'http://smartcity.haiwainet.cn/',  # AI城市
    'http://wenyi.haiwainet.cn/',  # 文遗
    'http://pinpai.haiwainet.cn/',  # 品牌
    'http://jiaoyu.haiwainet.cn/',  # 教育
    'http://jinrong.haiwainet.cn/',  # 金融
    'http://nengyuan.haiwainet.cn/',  # 能源
    'http://jingmao.haiwainet.cn/',  # 经贸
    'http://shenlan.haiwainet.cn/',  # 深蓝
    'http://chanjing.haiwainet.cn/',  # 产经
    'http://haiyang.haiwainet.cn/',  # 海洋
    'http://xianyu.haiwainet.cn/',  # 县域
]


# 各个新闻网站 type
NEWS_ES_TYPE = enum(
    people='people',  # 人民网
    youth_news='youth_news',  # 中国青年网(中青网)
    china_news='china_news',  # 中国新闻网
    xinhua='xinhua',  # 新华网
    china='china',  # 中国网
    cctv_word='cctv_word',  # 央视国际网
    china_daily='china_daily',  # 中国日报网
    china_economy='china_economy',  # 中国经济网
    china_taiwan='china_taiwan',  # 中国台湾网
    gmw_news='gmw_news',  # 光明网
    k618_news='k618_news',  # k618_news
    xfrb_news='xfrb_news',  # 消费日报网
    ckxx_news='ckxx_news',  # 参考消息网
    cnr_news='cnr_news',  # 央广网
    huanqiu_news='huanqiu_news',  # 环球网
    cri_news='cri_news',  # 国际在线网
    dang_jian='dang_jian',  # 党建网
    cyol_news='cyol_news',  # 中青在线
    china_so='china_so',  # 中国搜索
    legal_daily='legal_daily',  # 法制网
    haiwai_net='haiwai_net',  # 海外网
    inewsweek='inewsweek',  # 中国新闻周刊
    xinhua_net='xinhua_net',  # 新华每日电讯
    qstheory='qstheory',  # 求是网
)
