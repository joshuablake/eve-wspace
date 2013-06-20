from threading import currentThread
_request_caches = {}

class Middleware(object):
    def process_request(self, request):
        get_request_cache().clear()
        
def get_request_cache():
    try:
        return _request_caches[currentThread]
    except KeyError:
        _request_caches[currentThread] = {} 
        return _request_caches[currentThread]