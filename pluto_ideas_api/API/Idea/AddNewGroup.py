# -*- coding: utf-8 -*-
import json

import flask
from flask import current_app as app, request

from pluto_ideas_api.Classes.BaseResponse import BaseResponse

# Blueprint Configuration
idea_addnewgroup_bp = flask.Blueprint(
    'addnewgroup', __name__,
    template_folder='templates',
    static_folder='static'
)


@idea_addnewgroup_bp.route('/idea/add_new_group', methods=['POST'])
def add_new_group():
    """/idea/add_new_group"""
    text_json = request.json
    text = text_json['text']
    tags = text_json['tags']
    name = text_json['name']
    author_id = text_json['author_id']
    max_id = 0
    for group in app.ideas:
        if group['id'] > max_id:
            max_id = group['id']
    new_group = {
        "id": max_id + 1,
        "name": name,
        "ideas": [
            {
                "name": name,
                "id": 1,
                "author_id": author_id,
                "text": text,
                "tags": tags,
                "rating": 1
            }
        ],

    }
    app.ideas.append(new_group)
    return json.dumps({'result': True, 'group': new_group})


@idea_addnewgroup_bp.after_request
def add_cors_headers(response):
    if request.referrer is not None:

        r = request.referrer[:-1]
        white = ['http://localhost:3000', 'http://localhost:8080', 'http://45.90.34.42']

        if r in white:
            response.headers.add('Access-Control-Allow-Origin', r)
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
            response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
            response.headers.add('Access-Control-Allow-Headers', 'Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response
