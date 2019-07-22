#! /usr/bin/python3
# -*- coding: utf-8 -*-


# ---------微博mapping--------------
WEIBO_DETAIL_MAPPING = {
    "weibo_time": {
        "type": "date",
        "index": True,
    },
    "platform": {
        "type": "keyword",
    },
    "contents": {
        "type": "text",
    },
    "weibo_id": {
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
    "like_num": {
        "type": "long",
    },
    "com_num": {
        "type": "long",
    },
    "repost_num": {
        "type": "long",
    },
    "is_forward": {
        "type": "integer",
    },
    "is_forward_weibo_id": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "key_user_list": {
        "type": "text",
    },
    "forward_user_url_list": {
        "type": "text",
    },
    "b_keyword": {
        "type": "keyword",
        "index": True,
    },
    "topic": {
        "type": "text",
    },
    "has_href": {
        "type": "long",
        "index": True,
    },
    "pics": {
        "type": "long",
        "index": True,
    },
    "videos": {
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
    "comment_time": {
        "type": "date",
        "index": True,
    },
    "platform": {
        "type": "keyword",
        "index": True
    },
    "comment_contents": {
        "type": "text",
    },
    "comment_id": {
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
    "comment_like": {
        "type": "long",
    },
    "key_user_list": {
        "type": "text",
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
    "repost_time": {
        "type": "date",
        "index": True,
    },
    "platform": {
        "type": "keyword",
        "index": True
    },
    "repost_contents": {
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
    "repost_like": {
        "type": "long",
    },
    "key_user_list": {
        "type": "text",
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
        "type": "text",
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
        "type": "text",
    },
    "registration": {
        "type": "text",
    },
    "birthday": {
        "type": "text",
    },
}

# ------------微信mapping----------------


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
    "article_date": {
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
    "article_text": {
        "type": "text",
    },
    "article_id": {
        "type": "keyword",
        "index": True,
    },
    "type": {
        "type": "keyword",
        "index": True,
    },
    "pics": {
        "type": "long",
        "index": True,
    },
    "user_id": {
        "type": "keyword",
        "index": True,
    },
    "img_url": {
        "type": "text",
    },
    "article_url": {
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
    "content": {
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
    "tiezi_time": {
        "type": "date",
        "index": True,
    },
    "pics": {
        "type": "long",
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
    "tid": {
        "type": "keyword",
        "index": True,
    },
    "fid": {
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
    "user": {
        "type": "keyword",
        "index": True,
    },
    "date": {
        "type": "date",
        "index": True,
    },
    "replay_text": {
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
    "level_name": {
        "type": "text",
    },
    "cur_score": {
        "type": "text",
    },
    "name_u": {
        "type": "text",
    },
    "author_id": {
        "type": "keyword",
        "index": True,
    },
    "replay_id": {
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
    "replay_no": {
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
    "pics": {
        "type": "long",
        "index": True,
    },
    "img_url": {
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
    "user": {
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
    "tiezi_num": {
        "type": "long",
        "index": True,
    },
    "vip_days": {
        "type": "keyword",
        "index": True,
    },
    "is_vip": {
        "type": "long",
        "index": True,
    },
    "author_id": {
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
