#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Simple Flask App"""

from flask import Flask

app = Flask(__name__)

from app import routes