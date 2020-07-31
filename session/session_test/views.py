from django.shortcuts import render

# Create your views here.

def setSession(request):
    request.session['name'] = 'Nirmal' #this data is save to database so db migrate is necessaty while using session
    #session is dict type object
    #by default when you create session it default expire data is two weeks 
    #when u look in client browser then instead of name u see sessionid and in value u will see session value
  
    request.session['lname'] = 'pandey'
    return render(request,'session/setSession.html')






#Read session 
def getSession(request):
    # name = request.session['name']#it gives name
    name = request.session.get('name',default='Guest')
    # lname = request.session.get('lname')
    keys = request.session.items()#values() access value,items() both key and values
    # age = request.session.setdefault('age','45')#using getdefault also create and give u value
    return render(request,'session/getSession.html',{'name':name,
                         'keys':keys,
                        #  'age':age,
                                                     })




#delete from backend

def delsession(request):
    if 'name' in request.session:
        del request.session['name']#data is deleted but not session in the browser
    # request.session.flush() #it deletes session id
    
    return render(request,'session/delSession.html')
    
        

    
    
