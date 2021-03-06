# -*- coding: utf-8 -*-
import json

import flask
from flask import current_app as app, request

# Blueprint Configuration
idea_gettopgroups_bp = flask.Blueprint(
    'getideasrating_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@idea_gettopgroups_bp.route('/idea/get_top_groups', methods=['GET'])
def get_ideas_rating():
    """/idea/get_ideas_rating"""
    data = app.ideas
    groups_dict = {}
    for group in data:
        rating = 0
        for idea in group['ideas']:
            rating += idea['rating']
        rating = rating / len(group['ideas'])
        groups_dict[(group['id'], group['name'])] = rating

    groups = list(groups_dict.items())
    groups.sort(key=lambda x: x[1], reverse=True)

    return json.dumps({'result': True, 'groups': [{'name': tag[1], 'id': tag[0], 'rating': count}
                                                  for tag, count in groups]})


@idea_gettopgroups_bp.after_request
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
