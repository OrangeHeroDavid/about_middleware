from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect,ensure_csrf_cookie
from django.views import View
from django.utils.decorators import method_decorator


def index(request, id):
    print(id)
    print('index')
    # print(111,id(request))
    # print(request.xxx)

    ret = HttpResponse('ok')

    # int('aaa')

    def xx():
        return HttpResponse('from xxx')

    #
    # ret.render =xx

    return ret


# @csrf_protect
def login(request):
    return render(request, 'login.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    @method_decorator(csrf_protect)
    def post(self, request):
        print(request.POST)
        return HttpResponse('o98k')
