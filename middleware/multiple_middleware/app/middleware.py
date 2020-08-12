


class brotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Brother initialization")
        
    def __call__(self,request):
        print("This is Brother before view")
        response = self.get_response(request)
        print("THis is Brother after view")
        return response
class fatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time father initialization")
        
    def __call__(self,request):
        print("This is father before view")
        response = self.get_response(request)
        print("THis is father after view")
        return response
    
class motherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time mother initialization")
        
    def __call__(self,request):
        print("This is mother before view")
        response = self.get_response(request)
        print("THis is mother after view")
        return response



