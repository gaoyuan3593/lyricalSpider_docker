#! /usr/bin/python3
# -*- coding: utf-8 -*-
weibo_list = [
    {
        "weibo_index": "weibo_tian_jin_ri_bao_3546332963",
        "weibo_user_id": "3546332963",
        "name": "天津日报"
    },
    {
        "weibo_index": "weibo_ren_min_ri_bao_2803301701",
        "weibo_user_id": "2803301701",
        "name": "人民日报"
    },
    {
        "weibo_index": "weibo_jing_ji_ri_bao_3037284894",
        "weibo_user_id": "3037284894",
        "name": "经济日报"
    },
    {
        "weibo_index": "weibo_guang_ming_ri_bao_1402977920",
        "weibo_user_id": "1402977920",
        "name": "光明日报"
    },
    {
        "weibo_index": "weibo_jin_wan_bao_1960785875",
        "weibo_user_id": "1960785875",
        "name": "今晚报"
    },
    {
        "weibo_index": "weibo_zhong_guo_qing_nian_bao_1726918143",
        "weibo_user_id": "1726918143",
        "name": "中国青年报"
    },
    {
        "weibo_index": "weibo_xin_hua_wang_2810373291",
        "weibo_user_id": "2810373291",
        "name": "新华网"
    },
    {
        "weibo_index": "weibo_xin_hua_mei_ri_dian_xun_1050395697",
        "weibo_user_id": "1050395697",
        "name": "新华每日电讯"
    },
    {
        "weibo_index": "weibo_ren_min_wang_2286908003",
        "weibo_user_id": "2286908003",
        "name": "人民网"
    },
    {
        "weibo_index": "weibo_yang_shi_wang_3266943013",
        "weibo_user_id": "3266943013",
        "name": "央视网"
    },
    {
        "weibo_index": "weibo_yang_guang_wang_1683472727",
        "weibo_user_id": "1683472727",
        "name": "央广网"
    },
    {
        "weibo_index": "weibo_zhong_guo_xin_wen_wang_1784473157",
        "weibo_user_id": "1784473157",
        "name": "中国新闻网"
    },
    {
        "weibo_index": "weibo_zhong_guo_qing_nian_wang_2748597475",
        "weibo_user_id": "2748597475",
        "name": "中国青年网"
    },
    {
        "weibo_index": "weibo_xin_jing_bao_1644114654",
        "weibo_user_id": "1644114654",
        "name": "新京报"
    },
    {
        "weibo_index": "weibo_bei_jing_qing_nian_bao_1749990115",
        "weibo_user_id": "1749990115",
        "name": "北京青年报"
    },
    {
        "weibo_index": "weibo_zhong_guo_jing_ying_bao_1650111241",
        "weibo_user_id": "1650111241",
        "name": "中国经营报"
    },
    {
        "weibo_index": "weibo_peng_pai_xin_wen_5044281310",
        "weibo_user_id": "5044281310",
        "name": "澎湃新闻"
    },
    {
        "weibo_index": "weibo_cai_xin_wang_1663937380",
        "weibo_user_id": "1663937380",
        "name": "财新网"
    },
    {
        "weibo_index": "weibo_chang_an_jie_zhi_shi_1697601814",
        "weibo_user_id": "1697601814",
        "name": "长安街知事"
    },
    {
        "weibo_index": "weibo_tuan_jie_hu_can_kao_5237400929",
        "weibo_user_id": "5237400929",
        "name": "团结湖参考"
    },
    {
        "weibo_index": "weibo_jie_mian_xin_wen_5182171545",
        "weibo_user_id": "5182171545",
        "name": "界面新闻"
    },
    {
        "weibo_index": "weibo_feng_mian_xin_wen_1496814565",
        "weibo_user_id": "1496814565",
        "name": "封面新闻"
    },
    {
        "weibo_index": "weibo_nan_fang_zhou_mo_1639498782",
        "weibo_user_id": "1639498782",
        "name": "南方周末"
    },
    {
        "weibo_index": "weibo_nan_fang_du_shi_bao_1644489953",
        "weibo_user_id": "1644489953",
        "name": "南方都市报"
    },
    {
        "weibo_index": "weibo_hong_xing_xin_wen_6105713761",
        "weibo_user_id": "6105713761",
        "name": "红星新闻"
    },
    {
        "weibo_index": "weibo_mei_ri_jing_ji_xin_wen_1649173367",
        "weibo_user_id": "1649173367",
        "name": "每日经济新闻"
    },
    {
        "weibo_index": "weibo_feng_huang_wang_2615417307",
        "weibo_user_id": "2615417307",
        "name": "凤凰网"
    },
    {
        "weibo_index": "weibo_shou_ji_shang_de_xin_lang_1712686623",
        "weibo_user_id": "1712686623",
        "name": "手机上的新浪 (新浪网)"
    },
    {
        "weibo_index": "weibo_sou_hu_yu_le_1843633441",
        "weibo_user_id": "1843633441",
        "name": "搜狐娱乐（搜狐网）"
    },
    {
        "weibo_index": "weibo_zhong_guo_fang_di_chan_bao_1749627367",
        "weibo_user_id": "1749627367",
        "name": "中国房地产报信息"
    }, ]

wechat_list = [{
    "wechat_index": "wechat_tian_jin_ri_bao_3546332963",
    "account": "天津日报",
},
    {
        "wechat_index": "wechat_ren_min_wang_2286908003",
        "account": "人民网",
    },
    {
        "wechat_index": "wechat_wang_shi_wang_2286908003",
        "account": "央视网",
    },
    {
        "wechat_index": "wechat_ren_min_ri_bao_2803301701",
        "account": "人民日报",
    },
    {
        "wechat_index": "wechat_xin_hua_wang_2810373291",
        "account": "新华网",
    },
    {
        "wechat_index": "wechat_zhong_guo_wang_3164957712",
        "account": "中国网",
    },
    {
        "wechat_index": "wechat_zhong_guo_ri_bao_wang_2127460165",
        "account": "中国日报网",
    },
    {
        "wechat_index": "wechat_zhong_guo_qing_nian_wang_2748597475",
        "account": "中国青年网",
    },
    {
        "wechat_index": "wechat_peng_pai_xin_wen_5044281310",
        "account": "澎湃新闻",
    },
    {
        "wechat_index": "wechat_yang_guang_wang_1683472727",
        "account": "央广网",
    },
    {
        "wechat_index": "wechat_zhong_guo_xin_wen_wang_1784473157",
        "account": "中国新闻网",
    },
    {
        "wechat_index": "wechat_xin_jing_bao_1784473157",
        "account": "新京报",
    },
    {
        "wechat_index": "wechat_bei_jing_qing_nian_bao_1749990115",
        "account": "北京青年报",
    },
    {
        "wechat_index": "wechat_zhong_guo_jing_ying_bao_1650111241",
        "account": "中国经营报",
    },
    {
        "wechat_index": "wechat_cai_xin_wang_1663937380",
        "account": "财新网",
    },
    {
        "wechat_index": "wechat_chang_an_jie_zhi_shi_1697601814",
        "account": "长安街知事",
    },
    {
        "wechat_index": "wechat_tuan_jie_hu_can_kao_5237400929",
        "account": "团结湖参考",
    },
    {
        "wechat_index": "wechat_jie_mian_xin_wen_5182171545",
        "account": "界面新闻",
    },
    {
        "wechat_index": "wechat_feng_mian_xin_wen_1496814565",
        "account": "封面新闻",
    },
    {
        "wechat_index": "wechat_nan_fang_zhou_mo_1639498782",
        "account": "南方周末",
    },
    {
        "wechat_index": "wechat_nan_fang_du_shi_bao_1644489953",
        "account": "南方都市报",
    },
    {
        "wechat_index": "wechat_hong_xing_xin_wen_6105713761",
        "account": "红星新闻",
    },
    {
        "wechat_index": "wechat_mei_ri_jing_ji_xin_wen_1649173367",
        "account": "每日经济新闻",
    },
    {
        "wechat_index": "wechat_bei_jing_shen_yi_du_2747175561",
        "account": "北青深一度",
    }, ]
