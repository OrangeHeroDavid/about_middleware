from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MD1(MiddlewareMixin):

    def process_request(self, request):
        print(id(request))
        # request.xxx = 's16'
        print('form MD1 process_request')
        # return HttpResponse('o98k')

    def process_response(self, request, response):
        # print(id(response))
        print('form MD1 process_response')

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(view_func)
        # print(view_args)
        # print(view_kwargs)
        print('form MD1 process_view')

        # return HttpResponse('xxxx')

    def process_exception(self, request, exception):
        print('form MD1 process_exception')
        print(exception)

    def process_template_response(self, request, response):
        print('form MD1 process_template_response')
        return response


class MD2(MiddlewareMixin):

    def process_request(self, request):
        print('form MD2 process_request')

    def process_response(self, request, response):
        print('form MD2 process_response')

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(view_args)
        print(view_kwargs)
        print('form MD2 process_view')

    def process_exception(self, request, exception):
        print('form MD2 process_exception')
        print(exception)

        return HttpResponse('404')


visit_dict = {}

import time


# class Throttle(MiddlewareMixin):
#     def process_request(self, request):
#         # 获取IP
#         ip = request.META.get('REMOTE_ADDR')
#
#         # 获取到访问记录
#         history = visit_dict.get(ip, [])
#         if not history:
#             visit_dict[ip] = history
#
#         # 获取当前时间
#         now = time.time()
#
#         # history  [ 9:16:30  ,  9:16:35,  9:16:40 ]   9:26:50
#         # history  [  9:16:40 , 9:16:35, 9:16:30  ,]   9:26:50
#
#         # new = []
#         # for i in history:
#         #     if now - i > 5:
#         #         new.append(i)
#         #
#         # for i in new:
#         #     history.remove(i)
#         while history and now - history[-1] > 5:
#             history.pop()
#
#         if len(history) >= 3:
#             return HttpResponse('你的访问频率太快了，你歇一会')
#
#         history.insert(0, now)


class Throttle(MiddlewareMixin):
    def process_request(self, request):

        # 获取到访问记录
        history = request.session.get('history',[])

        # 获取当前时间
        now = time.time()

        while history and now - history[-1] > 5:
            history.pop()

        if len(history) >= 3:
            return HttpResponse('你的访问频率太快了，你歇一会')

        history.insert(0, now)

        request.session['history'] = history
