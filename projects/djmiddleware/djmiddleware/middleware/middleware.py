from django.http import HttpResponseForbidden

class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the incoming request
        print(f"Incoming request: {request.method} {request.path}")

        response = self.get_response(request)

        # Log the outgoing response
        print(f"Outgoing response: {response.status_code} for {request.method} {request.path}")

        return response
    
class BlockingMiddleware:
    def __init__(self, getResponse):
        self.getResponse = getResponse

    def __call__(self, request):
        if request.path == "/blocked/":
            return HttpResponseForbidden("This path is blocked.")
        print(f"Processing request for {request.path}")
        response = self.getResponse(request)
        return response


class IPBlockingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = ["192.168.1.100"]

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def __call__(self, request):

        if ip := self.get_client_ip(request) in self.blocked_ips:
            return HttpResponseForbidden("Your IP is blocked.")
        return self.get_response(request)
    

class CheckBMPIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/store/":
            bmp_id = request.headers.get('bmp-id')
            if not bmp_id:
                return HttpResponseForbidden("BMP ID is required.")
            else:
                print(f"Valid BMP ID: {bmp_id}")
        return self.get_response(request)