# #
# # import jwt
# #
# # key = 'selecet'
# # token = jwt.encode({'plsyload':'abc123'},key,'HS256')
# # print(token)
# #
# # header,payload,signature = token.split(b'.')
# # print(header)
# # print(payload)
# # print(signature)
# #
# # import base64
# #
# # def addep(b:bytes):
# #     rem = len(b) % 4
# #     return b + b'='*rem
# #
# # print('header=',base64.urlsafe_b64decode(addep(header)))
# # print('payload=',base64.urlsafe_b64decode(addep(payload)))
# # print('sginature=',base64.urlsafe_b64decode(addep(signature)))
# #
# # from jwt import algorithms
# # alg = algorithms.get_default_algorithms()['HS256']
# # newkey = alg.prepare_key(key)
# #
# # signing_input,_,_=token.rpartition(b'.')
# # print(signing_input)
# #
# # signature = alg.sign(signing_input,newkey)
# # print('+++++++++++++++++++++')
# # print(signature)
# # print(base64.urlsafe_b64encode(signature))
# #
# # import json
# # print(base64.urlsafe_b64encode(json.dumps({'payload':'abc'}).encode()))
# #
#
#
# import bcrypt
# import datetime
#
# password = b'123456'
#
# #拿到的盐不同
# print(1,bcrypt.gensalt())
# print(2,bcrypt.gensalt())
#
# salt = bcrypt.gensalt()
# #得到同样的盐，密文一样
# print('-------------same salt-------------')
# x = bcrypt.hashpw(password,salt)
# print(3,x)
# x = bcrypt.hashpw(password,salt)
# print(4,x)
#
# #盐不同，得到的密文也不一样
# print('-----------different salt-------------')
# x = bcrypt.hashpw(password,bcrypt.gensalt())
# print(5,x)
# x = bcrypt.hashpw(password,bcrypt.gensalt())
# print(6,x)
#
# #校验
# print(7,bcrypt.checkpw(password,x),len(x))
# print(8,bcrypt.checkpw(password+b'',x),len(x))
#
# #计算时长
# start = datetime.datetime.now()
# y = bcrypt.hashpw(password,bcrypt.gensalt())
# dalta = (datetime.datetime.now()-start)
# print(9,'duration={}'.format(dalta))
#
#
# #校验时长
# start = datetime.datetime.now()
# y1 = bcrypt.checkpw(password,x)
# delta1 = (datetime.datetime.now()-start).total_seconds()
# print(y1)
# print(10,delta1)
#
# start = datetime.datetime.now()
# y2 = bcrypt.checkpw(b'1',x)
# delta2 = (datetime.datetime.now()-start).total_seconds()
# print(y2)
# print(11,delta2)

# from .blog.settings import SECRET_KEY
#
# print(SECRET_KEY)





# from captcha.audio import AudioCaptcha
# def test_audio_generate():
# captcha = AudioCaptcha()
# data = captcha.generate('1234')
# assert bytearray(b'RIFF') in data


from django.http import HttpRequest
#
# def getall(request):
#     page(request)
#     size(request)
#
#
# def page(d:dict,name:str,convert,default):
#     try:
#         page = request.GET.get('page')
#         page = int(page)
#         page = page if page>0 else 1
#     except Exception:
#         page = default
#
#     return page







for i in range(9):
    print(i%2)



