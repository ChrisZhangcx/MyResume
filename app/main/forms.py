# -*- coding:utf-8 -*-

# 此处为表单的定义
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange


# 表单类
# 用户登录表单
class LoginForm(Form):
    # 输入帐号
    username = StringField(u'账号', validators=[DataRequired(), Length(1,12)])
    # 输入密码
    password = PasswordField(u'密码', validators=[DataRequired()])
    # 记住登录者
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')

# 用户注册表单
class RegisterForm(Form):
    # 输入账号：账号要求在12个字符之内，且不能与现有账号重复
    username = StringField(u'用户名', validators=[DataRequired(), Length(1,12)])
    # 输入密码：密码要求在8-20字符之间，只能由数字和字母构成，且必须同时有数字和字母
    password = PasswordField(u'密码', validators=[DataRequired(), Length(1,12)])