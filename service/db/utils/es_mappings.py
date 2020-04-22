#! /usr/bin/python3
# -*- coding: utf-8 -*-


# ---------微博mapping--------------
WEIBO_DETAIL_MAPPING = {
    "time": {
        "type": "date",
        "index": True,
    },
    "platform": {
        "type": "keyword",
    },
    "contents": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "mid": {
        "type": "keyword",  # 字符串
        "index": True,
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "like": {
        "type": "long",
    },
    "comment_num": {
        "type": "long",
    },
    "repost_num": {
        "type": "long",
    },
    "is_forward": {
        "type": "integer",
    },
    "forward_weibo_id": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "key_user_id_list": {
        "type": "keyword",
        "index": True,
    },
    "forward_user_id_list": {
        "type": "keyword",
        "index": True,
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "topic_list": {
        "type": "keyword",
        "index": True,
    },
    "is_has_href": {
        "type": "long",
        "index": True,
    },
    "is_pics": {
        "type": "long",
        "index": True,
    },
    "is_videos": {
        "type": "long",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

WEIBO_COMMENT_MAPPING = {
    "time": {
        "type": "date",
        "index": True,
    },
    "platform": {
        "type": "keyword",
        "index": True
    },
    "contents": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True
    },
    "user_id": {
        "type": "keyword",
        "index": True
    },
    "user_name": {
        "type": "keyword",
        "index": True
    },
    "weibo_id": {
        "type": "keyword",
        "index": True
    },
    "type": {
        "type": "keyword",
        "index": True
    },
    "like": {
        "type": "long",
    },
    "key_user_id_list": {
        "type": "keyword",
        "index": True
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

WEIBO_REPOST_MAPPING = {
    "time": {
        "type": "date",
        "index": True,
    },
    "platform": {
        "type": "keyword",
        "index": True
    },
    "contents": {
        "type": "text",
    },
    "user_id": {
        "type": "keyword",
        "index": True
    },
    "user_name": {
        "type": "keyword",
        "index": True
    },
    "weibo_id": {
        "type": "keyword",
        "index": True
    },
    "type": {
        "type": "keyword",
        "index": True
    },
    "like": {
        "type": "long",
    },
    "key_user_id_list": {
        "type": "keyword",
        "index": True
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

WEIBO_USERINFO_MAPPING = {
    "user_id": {
        "type": "keyword",
        "index": True
    },
    "fan_count": {
        "type": "long",
        "index": True
    },
    "follow_count": {
        "type": "long",
        "index": True
    },
    "user_name": {
        "type": "keyword",
        "index": True
    },
    "verified": {
        "type": "keyword",
        "index": True
    },
    "verified_reason": {
        "type": "text",
    },
    "profile_image_url": {
        "type": "text",
    },
    "tags": {
        "type": "keyword",
        "index": True
    },
    "weibo_count": {
        "type": "long",
        "index": True
    },
    "type": {
        "type": "keyword",
        "index": True
    },
    "city": {
        "type": "keyword",
        "index": True
    },
    "introduction": {
        "type": "text",
    },
    "gender": {
        "type": "keyword",
        "index": True
    },
    "grade": {
        "type": "keyword",
        "index": True
    },
    "registration": {
        "type": "text",
    },
    "birthday": {
        "type": "text",
    },
}

WEIBO_LEAD_MAPPING = {
    "lead_text": {
        "type": "text"
    },
}

# ------------微信mapping----------------
WECHAT_DETAIL_MAPPING = {
    "title": {
        "type": "text",
    },
    "author": {
        "type": "keyword",
    },
    "wechat_num": {
        "type": "keyword",
        "index": True,
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "contents": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "is_pics": {
        "type": "long",
        "index": True,
    },
    "img_url_list": {
        "type": "text",
    },
    "link": {
        "type": "text",
    },
    "is_share": {
        "type": "long",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

# ------------百度百家号mapping----------------
BAIJIAHAO_DETAIL_MAPPING = {
    "title": {
        "type": "text",
    },
    "author": {
        "type": "keyword",
    },
    "introduction": {
        "type": "text",
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "avatar_img": {
        "type": "text",  # 字符串
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "contents": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "is_pics": {
        "type": "long",
        "index": True,
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "img_url_list": {
        "type": "text",
    },
    "link": {
        "type": "text",
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

# ------------百度贴吧mapping----------------
TIEBA_DETAIL_MAPPING = {
    "title": {
        "type": "text",
    },
    "contents": {
        "type": "text",
    },
    "tieba": {
        "type": "text",
        "index": True,
    },
    "author": {
        "type": "keyword",
        "index": True,
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "is_pics": {
        "type": "long",
        "index": True,
    },
    "img_url_list": {
        "type": "text",
        "index": True,
    },
    "b_keywold": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

TIEBA_COMMENT_MAPPING = {
    "user_name": {
        "type": "keyword",
        "index": True,
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "contents": {
        "type": "text",
    },
    "nick_name": {
        "type": "keyword",
        "index": True,
    },
    "level": {
        "type": "keyword",
        "index": True,
    },
    "level_explain": {
        "type": "text",
    },
    "cur_score": {
        "type": "text",
    },
    "name_u": {
        "type": "text",
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "source": {
        "type": "keyword",
        "index": True,
    },
    "platform": {
        "type": "keyword",
        "index": True,
    },
    "comment_no": {
        "type": "keyword",
        "index": True,
    },
    "comment_num": {
        "type": "long",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "is_pics": {
        "type": "long",
        "index": True,
    },
    "img_url_list": {
        "type": "text",
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

TIEBA_USER_MAPPING = {
    "user_name": {
        "type": "keyword",
        "index": True,
    },
    "nick_name": {
        "type": "keyword",
        "index": True,
    },
    "gender": {
        "type": "keyword",
        "index": True,
    },
    "tieba_age": {
        "type": "keyword",
        "index": True,
    },
    "statuses_count": {
        "type": "long",
        "index": True,
    },
    "vip_day": {
        "type": "keyword",
        "index": True,
    },
    "is_vip": {
        "type": "long",
        "index": True,
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "follow_count": {
        "type": "keyword",
        "index": True,
    },
    "fan_count": {
        "type": "keyword",
        "index": True,
    },
    "profile_image_url": {
        "type": "text",
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    }
}
# ------------知乎mapping-------------------
# TODO 知乎文章详情
ZHIHU_DETAIL_MAPPING = {
    "id": {
        "type": "keyword",
        "index": True,
    },
    "user_name": {
        "type": "keyword",
        "index": True,
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "title": {
        "type": "text"
    },
    "description": {
        "type": "text",
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "update_time": {
        "type": "date",
        "index": True,
    },
    "contents": {
        "type": "text"
    },
    "like": {
        "type": "long",
    },
    "comment_num": {
        "type": "long",
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "link": {
        "type": "text"
    },
    "is_has_href": {
        "type": "long",
        "index": True,
    },
    "is_pics": {
        "type": "long",
        "index": True,
    },
    "is_videos": {
        "type": "long",
        "index": True,
    },
    "img_url_list": {
        "type": "text",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

# TODO 知乎评论详情
ZHIHU_COMMENT_MAPPING = {
    "user_name": {
        "type": "keyword",
        "index": True,
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "like": {
        "type": "long"
    },
    "zhihu_id": {
        "type": "keyword",
        "index": True,
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "contents": {
        "type": "text"
    },
    "is_reply": {
        "type": "keyword",
        "index": True,
    },
    "reply_user": {
        "type": "keyword",
        "index": True,
    },
    "reply_user_id": {
        "type": "keyword",
        "index": True,
    },
    "is_author": {
        "type": "keyword",
        "index": True,
    },
    "is_parent_author": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    }
}

# TODO 知乎用户详情
ZHIHU_USER_MAPPING = {
    "id": {
        "type": "keyword",
        "index": True,
    },
    "url_token": {
        "type": "keyword",
        "index": True,
    },
    "user_name": {
        "type": "keyword",
        "index": True,
    },
    "headline": {
        "type": "text"
    },
    "gender": {
        "type": "keyword",
        "index": True,
    },
    "user_type": {
        "type": "keyword",
        "index": True,
    },
    "profile_image_url": {
        "type": "text"
    },
    "is_followed": {
        "type": "keyword",
        "index": True,
    },
    "is_following": {
        "type": "keyword",
        "index": True,
    },
    "topic_list": {
        "type": "keyword",
        "index": True,
    },
    "introduction": {
        "type": "text",
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    }
}

# ------------各类新闻网站mapping----------------
NEWS_DETAIL_MAPPING = {
    "title": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "source": {
        "type": "keyword",
        "index": True,
    },
    "author": {
        "type": "keyword",
        "index": True,
    },
    "link": {
        "type": "text",
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "contents": {
        "type": "text",
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

# ------------微博热搜mapping----------------
HOT_SEARCH_KEYWORD_WEIBO_MAPPING = {
    "index": {
        "type": "keyword",
        "index": True,
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "result": {
        "properties": {
            "heat": {
                "type": "keyword"
            },  # "fields": {"keyword": {"ignore_above": 256, "type": "keyword"}}},
            "time": {
                "type": "date"
            }
        }
    },
    "mark": {
        "type": "keyword",
        "index": True,
    },
    "w_url": {
        "type": "text",
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "text": {
        "type": "text"
    },
    "lead_text": {
        "type": "text"
    },
}

# ------------百度热搜和360热搜mapping----------------
HOT_SEARCH_KEYWORD_MAPPING = {
    "index": {
        "type": "keyword",
        "index": True,
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "text": {
        "type": "text"
    },
    "result": {
        "properties": {
            "heat": {
                "type": "keyword"
            },
            "time": {
                "type": "date"
            }
        }
    },
}

# ------------监控报纸mapping----------------
PAPER_ALL_MAPPING = {
    "title": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "week": {
        "type": "keyword",
        "index": True,
    },
    "word_num": {
        "type": "long"
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "author": {
        "type": "keyword",
        "index": True,
    },
    "column": {
        "type": "keyword",
        "index": True,
    },
    "page": {
        "type": "keyword",
        "index": True,
    },
    "pdf": {
        "type": "text"
    },
    "pdf_content": {
        "type": "text"
    },
    "link": {
        "type": "text"
    },
    "paper_name": {
        "type": "keyword",
        "index": True,
    },
    "abstract": {
        "type": "text"
    },
    "contents": {
        "type": "text"
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

#----------小木虫maping----------------#
MUCHONG_DETAIL_MAPPING = {
    "title": {
        "type": "text",
    },
    "author": {
        "type": "keyword",
    },
    "time": {
        "type": "date",
        "index": True,
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "contents": {
        "type": "text",
    },
    "id": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "link": {
        "type": "text",
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
    "subject_words": {
        "type": "nested",
        "properties": {
            "words": {
                "type": "keyword"
            },
            "num": {
                "type": "integer"
            }
        }
    }
}

if __name__ == '__main__':
    import datetime

    from service.db.utils.elasticsearch_utils import es_client

    _index_mapping = {
        "index_type":
            {
                "properties": PAPER_ALL_MAPPING
            }
    }
    es_client.create_index("all_paper_details", _index_mapping)
