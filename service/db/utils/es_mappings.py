#! /usr/bin/python3
# -*- coding: utf-8 -*-


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
        "index": "not_analyzed"
    },
    "mid": {
        "type": "keyword",  # 字符串
        "index": "not_analyzed"
    },
    "user_id": {
        "type": "keyword",
        "index": "not_analyzed"
    },
    "like_num": {
        "type": "long",
        "index": "not_analyzed"
    },
    "com_num": {
        "type": "long",
        "index": "not_analyzed"
    },
    "repost_num": {
        "type": "long",
        "index": "not_analyzed"
    },
    "is_forward": {
        "type": "integer",
    },
    "is_forward_weibo_id": {
        "type": "text",
        "index": "not_analyzed"
    },
    "type": {
        "type": "keyword",
        "index": "not_analyzed"
    },
    "key_user_list": {
        "type": "text",
        "index": "not_analyzed"
    },
    "forward_user_url_list": {
        "type": "text",
        "index": "not_analyzed"
    },
    "b_keyword": {
        "type": "keyword",
        "index": "not_analyzed"
    },
    "topic": {
        "type": "text",
        "index": "not_analyzed"
    },
    "has_href": {
        "type": "long",
        "index": "not_analyzed"
    },
    "pics": {
        "type": "long",
        "index": "not_analyzed"
    },
    "videos": {
        "type": "long",
        "index": "not_analyzed"
    },
    "crawl_time": {
        "type": "date",
        "index": True,
    },
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
        "index": "not_analyzed"
    },
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
        "index": "not_analyzed"
    },
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
