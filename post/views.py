from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.http import HttpResponseBadRequest,HttpResponseNotFound
from user.views import auth
from user.models import User
import simplejson
import datetime
from .models import Post,Content
import math



@auth
def pub(request:HttpRequest):
    #return HttpResponse(b'pub')

    try:
        post = Post()
        content = Content()
        payload = simplejson.loads(request.body)
        post.title = payload['title']
        post.author = User(request.user.id)  #注入进去
        post.postdate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        post.save()

        content.content = payload['content']
        content.post = post
        content.save()
        return JsonResponse({'post_id':post.id})
    except Exception as e:
        #print(e)
        return HttpResponseBadRequest()


def get(request,id):
    try:
        id = int(id)
        post = Post.objects.get(pk=id)

        if post:
            return JsonResponse({
                'post':{
                    'post_id':post.id,
                    'title':post.title,
                    'author':post.author.name,
                    'author_id':post.author_id,
                    'postdate':post.postdate.timestamp(),
                    'content':post.content.content
                }
            })
    except Exception as e:
        #print(e)
        return HttpResponseNotFound()



# def getall(request):
#
#     try:
#         page = int(request.GET.get('page',1))
#         page = page if page > 0 else 1
#     except:
#         page = 1
#
#     try:
#         size = int(request.GET.get('size',20))
#         size = size if size > 0 and size < 101 else 20
#     except:
#         size = 20
#
#     try:
#         start = (page-1)*size
#         posts = Post.objects.order_by('-id')[start:start+size]
#         count = posts.count()
#         return JsonResponse({
#             'posts':[
#                 {
#                     'post_id':post.id,
#                     'title':post.title
#                 }for post in posts
#             ],'pagination':{
#                 'page':page,
#                 'size':size,
#                 'count':count,
#                 'pages':math.ceil(count/size)
#             }
#         })
#
#     except Exception as e:
#         print(e)
#         return HttpResponseBadRequest()

def validate(d:dict,name:str,type_fun,defalut,validate_func):
    try:
        result = type_fun(d.get(name,defalut))
        result = validate_func(result,defalut)
    except:
        result = defalut
    return  result



def getall(request):

    page = validate(request.GET,'page',int,1,lambda x,y:x if x>0 else 1)
    size = validate(request.GET,'size',int,20,lambda x,y:x if x>0 and x<101 else y)

    try:
        start = (page-1)*size
        posts = Post.objects.order_by('-id')[start:start+size]
        #print(posts,1111)
        qs = Post.objects
        count1 = qs.count()
        count = posts.count()
       # print(count1,222222)
        #print(count,33333)
        return JsonResponse({
            'posts':[
                {
                    'post_id':post.id,
                    'title':post.title
                }for post in posts
            ],'pagination':{
                'page':page,
                'size':size,
                'count':count1,
                'pages':math.ceil(count1//size)
            }
        })

    except Exception as e:
        #print(e)
        return HttpResponseBadRequest()



