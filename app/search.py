# -*- coding: utf-8 -*-
from flask import current_app

"""
-------------------------------------------------
   File Name：     search
   Description :
   Author :       burt
   date：          2019-02-04
-------------------------------------------------
   Change Activity:
                   2019-02-04:
-------------------------------------------------
"""


def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, doc_type=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index, id=model.id)


def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    search_res = current_app.elasticsearch.search(
        index=index,
        doc_type=index,
        body={
            'query': {'multi_match': {'query': query, 'fields': ['*']}},
            'from': (page - 1) * per_page,
            'size': per_page
        })

    ids = [int(hit['_id']) for hit in search_res['hits']['hits']]
    return ids, search_res['hits']['total']
