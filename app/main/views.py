# -*- encoding:utf-8 -*-


import os
from flask import render_template, session, redirect
from flask import url_for, current_app
from flask import request
from .. import db
from ..models import User, CS, CountResult, ClassInfo, SC, CE, CER, ClassResult, Principle
from . import main
from .forms import LoginForm
from flask import flash
from flask_login import current_user
from flask_login import login_user, logout_user, login_required
# 使用SQL语句
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# 网站主页：简历主页
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/score', methods=['GET', 'POST'])
def score():
    return render_template('score.html')

@main.route('/research', methods=['GET', 'POST'])
def research():
    return render_template('research.html')