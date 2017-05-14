#-*- coding:utf-8 -*-
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline2.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    length = len(chars) -1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type == "register":
        email_title = "慕雪网注册激活链接"
        email_body = "您好，您的邮箱已在慕雪网注册成功，请点击下面的链接激活: http://127.0.0.1:8000/active/{0}如非本人操作请勿点击".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "找回密码"
        email_body = "请点击下面的链接修改密码: http://127.0.0.1:8000/reset/{0}如非本人操作请勿点击".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass