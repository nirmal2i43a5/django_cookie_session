from django.shortcuts import render,HttpResponse


# Create your views here.

def setSession(request):
    request.session['name'] = 'Retrica' #this data is save to database so db migrate is necessary while using session
    #session is dict type object
    #by default when you create session it default expire data in two weeks 
    #when u look in client browser then instead of name u see sessionid and in value u will see session value
  
    request.session['lname'] = 'pandey'
    return render(request,'session/setSession.html')

#Read session 
def getSession(request):
    #when refresh it checks name
    if 'name' in request.session:#after 20 sec(SESSION_COOKIE_AGE = 20 in settings.py) name will not be in session so go to else
        #if u want to expire(get page) data after 20 sec then use this 
        name = request.session['name']#it gives name
        # name = request.session.get('name',default='Guest')
        
        request.session.modified = True#b4 i use this then refresh after 20 sec it expire  default is false
        # but modified = True means it does not expire it in if the user is active otherwise it expires even when the user is active
    
        return render(request,'session/getSession.html',{'name':name })
    else:
        return HttpResponse("Your session has expired")
  
  
#delete from backend
def delSession(request):
    if 'name' in request.session:
        del request.session['name']#data is deleted but not session in the browser
    # request.session.flush() #it deletes session id
    
    return render(request,'session/delSession.html')
    
        

    
    
