# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password


from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email



class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))#Q的引入让方法可以判断并集
            if user.check_password(password):
                return user
        except Exception:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, "html/register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "html/register.html", {"register_form":register_form, "msg":"用户已存在"})
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, "register")
            return render(request, "html/login.html", {"msg":"注册成功！"})
        else:
            return render(request, "html/register.html", {"register_form":register_form})


class LoginView(View):

    def get(self, request):#自动判断 是get方法就引用这个
        return render(request, "html/login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "html/index.html")
                else:
                    return render(request, "html/login.html", {"msg": "邮箱未激活", "login_form": login_form})
            else:
                return render(request, "html/login.html", {"msg": "用户名或密码错误了啊", "login_form": login_form})
        else:
            return render(request, "html/login.html", {"msg": "用户名或密码错误了啊", "login_form":login_form})


class ForgetPwdView(View):

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "html/forgetpwd.html", {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_sucess.html")
        else:
            return render(request, "html/forgetpwd.html", {'forget_form': forget_form})

class ResetView(View):

    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "html/password_reset.html", {"email":email})
        else:
            return render(request, "active_fail.html")
        return render(request, "html/login.html")


class ModifyPwdView(View):

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 == pwd2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd1)
                user.save()
                return render(request, "html/login.html")
            else:
                return render(request, "html/password_reset.html", {"email": email, "msg":"密码不一致"})
        else:
            email = request.POST.get("email", "")
            return render(request, "html/password_reset.html", {"email": email, "modify_form":modify_form})

class TestView(View):
    def get(self, request):
        return render(request, "html/course-detail.html")