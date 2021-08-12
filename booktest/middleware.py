from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIPSMiddleware(MiddlewareMixin):
    """中间件类"""
    EXCLUDE_IPS = ['127.0.0.1']

    def process_view(self, request, view_func, *args, **kwargs):
        """视图函数调用前调用"""
        if request.META['REMOTE_ADDR'] in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>你已经给拉黑了</h1>')


class MiddleWare(MiddlewareMixin):
    """测试中间件类"""

    def __init__(self, get_response):
        self.get_response = get_response
        print("重启服务器调用，只调用一次")

    def process_request(self, request):
        """产生request对象之后，url匹配之前调用"""
        print('---process_request---')

    def process_view(self, request, view_func, *view_args, **kwargs):
        print('---process_view---')

    def process_response(self, request, response):
        print('---process_resposne')
        return response
