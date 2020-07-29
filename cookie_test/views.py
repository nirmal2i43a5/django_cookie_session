from django.shortcuts import render

# Create your views here.\\
from datetime import datetime,timedelta

def setCookie(request):
    response =  render(request,'cookie/set_cookie.html')#use this variable to send cookie
    response.set_cookie('name','nirmal',expires = datetime.utcnow()+timedelta(days=2) )#expires in 60 seconds
    #u set this value to the web server('keys','values')
    
    return response

#go to chrome://settings/cookies/ to see whether it is working or not

#Now how to read that from web server to browser or client
def getCookie(request):
    # nm = request.COOKIES['name']#['keys]
    
    #can also access using get method
    # nm = request.COOKIES.get('name')
    nm = request.COOKIES.get('name','Guest')
    #same as above but u can also get default value using get method
    #second params is the default value is cookie is not set ,if second params is not set then it gives none instead of error
    return render(request,'cookie/get_cookie.html',{'name':nm})

#delete cookie from your client browser
def delete(request):
    response =  render(request,'cookie/delete_cookie.html')
    response.delete_cookie('name')
    return response
    
