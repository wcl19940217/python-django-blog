from django.shortcuts import render

# Create your views here.

import logging
import simplejson
from django.http import HttpRequest,HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import User
from blog.settings import SECRET_KEY
import bcrypt
import datetime
import jwt
AUTH_EXPIRE = 60*60*8


def gen_token(user_id):
    ret = jwt.encode({
        'user_id':user_id,
        'exp':int(datetime.datetime.now().timestamp()) + AUTH_EXPIRE
    },SECRET_KEY,'HS256').decode()
    return ret

def reg(request):

    try:
        playload = simplejson.loads(request.body.decode())
        email = playload['email']
        query = User.objects.filter(email=email)
        #query = User.objects.filter(Q(email__startswith='www'))

        #s1 = [user.name for user in User.objects.all()]  #没有缓存，每次都要查库
        #print(s1,'===============')
        #qs = User.objects.all()
        #s2 = [user.name for user in qs]    #有缓存，使用的是缓存集
        #s3 = [user.name for user in qs]
        # print(s2,'-------------')
        # print(s3,'+++++++++++++')

        #print(query)
        if query:
            return HttpResponseBadRequest()

        name = playload['name']
        password = bcrypt.hashpw(playload['password'].encode(),bcrypt.gensalt())
        print(1,email,2,name,3,password)
        user = User()
        user.password = password
        user.name = name
        user.email = email

        try:
            user.save()  #数据库中提交数据

            # return HttpResponse('user.reg')
            return JsonResponse({'token':gen_token(user.id)})
        except Exception as e:
            #print(e,'+++++++++++++++++++++')
            raise  #会抛出最近一个异常
    except Exception as e:
        #print(e,'-------------------')
        return HttpResponseBadRequest()


def login(request:HttpRequest):

    try:
        playload = simplejson.loads(request.body)
        email = playload['email']
        user = User.objects.filter(email=email).get()
        if not user:
            return HttpResponseBadRequest()

        if not bcrypt.checkpw(playload['password'].encode(),user.password.encode()):
            return HttpResponseBadRequest()

        return JsonResponse({
                'user':{
                    'user_id':user.id,
                    'name':user.name,
                    'email':user.email
                },'token':gen_token(user.id)
            })

    except Exception as e:
        # print(e,'++++++++++++++++++')
        return HttpResponseBadRequest()


# AUTH_EXPIRE = 60*60*8
#
# def test(request:HttpRequest):
#     pass
#
# def auth(request:HttpRequest):
#     #提取用户提交的jwt
#     token = request.META.get('HTTP_JWT')
#
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
#         print(payload)
#
#         if (datetime.datetime.now().timestamp()-payload['timestamp']) > AUTH_EXPIRE:
#             return HttpResponseBadRequest()
#
#         return HttpResponse(b'test jwt')
#
#     except Exception as e:
#         print(e)
#         return HttpResponse(status=401)





def auth(view):
    def wrapper(request:HttpRequest):
    #提取用户提交的jwt
        token = request.META.get('HTTP_JWT')

        if not token:
            return HttpResponse(status=401)

        try:   #解码同时，验证过期问题
            payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
            #print(payload)

            # if (datetime.datetime.now().timestamp()-payload['timestamp']) > AUTH_EXPIRE:
            #     return HttpResponseBadRequest()

            user_id = payload.get('user_id',-1)
            user = User.objects.filter(pk=user_id).get()
            request.user = user

            return view(request)

        except Exception as e:
            #print(e)
            return HttpResponse(status=401)
    return wrapper

@auth
def test(request:HttpRequest):
    return HttpResponse(b'test jwt')